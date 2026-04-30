# Mapping skills et agents avec les chapitres du livre

Chaque artefact prolonge un chapitre précis du livre *Le Product Manager Augmenté*. Cette table est le fil conducteur entre la lecture et l'usage.

| Chapitre | Sujet | Skills | Agents |
|----------|-------|--------|--------|
| 5 — Discovery augmentée | Cadrage de discovery, observation utilisateur | `discovery-cadrage`, `weak-signals-weekly` | `weak-signals-watcher` |
| 6 — Décider mieux | Arbitrage, esprit critique, éthique de la décision | `committee-prep`, `devils-advocate`, `feature-ethics-audit` | `decision-journal-keeper` |
| 7 — Spécifier et écrire | Transformation brief → spec, qualité tickets | `spec-from-brief`, `quality-review-tickets` | `backlog-triage-agent` |
| 8 — Aligner et communiquer | Communication multi-stakeholder | `multi-stakeholder-comm` | `stakeholder-digest-agent` |
| 11 — PM orchestrateur | Pilotage en continu, veille | `roadmap-variants` | `competitive-watcher`, `roadmap-pilot-agent` |
| 13 — Manager une équipe augmentée | Onboarding, revue de PM | `onboarding-pm`, `quarterly-review-pm` | — |
| 14 — Mesurer l'impact réel | Indicateurs du PM augmenté | `four-indicators-measure` | — |

## Comment lire ce mapping

- Un skill ou un agent peut prolonger plusieurs chapitres ; on indique le **chapitre principal**, celui qui pose le concept.
- Le frontmatter de chaque fichier porte `book.annex: A3` (l'annexe d'origine), pas le numéro de chapitre. Cette table est la source de vérité côté chapitre.
- Quand un nouveau skill ou agent est contribué, sa première PR met cette table à jour.

## Lecture chapitre par chapitre

### Chapitre 5 — Discovery augmentée

La discovery est le terrain où l'IA fait gagner le plus de temps sans diluer la responsabilité du PM. Les trois artefacts du chapitre couvrent : **cadrer** une investigation (`discovery-cadrage`), **synthétiser** les signaux récurrents (`weak-signals-weekly`), **observer** en continu (`weak-signals-watcher`).

### Chapitre 6 — Décider mieux

Le chapitre le plus dense en artefacts : **préparer** un arbitrage avec contradictions (`committee-prep`), **stress-tester** une proposition (`devils-advocate`), **auditer** ses biais éthiques (`feature-ethics-audit`), **historiser** les décisions pour la justesse rétrospective (`decision-journal-keeper`).

### Chapitre 7 — Spécifier et écrire

Du flou à la rigueur : **transformer** un brief (`spec-from-brief`), **pré-réviser** un ticket (`quality-review-tickets`), **trier** le flux entrant (`backlog-triage-agent`).

### Chapitre 8 — Aligner et communiquer

Le travail d'alignement consomme un temps disproportionné dans la semaine du PM. Deux artefacts pour le compresser sans perdre la nuance : **décliner** un sujet par stakeholder (`multi-stakeholder-comm`), **produire** un digest hebdo personnalisé (`stakeholder-digest-agent`).

### Chapitre 11 — PM orchestrateur

C'est ici que la posture orchestrateur se concrétise. Trois agents tournent en routine (veille concurrentielle, pilotage roadmap), un skill couvre la simulation de variantes (`roadmap-variants`).

### Chapitre 13 — Manager une équipe augmentée

Onboarding accéléré (`onboarding-pm`) et revue trimestrielle factualisée (`quarterly-review-pm`).

### Chapitre 14 — Mesurer l'impact réel

Un seul skill calcule les **quatre indicateurs** du PM augmenté (`four-indicators-measure`). Cohérent : la mesure n'est pas un workflow continu, c'est un rite trimestriel.

## Ce qui n'est pas dans le starter pack

L'Annexe 3 cadre douze skills et six agents. Le livre cite d'autres patterns (chapitre 4 : journée type ; chapitre 10 : workflows et prompts ; chapitre 17 : plan 90 jours) qui ne sont pas implémentés ici parce qu'ils ne se prêtent pas au format "skill ponctuel" ou "agent persistant". Ils relèvent plutôt de la **bibliothèque de prompts** (Annexe 1).

Si tu identifies un workflow récurrent qui mériterait d'être un skill et qui n'apparaît pas ci-dessus, ouvre une issue avec le template `new-skill`.
