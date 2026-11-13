#!/usr/bin/env python3
"""Create a deterministic, offline draft embedded/ROS study plan.

No network calls; it cannot verify links, course versions, or job requirements.
Uses only Python 3.10+ standard library.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'assets' / 'resource_catalog.json'

ROLE_TAGS = {
    'embedded-firmware': {'c','stm32','esp32','rp2350','rtos','testing','hardware','protocols','safety'},
    'embedded-linux': {'linux','cpp','c','build','testing','protocols'},
    'bsp-driver': {'linux','stm32','c','hardware','build','testing'},
    'ros2-robotics': {'ros2','robotics','cpp','simulation','control','testing','linux'},
    'robot-low-level-software': {'ros2','robotics','rtos','stm32','cpp','control','safety','protocols'},
    'iot': {'wireless','esp32','rtos','stm32','protocols','testing','safety'},
    'general-embedded': {'c','cpp','stm32','rtos','protocols','testing'}
}
TRACK_SEQUENCE = {
    'C': 0, # professional C/C++ and build foundations
    'A': 1, # bare metal and peripherals
    'E': 2, # selected references at the time of use
    'B': 3, # RTOS and Linux
    'D': 4, # ROS 2 and robots
}

def load_catalog():
    data = json.loads(CATALOG.read_text(encoding='utf-8'))
    return data['resources']

def clean_list(value):
    if isinstance(value, list):
        return [str(v).strip().lower() for v in value if str(v).strip()]
    return []

def desired_tags(profile):
    roles=clean_list(profile.get('target_roles'))
    gaps=set(clean_list(profile.get('learning_gaps')))
    known=set(clean_list(profile.get('known_skills')))
    role_tags=set()
    for role in roles:
        role_tags |= ROLE_TAGS.get(role,set())
        for key,tags in ROLE_TAGS.items():
            if key in role or role in key:
                role_tags |= tags
    if not role_tags: role_tags=ROLE_TAGS['general-embedded']
    return role_tags,gaps,known

def score_resource(r, profile):
    tags=set(r.get('tags',[]))
    roles,gaps,known=desired_tags(profile)
    overlap_role=len(tags & roles)
    overlap_gaps=len(tags & gaps)
    # Historical ranks are editorial opinions; personalized selection is a heuristic.
    score=110 - r['tier']*19 - min(r['rank'],35)*0.45
    score+= min(overlap_role,4)*3.0 + min(overlap_gaps,3)*9.0
    if r['tier']==4: score-=20
    if r.get('evidence_code')=='X': score-=6
    boards=' '.join(clean_list(profile.get('available_hardware')))
    title=r['title'].lower()
    # Do not send a learner to board-specific documentation for hardware they lack.
    if ('nucleo-g474' in title or 'stm32cubeg4' in title) and not any(x in boards for x in ['g474','stm32g4']): score-=22
    if ('pico sdk' in title or 'rp2350' in title) and not any(x in boards for x in ['pico','rp2350','rp2040']): score-=18
    if ('esp-idf' in title or 'esp32' in title) and 'esp32' not in boards and 'iot' not in clean_list(profile.get('target_roles')): score-=16
    if r['domain_id']=='D' and not any('ros' in x or 'robot' in x for x in clean_list(profile.get('target_roles'))):score-=45
    return round(score,2)

def pick_resources(profile,n):
    rs=load_catalog()
    indexed={r['id']:r for r in rs}
    roles=clean_list(profile.get('target_roles'))
    role_tags,gaps,known=desired_tags(profile)
    robotics=any('ros' in x or 'robot' in x for x in roles)
    linux=any('linux' in x or 'bsp' in x for x in roles) or 'linux' in gaps
    firmware=any('firmware' in x or 'robot-low-level' in x or 'iot' in x for x in roles)
    ranked=sorted(rs,key=lambda r:(-score_resource(r,profile),r['tier'],r['rank']))
    selected=[]
    def add(id):
        r=indexed.get(id)
        if r and r not in selected and len(selected)<n:selected.append(r)
    # Core learning path anchors deliberately selected for educational dependency.
    add('C05')  # practical build systems
    if 'testing' in gaps or 'c' in role_tags: add('C07')
    if firmware or not linux: add('A01')
    if firmware or 'rtos' in gaps: add('B01')
    if linux: add('B03')
    if robotics:
        add('D01')
        add('D06')
    add('E01')
    if firmware and 'stm32' in ' '.join(clean_list(profile.get('available_hardware'))): add('A05')
    cap=max(3,(n+2)//3)
    counts=Counter(r['domain_id'] for r in selected)
    for r in ranked:
        if len(selected)>=n:break
        if r in selected or r['tier']==4:continue
        if counts[r['domain_id']]>=cap:continue
        if r['domain_id']=='D' and not robotics:continue
        selected.append(r);counts[r['domain_id']]+=1
    for r in ranked:
        if len(selected)>=n:break
        if r not in selected and r['tier']<4 and (r['domain_id']!='D' or robotics):selected.append(r)
    return sorted(selected,key=lambda r:(TRACK_SEQUENCE[r['domain_id']],r['tier'],r['rank']))

def markdown(profile,chosen):
    weeks=int(profile.get('weeks') or 12)
    hours=float(profile.get('hours_per_week') or 6)
    roles=profile.get('target_roles') or ['general-embedded']
    gaps=profile.get('learning_gaps') or ['firmware-debugging','testing']
    hardware=profile.get('available_hardware') or ['existing development board or PC']
    lines=['# Personalized Embedded & Robotics Learning Roadmap',
        '', '> **Generated offline from a 2026-11-12 catalogue.** No URLs, prices, SDK versions, or forum feedback were checked live. Scores represent editorial prioritization, not hiring probabilities.',
        '',f'**Targets:** {", ".join(roles)}  ',
        f'**Time:** {weeks} weeks × {hours:g} hours/week ≈ {weeks*hours:g} hours  ',
        f'**Available hardware:** {", ".join(hardware)}',
        '', '## Priority learning gaps', '']
    lines += [f'- {g}' for g in gaps]
    lines += ['', '## Sequenced resource shortlist', '', '| # | ID | Resource | Tier | Heuristic score | Primary outcomes |', '|---:|---|---|---|---:|---|']
    for i,r in enumerate(chosen,1):
        concise=r['curriculum'].replace('|','/')[:190]
        lines.append(f'| {i} | {r["id"]} | [{r["title"]}]({r["url"]}) | {r["tier"]} | {score_resource(r,profile):g} | {concise} |')
    lines += ['', '## Phases and exit criteria', '']
    # Allocate time proportionally; do not pretend each resource requires full completion.
    phases=[('Foundations and environment',0,0.2,'Build one reproducible C/C++/MCU example and write down debugging steps.'),
            ('MCU/RTOS implementation',0.2,0.5,'Implement one interrupt/DMA or message-passing feature with host tests.'),
            ('Linux / ROS 2 or specialization',0.5,0.8,'Demonstrate a cross-component interface or a simulated robot node.'),
            ('Capstone, metrics and interviews',0.8,1.0,'Publish reproducible build, tests, logs/measurements, and one debug postmortem.')]
    for title,a,b,exit_ in phases:
        start=max(1,int(weeks*a)+1)
        end=max(start,int(weeks*b))
        lines += [f'### Weeks {start}–{end}: {title}',f'- Approximate budget: {(b-a)*weeks*hours:.0f} hours.',f'- Exit criterion: {exit_}','']
    lines += ['## Capstone recommendation','',
        '**Firmware-focused:** sensor/timer → RTOS queue/notification → checked UART frames → Linux host tests, with bounded buffers, watchdog, fault logs, and quantitative jitter/recovery measurements.',
        '', '**Robotics-focused:** ROS 2 C++ → ros2_control → serial/CAN MCU motor interface → encoder feedback, with TF2, SLAM Toolbox, Nav2, launch tests, and a verified safety stop.',
        '', 'Choose the one aligned to your target role and actual hardware. Never invent measured results; collect raw logs and repeat tests.',
        '', '## First seven days','',
        '1. Confirm board, OS, firmware SDK and ROS distribution.','2. Set up build, debugger and source control.','3. Read the first resource selected for each relevant track.','4. Implement one tiny MCU or ROS 2 component.','5. Add a host-side unit test.','6. Reproduce one failure and document the diagnosis.','7. Commit a README describing next steps and measurable results.','',
        '## Evidence caveat','',
        'The source catalogue contains both direct community feedback (D) and less verified sources (P/N). Inspect individual `community_verdict` fields, validate compatibility from upstream documentation, and recheck live links before paying for a course.']
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile',type=Path,required=True,help='JSON profile (see assets/example)')
    p.add_argument('--top',type=int,default=12,help='number of resources, 5..30')
    p.add_argument('--output',type=Path,default=Path('roadmap.md'))
    args=p.parse_args()
    if not 5<=args.top<=30:p.error('--top must be 5 to 30')
    profile=json.loads(args.profile.read_text(encoding='utf-8'))
    if not isinstance(profile,dict):p.error('profile must be a JSON object')
    if not 1<=int(profile.get('weeks',12))<=104:p.error('weeks must be 1..104')
    if not 0.5<=float(profile.get('hours_per_week',6))<=80:p.error('hours_per_week must be 0.5..80')
    chosen=pick_resources(profile,args.top)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(markdown(profile,chosen),encoding='utf-8')
    print(f'Wrote {args.output} with {len(chosen)} resources')

if __name__=='__main__':main()
