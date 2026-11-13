# Embedded & Robotics Learning Architect

[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-blue)](https://agentskills.io/specification) ![Catalogue](https://img.shields.io/badge/resources-146-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue)

**A reusable AI Agent Skill that creates evidence-aware, personalized study plans for embedded firmware, RTOS, embedded Linux and ROS 2 robotics.**

The skill turns a 146-resource annotated catalogue into a focused curriculum, ranks courses by developer relevance rather than marketing ratings, produces a gap analysis, and designs measurable capstones. The public package includes **no personal resumes, contact details, academic records, or private chat exports**.

## What users can ask

- “I'm a software developer moving into embedded C. Make a 12-week plan with free resources.”
- “I have an STM32 board and FreeRTOS basics. Help me prepare for firmware interviews.”
- “Compare ROS 2 Jazzy tutorials, The Construct, Articulated Robotics, and Nav2 docs.”
- “Make a Linux ↔ MCU robotics portfolio capstone with real test metrics.”
- “Rank all 146 resources for my experience, explicitly mark weak community evidence.”

## Installation

### ChatGPT (where Skills are enabled)

Open **Plugins → Skills → Create → Upload from your computer**, then choose the **skill-only ZIP**. Depending on account/workspace settings, Skills creation and sharing may not be available. ChatGPT Skills availability changes; consult the [official help page](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

### Codex / other Agent Skills-compatible tools

Place this directory in the appropriate skills location, such as `.agents/skills/embedded-robotics-learning-architect/` inside a Git repo (Codex), or the user skill directory documented by your agent. The manifest is `SKILL.md` and follows the [Agent Skills specification](https://agentskills.io/specification).

### GitHub publication

For a public read-only resource explorer, enable GitHub Pages with the repository `docs/` folder as the site source. `docs/index.html` has all catalogue data embedded, so it does not need a backend.

Push this folder as a new public repository or use the **GitHub repository ZIP**. GitHub publication alone does not make it discoverable in ChatGPT's directory. If you intend wider ChatGPT distribution, follow current [plugin/skills publishing instructions](https://learn.chatgpt.com/docs/build-skills) and applicable account eligibility rules.

## Directory map

```
embedded-robotics-learning-architect/
  SKILL.md                         # activation, workflow, output and safety rules
  README.md                        # this document
  LICENSE                          # MIT (original contents only)
  CONTRIBUTING.md                  # contribution and audit policy
  CHANGELOG.md
  assets/
    resource_catalog.json         # 146 resources in machine-readable form
    learner_profile.example.json  # entirely fictional example
    output_example.md             # example deliverable
  references/
    ranking-methodology.md
    capstone-blueprints.md
    source-notes.md
  docs/index.html                  # shareable, static 146-resource catalogue
  scripts/
    roadmap.py                    # offline plan generator (stdlib only)
    validate_catalog.py          # tests catalogue and privacy hygiene
  tests/
    test_skill.py
```

## Optional offline roadmap generator

Requires Python **3.10+**, with no third-party packages:

```bash
python scripts/validate_catalog.py
python scripts/roadmap.py --profile assets/learner_profile.example.json --top 12 --output roadmap.md
python -m unittest discover -s tests -v
```

The script provides a **deterministic baseline selection**, not fresh web research. For current ROS/Gazebo/SDK information, ask a web-enabled agent to verify the recommended resources.

## Ratings and evidence limitations

Tier 1 = core/high return, Tier 2 = strong supplement, Tier 3 = niche/lower priority, Tier 4 = not recommended as **primary** starting material for current target stacks. Evidence codes `D`, `P`, `N`, `X` do **not** mean an endorsement score; see `references/ranking-methodology.md`.

The catalogue was assembled on **November 12, 2026**. Not every one of the 146 links was independently live-tested. Course URLs, costs, SDKs, ROS support, and availability change. Community claims are qualitative and not based on platform stars. This project does not redistribute third-party course or book content.

## License and attribution

MIT covers **original text, cataloguing/annotations, and software in this repository**. Linked publications, courses, software repositories, trademarks and media belong to their respective owners under their own terms. Public references and community source links appear in `references/source-notes.md`.

## Publishing checklist

- [ ] Inspect the catalog's 146 URLs and remove any dead or replaced ones you can identify.
- [ ] Review the real `community_verdict` fields; never turn P/N into endorsements.
- [ ] Run validation, offline roadmap example and unit tests.
- [ ] Check release compatibility for any explicitly named ROS 2/Gazebo versions.
- [ ] Add your desired GitHub profile/maintainer contact (optional; package omits it for privacy).
- [ ] Create a GitHub repo, upload files, tag `v1.0.0`, and publish release notes.
- [ ] For ChatGPT distribution, confirm Skills/plugin publishing eligibility and upload/share through supported UI.
