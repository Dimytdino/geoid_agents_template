# geoid_agents_template — template de projet GéoID

Dépôt **template** (GitHub *template repository*) du pôle GéoID (TSE) : c'est
le point de départ de tout nouveau projet. Il ne contient que le strict
nécessaire à un projet ; le **moteur du socle** (agents, skills, commandes)
n'est pas ici — il arrive par le plugin `geoid` de la marketplace.

> Décision : ADR-003 du socle (« template projet après la bascule en
> plugins », option B). Le dépôt du socle `geoid_socle_plugin` n'est plus un
> template ; il reste le dépôt de développement du socle + la marketplace.

## Comment s'en servir

Voir **`DEMARRER.md`**. En résumé : *Use this template* → cloner → `claude`
(le plugin `geoid` s'installe automatiquement) → `/cadrer-projet`.

## Contenu

| Élément | Rôle |
|---|---|
| `CHARTE.md` | Règles transverses du pôle (couche 1). Copie du master (socle). |
| `CLAUDE.md` | Bootstrap « projet non cadré » ; remplacé par `/cadrer-projet`. |
| `.claude/settings.json` | Permissions projet + **déclaration du plugin `geoid`** (`extraKnownMarketplaces` + `enabledPlugins`, `autoUpdate`) → installation au démarrage, sur toutes surfaces. |
| `templates/` | Gabarits (CLAUDE projet, suivi-projet, fiche-outil, `.mcp.json`, CSS doc). |
| `specialisations/` | Spécialisations du développeur ; la retenue est copiée au cadrage. |
| `DEMARRER.md` | Guide pas à pas. |

## Source de vérité et synchronisation

Le **socle** (`geoid_socle_plugin`) reste la source de vérité du contenu
« résiduel » (CHARTE, `settings.json`, `templates/`, `specialisations/`).
Ce template en est une copie tenue à jour depuis le socle. Le mécanisme de
synchronisation socle → template est suivi en **S-15** (à définir).

Ne pas modifier ici CHARTE / templates / spécialisations : corriger côté
socle, puis répercuter.
