# geoid_agents_template — template de projet GéoID

Dépôt **template** (GitHub *template repository*) du pôle GéoID (TSE) : c'est
le point de départ de tout nouveau projet. Il ne contient que le strict
nécessaire à un projet ; le **moteur du socle** (agents, skills, commandes)
n'est pas ici — il arrive par le plugin `geoid` de la marketplace.

> Décision : ADR-003 du socle (« template projet après la bascule en
> plugins », option B). Le dépôt du socle `geoid_socle_plugin` n'est plus un
> template ; il reste le dépôt de développement du socle + la marketplace.

## Comment s'en servir

Voir **`DEMARRER.md`**. En résumé : *Use this template* → cloner →
installer le plugin une fois par poste
(`claude plugin install geoid@geoid-socle --scope user`) → `claude` →
`/geoid:cadrer-projet` (les commandes de plugin sont préfixées par le nom du
plugin).

⚠️ La déclaration du plugin dans `.claude/settings.json` **active** `geoid`
pour ce dépôt, elle ne l'**installe** pas : sans l'installation ci-dessus, la
session peut démarrer sans aucune commande `/geoid:…` ni agent. Contrôle :
`claude plugin list` (voir `DEMARRER.md`, étape 2).

## Contenu

| Élément | Rôle |
|---|---|
| `CHARTE.md` | Règles transverses du pôle (couche 1). Copie du master (socle). |
| `CLAUDE.md` | Bootstrap « projet non cadré » ; remplacé par `/geoid:cadrer-projet`. |
| `.claude/settings.json` | Permissions projet + **déclaration du plugin `geoid`** : `extraKnownMarketplaces` (enregistre la marketplace `geoid-socle`, `autoUpdate`) + `enabledPlugins` (active `geoid` dans ce dépôt). L'installation de la copie du plugin reste un geste explicite, une fois par poste. |
| `templates/` | Gabarits (CLAUDE projet, suivi-projet, fiche-outil, `.mcp.json`, CSS doc). |
| `specialisations/` | Spécialisations du développeur ; la retenue est copiée au cadrage. |
| `DEMARRER.md` | Guide pas à pas. |

## Source de vérité et synchronisation

Le **socle** (`geoid_socle_plugin`) reste la source de vérité du contenu
« résiduel » (CHARTE, `templates/`, `specialisations/`). Ce template en est
une copie tenue à jour depuis le socle par `scripts/sync_template.py`
(`--check` détecte la dérive, `--apply` recopie), joué au moment d'une
release — sens unidirectionnel : le socle fait foi.

Le `.claude/settings.json` est **hors** de cette synchronisation : celui d'ici
est propre au projet (permissions + déclaration du plugin) et diffère de celui
du socle. Un durcissement des permissions destiné aux projets se porte donc à
la main sur ce fichier (ADR-003).

Ne pas modifier ici CHARTE / templates / spécialisations : corriger côté
socle, puis répercuter.
