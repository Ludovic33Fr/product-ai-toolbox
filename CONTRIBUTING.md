# Contributing to pm-augmente

Thanks for your interest. This repo accepts community-contributed skills, agents, and editorial improvements.

> French speakers: see [CONTRIBUTING.fr.md](CONTRIBUTING.fr.md) — that file holds the editorial criteria from the book in their original language.

## Acceptance criteria (3, from the book)

Every contribution must satisfy:

1. **Documentation** — required frontmatter fields are present and the body contains all required sections.
   - Skills: `Objectif`, `Entrées`, `Sorties`, `Cadence d'usage`.
   - Agents: `Mission`, `Périmètre`, `Déclencheurs`, `Boucle de contrôle`, `Garde-fous`.
2. **Versioning** — `version`, `author`, `book` fields are filled. Significant updates append to a `## Historique` section at the end of the file (date, contributor, motivation).
3. **Guardrails** — explicit limits, when not to use, what the artefact must never do.

The first two criteria are checked automatically by CI. The third requires human review.

## Workflow

1. **Open an issue first** using the `new-skill` or `new-agent` template. This avoids duplicate work.
2. **Fork** the repo and create a branch (`feat/skill-<name>` or `feat/agent-<name>`).
3. **Write the artefact** following [docs/conventions.md](docs/conventions.md) (FR).
4. **Run the CI locally** if possible:
   ```bash
   python scripts/validate_frontmatter.py
   ```
5. **Open a PR** linking the issue. Use the PR template.

## Quality gates

The CI runs four jobs on every PR:

- **Frontmatter & required sections** — schema validation against `scripts/validate_frontmatter.py`.
- **Markdown lint** — `markdownlint-cli2` against `.markdownlint.json`.
- **Broken links** — `lychee`.
- **Secrets scan** — `gitleaks`. Never commit API keys, tokens, or example credentials.

## Monthly community review

The first week of each month, a tracked issue (`monthly-review`) lists open PRs and proposals. The maintainer (currently Ludovic Lefebvre) reviews them, merges what fits, and ships a new release. As the contributor base grows, this evolves toward a small review committee.

## Removal & deprecation

An artefact may be deprecated when superseded or no longer maintained:

| State | Marker | Effect |
|-------|--------|--------|
| `active` | (default) | Listed in catalogue, executable |
| `experimental` | `status: experimental` | Listed with badge |
| `deprecated` | `status: deprecated` + `replaced_by:` | Listed as deprecated, kept for 2 months |
| `archived` | moved to `archive/` | Out of catalogue, kept for traceability |

Two months in `deprecated` is the floor before archiving.

## Code of conduct

This project follows the [Contributor Covenant 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

## License

By contributing, you agree your contribution is licensed under the [MIT License](LICENSE).
