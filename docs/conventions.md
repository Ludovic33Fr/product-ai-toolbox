# Conventions de format

Ce document fixe les règles précises auxquelles tout skill et tout agent du dépôt doit se conformer. La CI les vérifie en partie automatiquement (`scripts/validate_frontmatter.py`).

## Skills

### Localisation

`skills/<nom-en-kebab-case>/SKILL.md` — un dossier par skill, avec un seul fichier `SKILL.md`. Le nom du dossier doit matcher le champ `name` du frontmatter.

### Frontmatter

```yaml
---
name: nom-en-kebab-case
description: Phrase complète en français qui décrit quand activer le skill et ce qu'il produit. Minimum 60 caractères.
version: 0.1.0
author: Nom Prénom
license: MIT
language: fr
book:
  title: Le Product Manager Augmenté
  annex: A3
tags: [domaine, sous-domaine, cadence]
---
```

Champs optionnels :

- `status: experimental | deprecated` — par défaut `active` (omis).
- `replaced_by: <nom>` — obligatoire si `status: deprecated`.
- `contributors: [name1, name2]` — listés à mesure des PRs.

### Corps

Le corps doit contenir, dans l'ordre :

1. Un titre `# <nom-du-skill>`
2. Une section `## Fiche éditoriale` avec les **quatre champs en gras** :
   - `**Objectif.**` — une phrase claire.
   - `**Entrées.**` — ce que le skill consomme.
   - `**Sorties.**` — ce qu'il produit.
   - `**Cadence d'usage.**` — quand il est invoqué.
3. Une section `## Mode opératoire` avec :
   - `### Quand m'invoquer` — phrase de matching pour Claude Code.
   - `### Procédure` — étapes numérotées.
   - `### Format de sortie` — template markdown attendu.
   - `### Garde-fous` — limites explicites en bullet.
   - `### Exemple` — un exemple court (input + output).
4. Une section finale optionnelle `## Historique` listant les modifications.

## Agents

### Localisation

`agents/<nom-en-kebab-case>.md` — fichier plat. Si l'agent a besoin de fichiers de support (templates, listes versionnées), il est promu à un dossier `agents/<nom>/` (à acter en revue mensuelle).

### Frontmatter

Identique au skill, plus le champ optionnel mais recommandé :

```yaml
tools: [Read, Write, WebFetch, WebSearch]
```

Cela limite explicitement les outils Claude Code que l'agent peut invoquer, en cohérence avec ses garde-fous.

### Corps

Le corps doit contenir, dans l'ordre :

1. Un titre `# <nom-de-l-agent>`
2. Une section `## Fiche éditoriale` avec les **cinq champs en gras** :
   - `**Mission.**`
   - `**Périmètre.**`
   - `**Déclencheurs.**`
   - `**Boucle de contrôle.**`
   - `**Garde-fous.**`
3. Une section `## Mode opératoire` avec :
   - `### Quand m'invoquer`
   - `### Configuration attendue` — fichiers, dossiers, paramètres requis avant la première exécution.
   - `### Procédure`
   - `### Format de sortie` — pour la note hebdo et, le cas échéant, pour l'alerte courte.
   - `### Audit` — procédure d'audit human-in-the-loop.
4. Une section `## Mise en routine` — comment planifier l'exécution (cron, `/schedule`, GitHub Actions).
5. `## Historique` optionnel.

## Règles communes

### Description du frontmatter

Le champ `description` est lu par Claude Code pour décider quand activer l'artefact. Il doit donc :

- Commencer par `Utiliser` ou un verbe d'action équivalent.
- Préciser le déclencheur (à quelle demande utilisateur correspond cet artefact).
- Préciser la sortie produite.
- Faire au moins 60 caractères.

### Garde-fous

Toute section `Garde-fous` doit être :

- explicite (pas de "respecter les bonnes pratiques" sans précision),
- non triviale (pas seulement "ne pas écrire dans des fichiers système"),
- honnête sur les limites de confiance (e.g. "ne pas conclure en l'absence de source").

### Format de sortie

Toujours en markdown. Toujours fourni sous forme de **template prêt à copier**, avec des placeholders `{variable}` clairement signalés.

### Exemples

Un exemple suffit ; il doit tenir en moins de 20 lignes ; il doit illustrer une entrée plausible et une sortie qui respecte le template.

### Anonymisation

Tout exemple incluant des données utilisateur, support, ou commerciales doit être anonymisé (pas de nom, pas d'email, pas d'identifiant).

## Validation locale

Avant d'ouvrir une PR :

```bash
pip install pyyaml jsonschema
python scripts/validate_frontmatter.py
```

Le script doit retourner `All skills and agents pass...`. Sinon, la CI bloquera la PR.
