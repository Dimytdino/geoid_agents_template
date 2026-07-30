<!-- ============================================================================
COMMENT UTILISER CE TEMPLATE
------------------------------------------------------------------------------
Ce fichier est le squelette d'une fiche de documentation d'outil GeoID.
Il documente indifferemment un workflow FME, un script Python ou un modele QGIS.

1. Copier ce fichier sous un nom parlant, ex. : doc-mon-outil.md
2. Remplir chaque marqueur [A completer : ...] ; supprimer les marqueurs traites.
3. Adapter les blocs VARIANTE selon le type d'outil :
     - workflow FME  -> garder les blocs « VARIANTE FME » ;
     - script Python -> supprimer les blocs « VARIANTE FME » ;
     - modele QGIS   -> supprimer les blocs « VARIANTE FME », adapter au besoin.
   Chaque bloc variante est borne par deux commentaires HTML
   (<!-- VARIANTE FME : debut --> ... <!-- VARIANTE FME : fin -->) :
   supprimer tout ce qui est entre les deux, commentaires compris.
4. A l'endroit du diagramme, conserver le marqueur <!-- WORKFLOW_DIAGRAM -->.
   Fournir un fichier .svg au script via --diagram, sinon le marqueur est
   retire proprement (aucun diagramme affiche).
5. Generer le HTML autoportant :
     python3 scripts/generer_doc_html.py \
         --source doc-mon-outil.md \
         --output doc-mon-outil.html \
         --diagram schema.svg          # optionnel

