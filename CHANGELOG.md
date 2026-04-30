# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] — 2026-05-01

CI hardening release. No content change to skills or agents.

### Fixed

- Drop deprecated `--exclude-mail` flag in `lychee-action` step (lychee 0.24+
  removed it; mailto URLs are excluded by default).
- Relax `markdownlint` rules that fired on intentional content (MD025, MD031,
  MD040, MD060). MD022 is kept and the offending blank-lines were fixed in
  the six agent files.
- Correct broken Contributor Covenant FR URL (`code_de_conduite` →
  `code_of_conduct`) and wrap as autolink.
- Fix list-spacing issues in `CONTRIBUTING.fr.md`, `docs/installation.md`,
  and `agents/decision-journal-keeper.md`.

### Notes

- All four CI jobs (frontmatter validation, markdown lint, broken links,
  gitleaks) now pass on `main`.
- Lychee verified 86 links across the repo, 0 errors.

## [0.1.0] — 2026-04-30

First release. Companion to the book *Le Product Manager Augmenté* by Ludovic Lefebvre.

### Added — repository scaffolding

- MIT license, bilingual READMEs (EN envelope + FR for book readers).
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (single-plugin marketplace pattern).
- Bilingual `CONTRIBUTING` (EN technical workflow + FR editorial criteria from the book).
- GitHub Actions CI: frontmatter validation, markdown lint, broken-link check, secrets scan (gitleaks).
- Issue templates (`new-skill`, `new-agent`, `bug`) and PR template aligned on the three acceptance criteria.
- `scripts/validate_frontmatter.py` — JSON-Schema validation of skills and agents plus required body section checks.
- Documentation: `docs/conventions.md`, `docs/installation.md`, `docs/livre.md` (chapter mapping).

### Added — skills (12)

| Skill | Book chapter |
|-------|--------------|
| `weak-signals-weekly` | 5 — Discovery |
| `discovery-cadrage` | 5 — Discovery |
| `committee-prep` | 6 — Décider mieux |
| `devils-advocate` | 6 — Décider mieux |
| `feature-ethics-audit` | 6 / 16 — Éthique |
| `spec-from-brief` | 7 — Spécifier |
| `quality-review-tickets` | 7 — Spécifier |
| `roadmap-variants` | 11 — Pilotage |
| `multi-stakeholder-comm` | 8 — Aligner |
| `onboarding-pm` | 13 — Manager |
| `quarterly-review-pm` | 13 — Manager |
| `four-indicators-measure` | 14 — Mesurer |

### Added — agents (6)

| Agent | Book chapter |
|-------|--------------|
| `weak-signals-watcher` | 5 — Discovery |
| `decision-journal-keeper` | 6 — Décider mieux |
| `backlog-triage-agent` | 7 — Spécifier |
| `competitive-watcher` | 11 — Pilotage |
| `roadmap-pilot-agent` | 11 — Pilotage |
| `stakeholder-digest-agent` | 8 — Aligner |

### Notes

- All artefacts respect a two-tier structure: editorial card (verbatim from the book's Annex 3) + operating mode.
- All agents include a "Mise en routine" section honestly explaining that Claude Code subagents are stateless — scheduling recipes are listed in `docs/installation.md`.
- License: MIT. Content language: French. Envelope language: English.
