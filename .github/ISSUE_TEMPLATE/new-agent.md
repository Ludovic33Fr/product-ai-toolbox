---
name: New agent proposal
about: Propose a new agent for the pm-augmente starter pack
title: "[agent] <name>"
labels: ["proposal", "agent"]
---

## Proposed name

`<kebab-case-name>`

## Fiche éditoriale (FR — required)

**Mission.**

**Périmètre.**

**Déclencheurs.**

**Boucle de contrôle.**

**Garde-fous.**

## Why this agent

What recurring routine does it cover? Which book chapter does it relate to?

## Tools required

List the Claude Code tools the agent should be authorized to use (Read, Write, WebFetch, etc.). Justify each.

## Scheduling / persistence

Claude Code subagents are stateless. How will this agent be triggered for its continuous part (cron, /schedule, GitHub Actions)?

## Implementation plan

- [ ] Frontmatter complete
- [ ] Body sections complete (Fiche éditoriale + Mode opératoire + Mise en routine)
- [ ] Output format specified
- [ ] Audit procedure described
- [ ] CI passes locally