ANCRES / TABLE DES MATIERES
------------------------------------------------------------------------------
NE PAS ecrire de table des matieres manuelle : la nav laterale est generee
automatiquement a partir des titres (## et ###). Si vous tenez a ajouter des
liens internes manuels, sachez que la bibliotheque « markdown » DESACCENTUE
les identifiants : un titre « ## 2. Logique / algorithme » donne l'ancre
« #2-logique-algorithme » (sans accent). Utiliser des slugs SANS ACCENT,
sinon le lien ne resoudra pas (bug rencontre sur le pilote covisibilite).
============================================================================ -->

# [À compléter : nom lisible de l'outil]

**Fichier source :** `[À compléter : nom du fichier, ex. mon_workflow.fmw]`
**Version :** [À compléter : ex. FME 2025.2 / Python 3.13 / QGIS 3.34]
**Date de rédaction :** [À compléter : AAAA-MM-JJ]
**Auteur de la documentation :** [À compléter]

---

## Fiche d'identité

> Bloc normalisé décrivant l'outil. Format stable et autosuffisant, destiné à
> être moissonné par le futur catalogue des outils GéoID. À mettre à jour à
> chaque évolution majeure de l'outil ou de la documentation.

| Champ | Valeur |
|-------|--------|
| **Nom de l'outil** | [À compléter : nom fonctionnel] |
| **Type d'outil** | [À compléter : Workflow FME / Script Python / Modèle QGIS] |
| **Fichier source / version** | [À compléter : nom du fichier — version] |
| **Auteur d'origine** | [À compléter] |
| **Mainteneur actuel** | [À compléter] |
| **Emplacement de la source faisant autorité** | [À compléter : dépôt / chemin de la version de référence] |
| **Statut** | [À compléter : production / staging / brouillon] |
| **Date de dernière revue** | [À compléter : AAAA-MM-JJ] |

---

## 1. Vue d'ensemble

### Objectif

[À compléter : que fait l'outil, à quel besoin métier il répond, en quelques phrases.]

### Entrées et sorties — vue synthétique

| Entrée | Sortie |
|--------|--------|
| [À compléter] | [À compléter] |

### Périmètre fonctionnel

[À compléter : ce que l'outil couvre et ce qu'il ne couvre pas ; mode et fréquence d'exécution.]

---

## 2. Logique / algorithme

### Principe général

[À compléter : la logique de traitement, le raisonnement métier qui sous-tend le calcul.]

### Schéma d'enchaînement

<!-- WORKFLOW_DIAGRAM -->

[À compléter : description textuelle des étapes, qui accompagne le diagramme.
Cette description doit rester compréhensible même sans le schéma.]

---

## 3. Prérequis et environnement

### Logiciels

| Composant | Version requise | Notes |
|-----------|----------------|-------|
| [À compléter] | [À compléter] | [À compléter] |

### Accès aux données / au réseau

[À compléter : connexions base de données, services web, fichiers attendus, accès réseau requis.
Ne JAMAIS consigner ici d'identifiant, de mot de passe ou de donnée foncière.]

### SRC

[À compléter : système de référence de coordonnées de travail, ex. Lambert-93 (EPSG:2154).]

### Procédure d'installation pas à pas (de zéro au premier lancement réussi)

> Cette sous-partie est l'objectif explicite du modèle : permettre à un tiers
> de partir d'un poste vierge et d'aboutir à une première exécution réussie,
> sans assistance. La rédiger comme une recette, étape par étape.

1. [À compléter : installer le logiciel et sa version, ex. FME 2025.2 / Python 3.13.]
2. [À compléter : récupérer la source faisant autorité (cf. fiche d'identité).]
3. [À compléter : installer les dépendances — cf. section 6.]
4. [À compléter : configurer les connexions / accès — sans secret en clair.]
5. [À compléter : vérifier les prérequis réseau.]
6. [À compléter : lancer l'outil avec un jeu d'entrée d'exemple.]
7. [À compléter : vérifier que les sorties attendues sont produites.]

---

## 4. Entrées / paramètres d'entrée

[À compléter : tableau des paramètres et données en entrée.]

| Nom | Type | Valeur par défaut | Obligatoire | Description |
|-----|------|-------------------|-------------|-------------|
| [À compléter] | [À compléter] | [À compléter] | [À compléter] | [À compléter] |

---

## 5. Sorties / paramètres de sortie

[À compléter : tableau des livrables produits — format, nom, contenu, emplacement.]

| Livrable | Format | Nom / emplacement | Contenu |
|----------|--------|-------------------|---------|
| [À compléter] | [À compléter] | [À compléter] | [À compléter] |

<!-- VARIANTE FME : debut — Transformers cles ============================== -->
<!-- Bloc reserve aux workflows FME. SUPPRIMER ce bloc (commentaires inclus)
     pour un script Python ou un modele QGIS. -->

## Transformers clés

[À compléter : transformers principaux dans l'ordre du flux, avec leur rôle.
Omettre les transformers utilitaires. Signaler les transformers DÉSACTIVÉS
et la raison de ne pas les réactiver sans vérification.]

| Transformer | Rôle |
|-------------|------|
| [À compléter] | [À compléter] |

<!-- VARIANTE FME : fin — Transformers cles ================================= -->

## 6. Code et dépendances

> Convention GéoID : ne PAS documenter le code ligne à ligne. Documenter les
> bibliothèques utilisées et leurs versions, ainsi que les points d'attention.

### Dépendances

| Bibliothèque / composant | Rôle | Statut | Version |
|--------------------------|------|--------|---------|
| [À compléter] | [À compléter] | [À compléter : Obligatoire / Optionnelle / À valider] | [À compléter] |

### Points d'attention sur le code

[À compléter : paramètres codés en dur, logs de debug résiduels, etc.]

<!-- VARIANTE FME : debut — Deploiement FME Server / FME Flow ============== -->
<!-- Bloc reserve aux workflows FME. SUPPRIMER ce bloc (commentaires inclus)
     pour un script Python ou un modele QGIS. -->

## Déploiement FME Server / FME Flow

[À compléter : procédure de publication, paramètres exposés, connexions à
recréer sur le serveur, persistance des sorties, disponibilité des
bibliothèques Python côté serveur. Signaler les écarts de comportement
poste Windows vs FME Server / Flow.]

<!-- VARIANTE FME : fin — Deploiement FME Server / FME Flow ================= -->

## Partis pris, hypothèses et limites connues

> Cette section explicite les décisions de conception et les hypothèses sur
> lesquelles elles reposent, ainsi que les limites et dettes techniques
> connues. Elle répond à *pourquoi l'outil est fait ainsi*. Distinguer trois
> catégories :
>
> - **Parti pris assumé** — choix de conception délibéré et cohérent.
> - **Limite / dette** — point à corriger ou surveiller, susceptible de
>   fausser un résultat ou de gêner la reprise.
> - **Question ouverte** — élément incertain, à confirmer auprès de l'auteur ;
>   ne pas considérer comme acquis.

### Partis pris assumés

[À compléter : un paragraphe par parti pris — le choix, et *ce que cela suppose*.]

### Limites et dettes connues

[À compléter : un paragraphe par limite — la nature du problème et le risque associé.]

---

## Guide de reprise et points d'attention

[À compléter : tout ce dont un tiers a besoin pour reprendre l'outil sans l'auteur.]

### Procédure d'exécution

1. [À compléter]

### Checklist avant modification

- [ ] [À compléter : ex. sauvegarder une copie datée de la source.]
- [ ] [À compléter]

### Diagnostic des erreurs fréquentes

| Symptôme | Cause probable | Action |
|----------|---------------|--------|
| [À compléter] | [À compléter] | [À compléter] |

---

## Glossaire

| Terme | Définition |
|-------|------------|
| [À compléter] | [À compléter] |
