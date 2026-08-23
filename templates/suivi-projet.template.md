<!-- ════════════════════════════════════════════════════════════════
     docs/suivi-projet.md — {{NOM_PROJET}}
     Suivi opérationnel du projet : incréments, backlog, risques,
     historique des revues. Volontairement HORS du CLAUDE.md : ce
     fichier grossit avec le projet et n'a pas à occuper le contexte de
     chaque session — les agents le lisent à la demande (clôture de
     session, reporting). Le CLAUDE.md ne garde que ce qui guide la
     décision au quotidien (dont l'incrément en cours, en deux lignes).
     Généré le {{DATE}} via /geoid:cadrer-projet.
     ════════════════════════════════════════════════════════════════ -->

# Suivi du projet — {{NOM_PROJET}}

Tenu à jour par le `chef_projet` (ou l'orchestrateur s'il n'est pas
activé), notamment via `/geoid:cloturer-session`. L'humain valide ce qui
entre ici (cf. CHARTE §4 et §5).

## 1. Incréments métier

Un projet avance par **incréments que le métier peut essayer**, pas par
tâches techniques cochées. Chaque ligne décrit un résultat utilisable de
bout en bout, formulé du point de vue de l'utilisateur, avec le critère
qui permettra de dire « c'est bon ». **Pas de critère de recette écrit =
pas d'incrément.**

Statuts : `À faire` · `En cours` · `En recette` · `Recetté` · `Abandonné`.

| ID | Incrément (formulé métier) | Valeur : pour qui, quoi | Critère de recette (observable) | Démo / recette prévue | Statut |
|----|----------------------------|-------------------------|---------------------------------|-----------------------|--------|
| INC-01 | {{ex. le chargé d'études masque une couche et retrouve son choix à la reconnexion}} | {{pour qui / quel gain}} | {{ce qu'un tiers observe pour valider}} | {{date ou séance}} | À faire |

> Cycle sans aucun incrément recettable (refactor, dette, socle
> technique) : le noter ici explicitement, avec ce qu'il rend possible et
> pourquoi il ne pouvait pas être embarqué dans un incrément porteur.
> Possible, mais jamais l'état par défaut.

## 2. Roadmap / backlog

Chaque tâche est rattachée à un incrément du §1. Une tâche orpheline est
un signal : soit elle sert un incrément qu'on n'a pas nommé, soit elle ne
sert personne.

| ID | Tâche | Incrément | Priorité | Responsable / agent | Statut | Échéance |
|----|-------|-----------|----------|---------------------|--------|----------|
| {{...}} | | INC-0X | | | À faire / En cours / En revue / Terminé / Bloqué | |

## 3. Registre des risques

| ID | Risque | Probabilité | Impact | Mitigation | Statut |
|----|--------|-------------|--------|------------|--------|
| {{...}} | | | | | |

## 4. Suivi des revues

| Date | Livrable | Verdict | Points bloquants | Suite |
|------|----------|---------|------------------|-------|
| {{AAAA-MM-JJ}} | {{...}} | Approuvé / Sous réserve / Refusé | | |

## 5. Recettes prononcées

La revue (§4) dit que le livrable est conforme ; la recette dit que le
métier en veut bien. Les deux sont distinctes — un livrable
techniquement irréprochable peut être refusé en recette.

| Date | Incrément | Qui recette | Verdict | Écart constaté | Suite |
|------|-----------|-------------|---------|----------------|-------|
| {{AAAA-MM-JJ}} | INC-0X | {{utilisateur métier}} | Recetté / Réserves / Refusé | | |
