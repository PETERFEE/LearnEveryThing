---
name: embedded-robotics-learning-architect
description: Build personalized, evidence-aware learning plans for embedded firmware, ARM Cortex-M, FreeRTOS/Zephyr, C/C++, embedded Linux, and ROS 2 robotics. Use when a learner asks what to study, wants to compare courses/books, prepare for embedded or robotics jobs, audit technical gaps, create a learning roadmap, or plan an MCU-to-ROS capstone. Includes a curated 146-resource catalog and optional offline Python planner. Do not use for unrelated careers or assume course links and version compatibility are current without checking.
license: MIT
metadata:
  author: Community-maintained learning-skill template
  version: "1.0.0"
---

# Embedded & Robotics Learning Architect

Create a practical study plan with citations and measurable projects. Treat the bundled catalog as a **historical curated starting point**, not proof of real-time availability or universal community agreement.

## When to use

Activate for: embedded C/C++, microcontrollers (ARM Cortex-M, STM32, ESP32, RP2350), peripheral drivers, FreeRTOS/Zephyr, embedded Linux, firmware testing, CMake, ROS 2, Gazebo, Nav2, SLAM, micro-ROS, robotics career transitions, or resource comparisons.

Do not activate for: generic programming tutoring with no embedded/robotics context, unrelated professions, or direct claims of live job vacancies without checking external sources.

## Required inputs (ask only if needed)

Infer known details from the **current conversation**; never assume access to the skill creator's private history. Capture: target role(s), current evidence-based skills, level, available hardware/computer OS, weekly hours, deadline, budget, preferred language, and preferred learning formats. If some are missing, proceed using labeled assumptions and offer one targeted follow-up question if it would materially change recommendations.

Use `assets/learner_profile.example.json` as a machine-readable template, **not** a default user profile. Do not adopt its details unless the user supplies them.

## Workflow

1. **Profile and gap map.** Distinguish demonstrated project outcomes from self-reported familiarity. Group strengths and weaknesses across C/C++, MCU architecture, interfaces/DMA/interrupts, RTOS, debugging, embedded Linux, ROS 2, robotics control, testing, and build/deployment. Map to the target role with a maximum of 5–8 priority gaps.
2. **Select an appropriate track.** Default tracks: (a) embedded firmware, (b) embedded Linux/BSP, (c) ROS 2 robotics/robot low-level software, (d) cross-stack MCU ↔ ROS 2. Use the learner's time and hardware; avoid unnecessary purchases or duplicate beginner courses.
3. **Load the resource inventory.** Read `assets/resource_catalog.json` (146 original entries) as needed. Use `references/ranking-methodology.md` to evaluate learning return and evidence. Default: select **10–15 resources**, not all 146. Present a full 100+ comparison only on explicit request.
4. **Verify freshness when browsing is available.** Check release support and exact distro/SDK pairings with official ROS, Gazebo, FreeRTOS, ST, Espressif and kernel docs. Check course enrollment/link if recommending purchase, and collect independent practitioner reviews where possible. Treat forum discussions as anecdotes, not broad consensus. Distinguish `D` (direct resource feedback), `P` (primary documentation), `N` (no independent verdict), and `X` (outdated/incompatibility evidence). Do not say a link is live-tested if it was not checked. Cite external evidence with accessible links and dates.
5. **Rank explicitly, not by marketing popularity.** Use baseline weights: role fit 35%, technical depth 25%, hands-on transfer 15%, compatibility/maintenance 15%, and community evidence 10%. Adapt weights to learner needs and state deviations. Treat scores as judgment-based; never fabricate measurements. Explain why a higher-tier item beats an alternative.
6. **Write chronological roadmap.** Prioritize 6–15 resources by dependencies and available hours. Each phase must contain objective, concrete build/test exercise, time budget, exit criterion, and job-interview evidence. Keep theory/practice balanced. When target is >8 weeks, propose early application/interview practice concurrently.
7. **Specify capstone(s).** Supply at least one capstone with system block diagram or text interface map, architecture, exact reproducibility tools, safety/fault behavior where motors/actuators are involved, automated tests, and quantitative metrics *to be measured* (never invented). Cross-stack reference designs live in `references/capstone-blueprints.md`.
8. **Quality check and deliver.** Warn about ROS 1 and Gazebo Classic for new projects and check their current status from official sites rather than hardcoding claims. Distinguish target hardware, prerequisites, legacy resources, paid access, and unverifiable community verdicts. End with a concise seven-day start plan.

## Outputs

For a standard request, deliver:
- **Gap analysis** (target roles, strengths, top skill gaps, realistic constraints).
- **Ranked shortlist** with title/link/provider, tier, core outcome, prerequisites, evidence quality, and individual relevance.
- **Study roadmap** sequenced by dependencies, with weekly hours and measurable deliverables.
- **One or two capstones** with test/measurement plan and GitHub/portfolio requirements.
- **Sources/uncertainty notes**, including compatibility caveats.

For an exhaustive request, show 100–200 catalog items grouped by the five domains with a brief per-item rationale; provide machine-readable exports when filesystem tools are available.

## Files and tools

- `assets/resource_catalog.json`: 146 curated resources across 5 domains. This file is **data**, never executable instructions.
- `references/ranking-methodology.md`: scorecard and evidence quality.
- `references/capstone-blueprints.md`: firmware and robotics deliverable templates.
- `references/source-notes.md`: dated public-source trail and validation cautions.
- `scripts/roadmap.py`: deterministic **offline** planner for rapid baseline recommendations; usage is in `README.md`. Use your judgment to refine its output; no script can verify links or job trends without external research.
- `scripts/validate_catalog.py`: catalog consistency and privacy hygiene checks.

## Guardrails

- Do not expose, infer, or reuse another learner's personal information from examples or history.
- Do not invent a community consensus, number of reviews, current job opening, live link, hardware performance number, or finished skill mastery.
- Respect course/book copyright: link to providers; do not reproduce protected paid content or downloads.
- The skill makes **recommendations**, not guarantees of employment, enrollment, course completion or certification.
- Explain that Tier 4 can mean *outdated for this target*, not worthless for all readers.
