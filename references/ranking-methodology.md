# Resource Ranking and Evidence Discipline

**Catalog snapshot:** 2026-11-12. The 146-resource inventory was compiled from public sources and reviewed at category/top-resource level; it is not independently live-tested link-by-link. Scores are qualitative.

## Domains

A: Embedded & Bare-Metal Firmware · B: RTOS & Embedded Linux · C: C/C++ & Software Architecture · D: ROS 2 & Robotics · E: Books & Reference Manuals.

## Tiers

- **Tier 1:** Highest return for target track; core course, project sequence, or foundational reference.
- **Tier 2:** Strong supplement; narrow specialized work or worthwhile next step.
- **Tier 3:** Niche, intermediate reference, redundant for current learner, or low urgency.
- **Tier 4:** Poor **primary** choice for a modern stack due to age, mismatch, or shallow depth; may retain historical value.

## Candidate evaluation rubric (0–5 per factor)

| Factor | Default weight | Assess |
|---|---:|---|
| Fit for desired role and current gaps | 35% | Jobs, prerequisites, evidence of projects |
| Depth and technical correctness | 25% | Registers/ISRs, kernel mechanisms, design rationale, ROS 2 internals |
| Hands-on and measurable transfer | 15% | Hardware tests, code, CI, bug reports, reproduction |
| Version/maintenance/access compatibility | 15% | Distro release, code freshness, prerequisites, cost |
| Community evidence strength and quality | 10% | Actual practitioner discussions, limitations, not stars |

A score of 0–5 in each factor can be multiplied by weights and summed. **There are no objective per-resource scores in the bundled dataset.** Do not convert the historical tier or rank into a measured probability of employment.

## Evidence codes in resource_catalog.json

- **D:** A specific source or title was discussed or recommended directly on a public practitioner forum. Not necessarily representative consensus. Revisit links/dates.
- **P:** Primary publisher/vendor documentation supports curriculum; independent practitioner consensus not established.
- **N:** Limited independently confirmed community assessment for the specific resource.
- **X:** Material age, EOL, version mismatch, or fit drawback supported by technical/community evidence.

The catalogue's `community_verdict` includes its original qualitative context; when presenting, label each verdict with the correct code. Do **not** claim endorsements for entries marked P/N.

## Personalization rules

Use explicit learner evidence: code they implemented, bug they debugged, board they own, ROS nodes they wrote, and deployed/tested systems. Separate familiarity from production-quality mastery. Penalize resources duplicating current skill. Favor measurable project deliverables over course completion certificates. Prefer official manuals for exact MCU/SDK versions. Re-evaluate the ranking when the user targets ASIC verification, machine vision, electronics design, or different roles.

## Live verification checklist

1. Open official resource page; confirm course or repository still exists, language, platform, requirements and whether pricing is known.
2. Verify version pairing from current official ROS/Gazebo release docs; avoid old installation instructions.
3. If an item makes a community claim, find a direct discussion of that title, link it, and state sample size and date when known.
4. Distinguish a historical job-market snapshot from open positions.
5. Record `checked_on` and notes if publishing a refreshed catalogue.
