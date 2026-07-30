# DÉMARRER — initialiser un projet GéoID pas à pas

Ce guide explique comment créer et démarrer un projet à partir du template
`geoid_agents_template`. Du poste vide au premier livrable. Garde-le ouvert
à côté de toi la première fois.

> En une ligne : **template → `claude` (le plugin `geoid` s'installe seul) →
> `/cadrer-projet` → trancher les ADR → produire → revue avant de livrer.**

---

## Étape 0 — Prérequis (une seule fois par poste)

- Un terminal avec **Node.js** installé.
- **Claude Code** : `npm install -g @anthropic-ai/claude-code`, puis
  `claude` une première fois pour se connecter avec le compte Claude TSE.
- Accès aux dépôts du pôle sur GitHub — le template
  **TSE-Pole-Geomatique/geoid_agents_template** (pour créer un projet) et le
  socle **geoid_socle_plugin** (d'où provient le plugin `geoid`, servi par la
  marketplace).
- **Sous Windows** : travailler dans **WSL**, et garder les dépôts dans le
  home WSL (`~/...`), jamais dans `/mnt/c/...` (plus lent, problèmes de
  permissions).

Vérifier que tout est prêt :
```bash
node --version      # doit répondre une version
claude --version    # doit répondre une version
```

---

## Étape 1 — Créer le dépôt du projet depuis le template

Sur **GitHub** :
1. Ouvrir le dépôt `geoid_agents_template`.
2. Bouton **Use this template** → *Create a new repository*.
3. Nommer le projet en minuscules-tirets (ex. `pipeline-rpg`,
   `widget-export-geojson`, `orion-poc`).
4. Owner = l'organisation **TSE-Pole-Geomatique**, visibilité **Private**.
5. *Create repository*.

Puis cloner en local (dans WSL) :
```bash
cd ~
git clone https://github.com/TSE-Pole-Geomatique/<mon-projet>.git
cd <mon-projet>
```

---

## Étape 2 — Lancer Claude Code et cadrer le projet

```bash
claude
```
Au premier lancement dans le dossier, accepter de faire confiance au dépôt.

Le plugin d'équipe `geoid` (agents, skills, commandes) est **déjà déclaré**
dans `.claude/settings.json` : il **s'installe automatiquement au démarrage**,
sans aucune commande à taper (et se met à jour tout seul). Au besoin, vérifier
avec `/plugin` que `geoid` est actif.

> Cela fonctionne sur toutes les surfaces (terminal, appli desktop, WSL,
> sessions cloud). L'installation manuelle par `/plugin marketplace add` +
> `/plugin install` reste possible là où la commande `/plugin` est disponible,
> mais elle n'est plus nécessaire.

Puis lancer le cadrage :
```
/cadrer-projet
```

L'entretien guidé couvre, par petits groupes de questions :
- **identité** (nom, famille, commanditaire) ;
- **objectif** et critères de réussite ;
- **données** (sources, millésimes, sensibilité — foncier = confidentiel) ;
- **livrables** ;
- **environnement technique avec les versions exactes** (« à vérifier »
  plutôt que deviner) ;
- **existant à réutiliser** (règle 0) ;
- **décisions actées vs à arbitrer** (chaque point ouvert → un ADR) ;
- **équipe humaine et niveaux** (le mentor s'en sert pour calibrer).

À la fin : le `CLAUDE.md` du projet et `docs/suivi-projet.md` sont
générés. Les agents viennent du plugin `geoid` (déjà installé) ; le
cadrage inscrit la composition retenue au **§5 normatif** du CLAUDE.md —
l'orchestrateur ne délègue qu'à ces agents — et copie la seule
spécialisation du développeur retenue dans `.claude/agents/` du projet.
**Quitter puis relancer `claude`** : le nouveau CLAUDE.md et la
spécialisation ne sont chargés qu'au démarrage d'une session.

> Familles et agents typiques :
> - **étude / analyse SIG** → analyste_sig, revieweur, documentaliste, mentor
> - **pipeline de données** → architecte, developpeur_etl, revieweur, documentaliste, mentor
> - **développement applicatif** → architecte, developpeur_back_geo / front_carto, revieweur, documentaliste, chef_projet, mentor
> - **pilotage / transverse** → chef_projet, documentaliste, mentor

---

## Étape 3 — Faire trancher les décisions ouvertes (ADR)

Tant qu'un point est marqué `🔧 À ARBITRER` dans le `CLAUDE.md`, les
tâches qui **dépendent de cette décision** sont bloquées — le reste
(analyses, doc, tests, maquettes) avance. L'architecte instruit, **c'est
toi qui tranches**, et la décision est actée au journal.
```
Utilise le sous-agent architecte pour instruire ADR-001 et ADR-002.
```

---

## Étape 4 — Produire

Délègue le travail substantiel aux agents. Les actions sensibles
(base de données, `git push`, réseau) demanderont ta confirmation ; les
actions irréversibles exigent ton accord écrit explicite.
```
Implémente [la tâche], conformément aux ADR actés.
```

---

## Étape 5 — Comprendre en route (réflexe à prendre)

Dès qu'une notion n'est pas claire, le mentor est là — il explique sur le
code réel du projet, et ne fait jamais à ta place. Personne ne juge.
```
Utilise le sous-agent mentor pour m'expliquer [ce fichier / cette erreur /
ce concept] — je débute sur [sujet].
```

---

## Étape 6 — Revue, puis livraison

Tout livrable **final** passe par le revieweur, puis par toi. Les
corrections retournent à l'agent qui a produit, jamais au revieweur.
```
Fais passer [le livrable] en revue par le revieweur.
```
Après ta validation :
```bash
git add . && git commit -m "..."   # message en français, décrit le pourquoi
git push                           # demande confirmation
```

---

## Étape 7 — Clôturer la session

En fin de séance utile, mettre à jour le suivi du projet :
```
/cloturer-session
```
Le chef de projet (ou l'orchestrateur) met à jour la roadmap et les
risques (`docs/suivi-projet.md`) et le journal des décisions
(`CLAUDE.md`), **après ta validation**. À lancer volontairement, pas à
chaque micro-session.

---

## En cas de mise à jour du socle

Le socle se met à jour par **deux canaux** :

- **Agents, skills et commandes** (plugin `geoid`) — par la marketplace,
  **automatiquement** (`autoUpdate` déclaré dans `.claude/settings.json`).
  Rien à faire ; au besoin, forcer avec :
  ```
  /plugin marketplace update geoid-socle
  ```
- **CHARTE, permissions, gabarits, spécialisations** (template résiduel) —
  par merge git depuis le **dépôt template**, une fois par projet ajouter la
  source :
  ```bash
  git remote add template https://github.com/TSE-Pole-Geomatique/geoid_agents_template.git
  ```
  puis à chaque évolution :
  ```bash
  git fetch template && git merge template/main
  ```
  Résoudre les éventuels conflits sur le `CLAUDE.md` (il est propre au
  projet).

---

## Mémo des commandes

| Commande | Quand |
|----------|-------|
| `geoid:cadrer-projet` | au démarrage d'un projet |
| `geoid:cloturer-session` | en fin de séance utile |

## Les règles d'or (rappel)

1. **Confidentialité** : jamais de coordonnées de parcelles, d'identités
   ou de stratégies de secteurs dans ce qui sort de TSE.
2. **Validation humaine** : toute action irréversible exige ton accord.
3. **Revue avant livraison** : aucun livrable final sans le revieweur.
4. **Esprit critique** : un agent affirme avec aplomb même quand il se
   trompe — vérifie ce qui compte.
5. **Le mentor d'abord** : comprends avant de copier-coller.
