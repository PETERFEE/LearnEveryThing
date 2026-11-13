#!/usr/bin/env python3
"""Validate the skill metadata, 146-resource inventory, and basic privacy hygiene.

No third-party packages or internet access required. Not a live URL checker.
"""
from __future__ import annotations
import json
from pathlib import Path
import re
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]

def validate():
    errors=[]
    skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
    front=re.match(r'\A---\n(.*?)\n---\n',skill,re.S)
    if not front: errors.append('SKILL.md is missing YAML frontmatter')
    else:
        name=re.search(r'^name:\s*(.+)$',front.group(1),re.M)
        desc=re.search(r'^description:\s*(.+)$',front.group(1),re.M)
        if not name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name.group(1).strip()):errors.append('invalid skill name')
        elif name.group(1).strip()!=ROOT.name: errors.append('name and folder mismatch')
        if not desc or len(desc.group(1))>1024:errors.append('invalid description')
    data=json.loads((ROOT/'assets'/'resource_catalog.json').read_text(encoding='utf-8'))
    rs=data['resources']
    if len(rs)!=146:errors.append(f'Expected 146 resources; got {len(rs)}')
    ids=[r.get('id') for r in rs]
    if len(set(ids))!=len(ids):errors.append('duplicate resource IDs')
    domains=Counter(r.get('domain_id') for r in rs)
    if domains!={'A':31,'B':29,'C':26,'D':35,'E':25}:
        errors.append(f'wrong domain distribution: {domains}')
    required={'title','url','provider','format','curriculum','style_prerequisites','community_verdict','evidence_code','general_fit','tags','domain_id','rank','tier'}
    for r in rs:
        missing=required-set(r)
        if missing:errors.append(f'{r.get("id")}: missing fields {missing}')
        if not str(r.get('url','')).startswith('https://') and not str(r.get('url','')).startswith('http://'):
            errors.append(f'{r.get("id")}: bad url syntax')
        if r.get('tier') not in (1,2,3,4):errors.append(f'{r.get("id")}: tier out of range')
        if r.get('evidence_code') not in ('D','P','N','X'):errors.append(f'{r.get("id")}: bad evidence code')
        if not isinstance(r.get('tags'),list):errors.append(f'{r.get("id")}: tags must be a list')
    # Heuristic privacy scan of *published content*, not this validator's own source.
    blocked=[r'\bgmail\.com\b',r'linkedin\.com/in/',r'\bmy account memory\b',r'\bprivate chat export\b',r'\bpersonal relevance\b']
    content_files=[ROOT/'SKILL.md',ROOT/'README.md',ROOT/'assets'/'resource_catalog.json',
                   ROOT/'assets'/'learner_profile.example.json',ROOT/'assets'/'output_example.md']
    content_files+=list((ROOT/'references').glob('*.md'))
    for path in content_files:
        t=path.read_text(encoding='utf-8')
        for pattern in blocked:
            if re.search(pattern,t,re.I):
                errors.append(f'possible personal information: {path.relative_to(ROOT)}: {pattern}')
    return errors

if __name__=='__main__':
    issues=validate()
    if issues:
        for i in issues: print('ERROR:',i)
        raise SystemExit(1)
    print('OK: SKILL.md, 146 unique resources, tags, evidence codes and privacy screen')
