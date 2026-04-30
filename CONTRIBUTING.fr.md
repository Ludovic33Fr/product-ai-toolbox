# Contribuer à pm-augmente

> *"Si vous tirez bénéfice du dépôt, contribuez. Le partage est la mécanique fondamentale du PM augmenté collectif."* — Annexe 3 du livre.

## Esprit de la contribution

Ce dépôt est un commun éditorial. Il vit des contributions de PM qui ont éprouvé un skill, configuré un agent utile, ou identifié un workflow manquant. La revue mensuelle tranche, intègre, retire — c'est cette mécanique vivante qui fait la valeur du dépôt sur la durée.

## Trois critères d'acceptation

Tous les artefacts (skills et agents), originaux ou contribués, doivent satisfaire les trois critères repris du livre :

### 1. Documentation

- Pour un **skill** : `Objectif`, `Entrées`, `Sorties`, `Cadence d'usage`.
- Pour un **agent** : `Mission`, `Périmètre`, `Déclencheurs`, `Boucle de contrôle`, `Garde-fous`.

Ces champs apparaissent verbatim dans la **fiche éditoriale** au début du fichier. Aucun ne doit être vide ou évasif.

### 2. Versionnement

Le frontmatter porte `version`, `author`, `book`. À chaque modification significative, une ligne est ajoutée à la fin du fichier dans une section `## Historique` :

```markdown
## Historique
- 2026-05-12 — @contributeur — précisions sur la matrice de scoring
- 2026-04-30 — @ludovic — création initiale
```

### 3. Garde-fous

Tout artefact comporte une section `Garde-fous` explicite :

- Ce que l'artefact ne doit **jamais** faire (action sortante, écrasement, etc.)
- Les cas d'usage où il **n'est pas** pertinent
- Les limites de confiance attendues

Les deux premiers critères sont vérifiés automatiquement par la CI. Le troisième relève du jugement éditorial et passe en revue humaine.

## Processus de contribution

1. **Ouvrir une issue d'abord** avec le template `new-skill` ou `new-agent`. Cela évite les PRs orphelins et permet d'écarter les redondances en amont.
2. **Discuter le périmètre** dans l'issue : objectif, entrées, sorties, cadence. Le mainteneur valide ou recadre.
3. **Forker, brancher** (`feat/skill-<nom>` ou `feat/agent-<nom>`), écrire l'artefact en suivant [docs/conventions.md](docs/conventions.md).
4. **Tester localement** : `python scripts/validate_frontmatter.py` doit passer sans erreur.
5. **Ouvrir une PR** liant l'issue, en utilisant le template fourni.

## Revue mensuelle

La **première semaine de chaque mois**, une issue dédiée (label `monthly-review`) liste les PRs ouvertes et les propositions en attente. Le mainteneur (actuellement Ludovic Lefebvre, mainteneur unique en v1) :

- examine les PRs au regard des trois critères
- arbitre les redondances
- valide ou demande des ajustements
- merge ce qui passe
- publie une release `vX.Y.Z` et alimente le `CHANGELOG.md`

À mesure que la communauté grossit (≥3 contributeurs réguliers), cette revue devient collégiale.

## Cycle de vie d'un artefact

| État | Marqueur | Effet |
|------|----------|-------|
| `active` | (par défaut) | Visible dans le catalogue, exécutable |
| `experimental` | `status: experimental` | Visible avec badge "en stabilisation" |
| `deprecated` | `status: deprecated` + `replaced_by: <nom>` | Listé comme déprécié, conservé 2 mois |
| `archived` | déplacé dans `archive/` | Hors catalogue, conservé pour traçabilité |

**Décommissionnement.** Un artefact reste **2 mois** en `deprecated` avant archivage. Pendant cette période, le `replaced_by` indique l'alternative recommandée.

## Conventions de format

Voir [docs/conventions.md](docs/conventions.md) — règles précises sur le frontmatter, les sections obligatoires, le format de sortie, les garde-fous attendus.

## Code de conduite

Contributor Covenant 2.1 — <https://www.contributor-covenant.org/fr/version/2/1/code_of_conduct/>

## Licence

En contribuant, vous acceptez que votre contribution soit publiée sous [licence MIT](LICENSE).
