# pm-augmente — La boîte à outils du PM augmenté

> Starter pack de **12 skills + 6 agents** pour [Claude Code](https://claude.com/claude-code), compagnon du livre *Le Product Manager Augmenté* de Ludovic Lefebvre.

[![Licence : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version plugin](https://img.shields.io/badge/plugin-v0.1.0-blue)](.claude-plugin/plugin.json)

Ce dépôt est la version vivante de l'**Annexe 3** du livre. Il contient les douze skills et les six agents décrits dans le livre, prêts à être installés et utilisés. Les contributions de la communauté l'enrichissent en continu.

---

## Installation rapide

### Option 1 — Plugin Claude Code (recommandée)

```bash
/plugin marketplace add Ludovic33Fr/product-ai-toolbox
/plugin install pm-augmente@product-ai-toolbox
```

### Option 2 — Copie manuelle

```bash
cp -r skills/* ~/.claude/skills/
cp -r agents/* ~/.claude/agents/
```

Pour les variantes (Cursor, cron, planification via `/schedule`, GitHub Actions cron), voir [docs/installation.md](docs/installation.md).

---

## Catalogue

Skills et agents sont regroupés ci-dessous par chapitre du livre, pour que la lecture conduise directement à l'usage.

### Discovery (chapitre 5)

| Nom | Type | Objectif |
|-----|------|----------|
| [`discovery-cadrage`](skills/discovery-cadrage/SKILL.md) | skill | Cadrer une discovery utilisateur avec hypothèses multiples et profil cible |
| [`weak-signals-weekly`](skills/weak-signals-weekly/SKILL.md) | skill | Synthèse hebdomadaire de signaux faibles à partir de sources multiples |
| [`weak-signals-watcher`](agents/weak-signals-watcher.md) | agent | Détection continue de signaux faibles utilisateurs |

### Décision (chapitre 6)

| Nom | Type | Objectif |
|-----|------|----------|
| [`committee-prep`](skills/committee-prep/SKILL.md) | skill | Préparer un comité d'arbitrage avec dossier de fond et anticipation d'objections |
| [`devils-advocate`](skills/devils-advocate/SKILL.md) | skill | Faire jouer à l'IA le rôle du sceptique professionnel |
| [`feature-ethics-audit`](skills/feature-ethics-audit/SKILL.md) | skill | Audit éthique d'une feature (manipulation, biais, données) |
| [`decision-journal-keeper`](agents/decision-journal-keeper.md) | agent | Maintenir à jour le journal de décision sans saisie manuelle systématique |

### Spec & qualité (chapitre 7)

| Nom | Type | Objectif |
|-----|------|----------|
| [`spec-from-brief`](skills/spec-from-brief/SKILL.md) | skill | Transformer un brief flou en spec testable et exhaustive |
| [`quality-review-tickets`](skills/quality-review-tickets/SKILL.md) | skill | Pré-revue qualité de tickets de backlog avant refinement |
| [`backlog-triage-agent`](agents/backlog-triage-agent.md) | agent | Pré-trier les tickets entrants pour préparer la décision humaine |

### Pilotage (chapitre 11)

| Nom | Type | Objectif |
|-----|------|----------|
| [`roadmap-variants`](skills/roadmap-variants/SKILL.md) | skill | Simuler trois variantes de roadmap selon hypothèses de capacité et risque |
| [`roadmap-pilot-agent`](agents/roadmap-pilot-agent.md) | agent | Comparer en continu l'avancement effectif vs roadmap prévue |
| [`competitive-watcher`](agents/competitive-watcher.md) | agent | Veille concurrentielle continue et note hebdomadaire de pilotage |

### Communication & alignement (chapitre 8)

| Nom | Type | Objectif |
|-----|------|----------|
| [`multi-stakeholder-comm`](skills/multi-stakeholder-comm/SKILL.md) | skill | Décliner un sujet en versions calibrées par stakeholder |
| [`stakeholder-digest-agent`](agents/stakeholder-digest-agent.md) | agent | Encarts hebdomadaires personnalisés par stakeholder, prêts à relire |

### Management de PM (chapitre 13)

| Nom | Type | Objectif |
|-----|------|----------|
| [`onboarding-pm`](skills/onboarding-pm/SKILL.md) | skill | Parcours d'onboarding pour un nouveau PM rejoignant l'équipe |
| [`quarterly-review-pm`](skills/quarterly-review-pm/SKILL.md) | skill | Revue trimestrielle d'un PM sur base factuelle + grille de maturité IA |

### Mesure d'impact (chapitre 14)

| Nom | Type | Objectif |
|-----|------|----------|
| [`four-indicators-measure`](skills/four-indicators-measure/SKILL.md) | skill | Calculer les quatre indicateurs du PM augmenté |

Mapping détaillé chapitre par chapitre : [docs/livre.md](docs/livre.md).

---

## Le livre

> **Le Product Manager Augmenté — Décider mieux, plus vite, avec l'IA**
> Ludovic Lefebvre, 2026.

Page de présentation Amazon (lien ajouté à la publication).

---

## Contribuer

Le dépôt est ouvert. Trois critères d'acceptation, repris du livre :

1. **Documentation** — pour un skill : objectif, entrées, sorties, cadence d'usage. Pour un agent : mission, périmètre, déclencheurs, boucle de contrôle, garde-fous.
2. **Versionnement** — auteur, date, motivation.
3. **Garde-fous** — limites explicites, cas d'usage où l'artefact n'est pas pertinent.

Une revue mensuelle (première semaine du mois) tranche les contributions, intègre les améliorations, retire les artefacts devenus obsolètes.

Détails complets : [CONTRIBUTING.fr.md](CONTRIBUTING.fr.md).

---

## Licence

[MIT](LICENSE) © 2026 Ludovic Lefebvre.
