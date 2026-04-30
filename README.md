# pm-augmente — Augmented Product Manager Toolbox

> Starter pack of **12 skills + 6 agents** for [Claude Code](https://claude.com/claude-code), companion to the book *Le Product Manager Augmenté* by Ludovic Lefebvre.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Plugin version](https://img.shields.io/badge/plugin-v0.1.0-blue)](.claude-plugin/plugin.json)
[![Content: French](https://img.shields.io/badge/content-français-orange)](README.fr.md)

> **Heads-up.** Skill and agent bodies, prompts and produced outputs are in **French**. The repository envelope (this README, contribution rules, frontmatter keys) is in English to maximize international discoverability. French speakers should start with [README.fr.md](README.fr.md).

---

## Install

### Option 1 — As a Claude Code plugin (recommended)

```bash
/plugin marketplace add Ludovic33Fr/product-ai-toolbox
/plugin install pm-augmente@product-ai-toolbox
```

### Option 2 — Manual copy

Copy the folders directly into your Claude Code config:

```bash
cp -r skills/* ~/.claude/skills/
cp -r agents/* ~/.claude/agents/
```

See [docs/installation.md](docs/installation.md) (FR) for variants (Cursor, cron, scheduled invocations).

---

## What's inside

### Skills (12)

| Name | One-line gloss (EN) |
|------|---------------------|
| `weak-signals-weekly` | Weekly weak-signals synthesis from verbatims, support, mentions, logs |
| `quality-review-tickets` | Pre-refinement quality review of backlog tickets (INVEST + edge cases) |
| `discovery-cadrage` | Frame a user discovery with hypotheses, target profile, interview guide |
| `committee-prep` | Prepare an arbitration committee with anticipated objections and decision criteria |
| `spec-from-brief` | Turn a fuzzy brief into a testable, exhaustive specification |
| `roadmap-variants` | Simulate three roadmap variants (cautious / balanced / aggressive) |
| `multi-stakeholder-comm` | Tailor one topic into stakeholder-specific one-pagers |
| `onboarding-pm` | Build the onboarding path for a new PM joining the team |
| `devils-advocate` | Have the AI play professional skeptic to demolish a proposal |
| `feature-ethics-audit` | Audit a planned feature for ethical risks (manipulation, bias, data) |
| `quarterly-review-pm` | Quarterly PM review based on factual deliveries and AI maturity grid |
| `four-indicators-measure` | Compute the four augmented-PM indicators |

### Agents (6)

| Name | One-line gloss (EN) |
|------|---------------------|
| `competitive-watcher` | Continuous competitive watch + weekly 5-minute briefing note |
| `backlog-triage-agent` | Pre-classify incoming tickets to prepare human decision |
| `roadmap-pilot-agent` | Compare roadmap progress vs plan, weekly steering note |
| `weak-signals-watcher` | Continuously detect weak user signals, feed the discovery journal |
| `decision-journal-keeper` | Keep the PM decision journal up to date without manual capture |
| `stakeholder-digest-agent` | Weekly per-stakeholder one-pager drafts, ready for human review |

Detailed mapping with the book chapters: [docs/livre.md](docs/livre.md) (FR).

---

## The book

This repository is the public companion of:

> **Le Product Manager Augmenté — Décider mieux, plus vite, avec l'IA**
> Ludovic Lefebvre, 2026.

The book introduces the augmented PM model, refounds operational gestures (discovery, decision, specification, alignment), and provides a 90-day transformation plan. This repo turns Annex 3 into executable artefacts.

Book landing page (link added at publication).

---

## Contributing

We welcome new skills, agents, and improvements. See [CONTRIBUTING.md](CONTRIBUTING.md) (EN) or [CONTRIBUTING.fr.md](CONTRIBUTING.fr.md) (FR — editorial criteria from the book).

Three acceptance criteria, lifted from the book:

1. **Documentation** — required fields complete (4 for skills, 5 for agents).
2. **Versioning** — author, date, motivation in the frontmatter.
3. **Guardrails** — explicit limits, when not to use.

A monthly community review merges contributions, retires obsolete artefacts, and ships a new release.

---

## License

[MIT](LICENSE) © 2026 Ludovic Lefebvre.
