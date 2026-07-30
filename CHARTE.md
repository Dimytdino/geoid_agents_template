# CHARTE GéoID — règles transverses du pôle

Ce fichier est la couche 1 de la bibliothèque d'agents : tout ce qui est vrai
**quel que soit le projet**. Il est complété par le `CLAUDE.md` de chaque
projet (couche 2), généré via la commande `/cadrer-projet`.
En cas de contradiction, la CHARTE prime, sauf dérogation explicitement
actée dans le journal des décisions du projet.

---

## 1. Identité

GéoID est le pôle SIG / identification de TSE (agrivoltaïsme). Ses projets
appartiennent à l'une des quatre familles suivantes :

| Famille | Exemples | Livrables types |
|---|---|---|
| **Étude / analyse SIG** | analyse de secteurs, pré-qualification de parcelles, étude macro | couches, cartes, note de synthèse |
| **Pipeline de données** | workflows FME, scripts Python, traitements PostGIS | scripts versionnés, données publiées, doc de flux |
| **Développement applicatif** | widgets ExB, applis web carto, scripts d'administration ArcGIS | code, appli déployée, doc technique |
| **Pilotage / transverse** | cadrage, reporting, notes de direction | documents, tableaux de bord |

## 2. Langue

- **Prose en français** : commentaires, docstrings, documentation,
  livrables, messages de commit, échanges entre agents.
- **Code en compromis technique/métier** : les identifiants techniques
  suivent l'écosystème en anglais (`load_`, `validate_`, `to_gpkg`) ;
  les termes du domaine restent en français, sans accents (`parcelles`,
  `millesime`, `emprise`, `secteur`). Ne pas traduire le vocabulaire
  métier : il perdrait sa précision.
  Exemple : `def load_parcelles_rpg(millesime: int) -> GeoDataFrame:`
  avec docstring en français.

## 3. Référentiel géographique

> Master/dérivé : la CHARTE est la source de vérité des §3 et §4. Le
> skill `conventions-sig-tse` (diffusé dans claude.ai **et** embarqué par
> le plugin `geoid` sous `plugins/geoid/skills/`) en est une copie
> dérivée : toute modification ici impose de régénérer le skill et de
> re-packager le `.skill` (responsabilité du mainteneur du socle).

- **SRC de stockage et de calcul** : Lambert-93 — **EPSG:2154**.
- **SRC d'affichage web** : Web Mercator — **EPSG:3857**.
- Reprojection toujours **explicite** (2154 → 3857 à l'affichage,
  3857 → 2154 à l'écriture). Ne jamais stocker ni calculer de surface
  en 3857.
- Toujours **déclarer le SRC** ; ne jamais en supposer un par défaut.
- Formats d'échange par défaut : GeoJSON, GeoPackage. Shapefile uniquement
  si exigé par un destinataire.
- **Le SRC d'un format d'échange prime sur le SRC de stockage** pour la
  donnée *produite*. En particulier, **GeoJSON (RFC 7946) impose le
  WGS84 — EPSG:4326** : un export GeoJSON se reprojette explicitement en
  4326, quel que soit le SRC de stockage. Ne jamais déduire le SRC de
  sortie d'un livrable de la règle « stockage = 2154 » : il est dicté par
  le format et le destinataire. GeoPackage et Shapefile, eux, portent le
  SRC qu'on leur écrit (2154 par défaut).

## 4. Sécurité & confidentialité

- **Actions irréversibles** (suppression, écriture en base de production,
  modification de droits, publication de service) : confirmation écrite
  explicite de l'utilisateur, systématiquement.
- **Données foncières** : les coordonnées de parcelles, identités de
  propriétaires et stratégies de secteurs sont confidentielles. Ne jamais
  les recopier dans des exemples, de la documentation partagée ou des
  fichiers destinés à sortir du périmètre TSE.
- Jamais de secret (mot de passe, token, chaîne de connexion) en clair
  dans le code ou la documentation.

## 5. Méthode

- **Règle 0 — réutiliser avant de créer.** Avant toute production, vérifier
  ce qui existe déjà (agents, scripts, couches, conventions, ce fichier).
- **ADR** : toute décision structurante (choix d'outil, de stack, de modèle
  de données, de stratégie) fait l'objet d'un ADR — contexte, options,
  décision, conséquences — instruit par l'`architecte`. Tant qu'un point
  est marqué `🔧 À ARBITRER` dans le CLAUDE.md du projet, aucun agent ne
  produit **sur les tâches qui dépendent de cette décision** (listées
  avec l'ADR). Ce qui n'en dépend pas — analyse, documentation, tests,
  maquette isolée, investigation — avance normalement.
- **Journal des décisions** : chaque décision actée est reportée dans le §
  « Journal des décisions » du CLAUDE.md projet, au format :
  `| AAAA-MM-JJ | sujet | décision | justification |`
- **Revue avant livraison** : tout livrable de production (code, données,
  document final) passe par le `revieweur` avant d'être considéré terminé.
- **Compte rendu de fin de tâche** : tâche / agents mobilisés / livrables /
  décisions actées (reportées au journal) / points en attente.

## 6. Orchestration

La session principale coordonne ; elle ne fait pas le travail spécialisé.
Pour une demande non triviale, expliciter d'abord : analyse de la demande
(1-2 phrases), agents mobilisés et pourquoi, mission précise de chacun.
Si la demande est ambiguë, contradictoire ou hors périmètre : le dire et
poser une question plutôt que deviner.

## 7. Pédagogie

La montée en compétences fait partie des objectifs du pôle.
- Tout agent doit pouvoir **justifier ses choix** si on le lui demande.
- L'agent `mentor` est dédié à l'apprentissage : il explique, il ne fait
  jamais à la place. L'invoquer est encouragé, jamais pénalisant.
