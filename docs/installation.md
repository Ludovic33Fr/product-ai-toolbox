# Installation

Trois manières d'utiliser le starter pack `pm-augmente`.

## 1. Plugin Claude Code (recommandé)

```bash
/plugin marketplace add Ludovic33Fr/product-ai-toolbox
/plugin install pm-augmente@product-ai-toolbox
```

Avantages :
- mise à jour en une commande (`/plugin update pm-augmente`)
- découverte automatique des skills et agents
- isolation propre (pas de fichiers à déplacer manuellement)

## 2. Copie manuelle dans `~/.claude`

```bash
git clone https://github.com/Ludovic33Fr/product-ai-toolbox.git
cd product-ai-toolbox
cp -r skills/* ~/.claude/skills/
cp -r agents/* ~/.claude/agents/
```

Avantages :
- contrôle fin de ce que tu installes (tu peux ne prendre que certains skills)
- facilite le fork pour adapter à ton contexte

Inconvénient : pas de mise à jour automatique. Pour mettre à jour : `git pull` puis `cp -r` à nouveau.

## 3. Adaptation à un autre environnement

Le format des skills et agents (markdown + frontmatter YAML) est utilisable au-delà de Claude Code. Pour Cursor, Continue, ou tout assistant qui consomme des prompts textuels :

- copier le **corps** du `SKILL.md` ou de l'agent comme system prompt ou instruction custom,
- adapter le format de sortie au formalisme attendu par l'environnement cible.

La compatibilité native n'est pas garantie ailleurs que sur Claude Code, et certaines fonctionnalités (auto-discovery via le champ `description`, déclaration `tools`) sont spécifiques.

## Planification des agents

Les agents Claude Code sont stateless : ils ne tournent pas seuls. Pour les routines décrites dans la fiche éditoriale (polling quotidien, note du vendredi 7h), plusieurs options.

### Option A — `/schedule` natif Claude Code

```bash
/schedule daily 09:00 "lance l'agent competitive-watcher"
/schedule weekly fri 07:00 "produis la note hebdo competitive-watcher"
```

Limites : nécessite que Claude Code soit lancé au moment du déclenchement.

### Option B — Cron système

Crée un script wrapper qui invoque Claude Code en mode non-interactif :

```bash
# ~/scripts/competitive-watcher.sh
#!/usr/bin/env bash
claude --skill competitive-watcher --no-interactive >> ~/veille/$(date +%Y-%m-%d).log
```

Puis dans crontab :

```cron
0 7 * * 5 ~/scripts/competitive-watcher.sh
```

### Option C — GitHub Actions cron

Exécution dans un runner GitHub Actions sur planning. Pertinent quand l'agent doit produire des artefacts versionnés (notes archivées dans un repo). Voir un exemple complet dans la documentation de chaque agent concerné.

## Validation locale du pack

Si tu modifies ou contribues, vérifie que tout passe la CI :

```bash
pip install pyyaml jsonschema
python scripts/validate_frontmatter.py
```
