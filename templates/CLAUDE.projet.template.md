<!-- ════════════════════════════════════════════════════════════════
     CLAUDE.md — {{NOM_PROJET}}
     Couche 2 : spécificités projet. La CHARTE.md (couche 1, règles
     transverses GéoID) s'applique intégralement et prime en cas de
     contradiction non actée au journal.
     Généré le {{DATE}} via /geoid:cadrer-projet.
     ════════════════════════════════════════════════════════════════ -->

# {{NOM_PROJET}}

> ⚖️ Règles transverses : voir `CHARTE.md` (langue, SRC, sécurité,
> méthode ADR, revue, comptes rendus). Non recopiées ici.
>
> 📦 Version socle — plugin geoid : {{VERSION_PLUGIN_GEOID}} (marketplace) ;
> template résiduel : {{VERSION_TEMPLATE}} (dernier merge).
>
> 🔌 Serveurs MCP (`.mcp.json`, si le projet en a) : **lecture seule** et
> identifiants via **variables d'environnement** — jamais de secret en
> clair (CHARTE §4 ; gabarit `templates/mcp.projet.template.json`).

> 📏 **Hygiène — ce fichier est lu en entier à chaque session : il reste
> court** (< 180 lignes). Critère de tri : *une ligne reste ici si elle
> change une décision dans n'importe quelle session* ; sinon elle part
> dans `docs/`, lu à la demande. Donc **jamais** ici : glossaire, état
> d'avancement, historique de sprints, roadmap ou backlog, comptes rendus
> de session, tutoriels, recopie de la CHARTE ou d'un skill. Le
> dégraissage fait partie de `/geoid:cloturer-session`.

## 0. Orchestration (session principale)
Tu coordonnes le travail substantiel ; tu traites directement le
trivial. Tu **ne délègues qu'aux agents listés au §5** : les agents du
plugin `geoid` sont tous techniquement invocables (`@geoid:<agent>`),
mais la table §5 est **normative** — un agent absent du §5 n'est pas
mobilisé sur ce projet, même s'il répond. Délègue dès qu'une tâche est
spécialisée, longue ou engageante (code de production, analyse, décision
de conception, revue) ; réponds toi-même aux questions rapides et
micro-modifications — déléguer du trivial coûte plus qu'il ne rapporte.
Avant une demande non triviale : analyse (1-2 phrases), agents
mobilisés, mission de chacun. Un point `🔧 À ARBITRER` ne bloque que les
tâches qui **dépendent** de la décision (colonne « Tâches bloquées » du
§9) — le reste du projet avance. Tout livrable **final ou de
production** passe par le `revieweur` (pas les brouillons ni les
intermédiaires). Chaque décision actée est reportée au journal (§11)
après validation humaine. Le suivi opérationnel (incréments, backlog,
risques, revues) vit dans `docs/suivi-projet.md`, pas ici.

**Cap de travail** : rattache ce que tu fais à l'**incrément en cours**
(§2) ; si une demande n'y contribue pas, dis-le et propose de la rattacher
à un incrément nommé ou d'en ouvrir un. Cette discipline ne dépend pas de
la présence du `chef_projet` au §5 : s'il n'est pas activé, elle t'incombe.

## 1. Identité
- **Famille** : {{FAMILLE}} (étude / pipeline / dev applicatif / pilotage)
- **Commanditaire** : {{COMMANDITAIRE}}
- **Parties prenantes** : {{PARTIES_PRENANTES}}

## 2. Objectif
{{OBJECTIF — problème, résultat attendu}}
- **Critères de réussite** : {{CRITERES}}
- **Échéance** : {{ECHEANCE}}

### Incrément en cours
- **Incrément** : {{INC-0X — ce que le métier pourra essayer, dit de son
  point de vue}}
- **Critère de recette** : {{ce qu'un tiers observe pour dire « c'est bon »}}

> Le projet avance par **incréments métier recettables** : chaque cycle
> vise quelque chose qu'un utilisateur peut prendre en main et valider,
> pas une couche technique terminée. Un cycle sans incrément recettable
> reste possible, mais se justifie explicitement. Tableau complet des
> incréments et des recettes : `docs/suivi-projet.md`.

## 3. Données
| Donnée | Rôle (source/produite) | Millésime | Sensibilité | Notes |
|--------|------------------------|-----------|-------------|-------|
| {{...}} | | | | |

## 4. Livrables
| Livrable | Format | Destinataire |
|----------|--------|--------------|
| {{...}} | | |

## 5. Équipe d'agents
| Agent | Rôle sur ce projet |
|-------|--------------------|
| {{...}} | |

**Équipe humaine & apprentissage** : {{QUI + NIVEAUX + OBJECTIFS
D'APPRENTISSAGE — le mentor s'en sert pour calibrer}}

## 6. Stack technique
⚠️ Tout code généré doit être compatible avec ces versions. Ne jamais
supposer une version non listée ; si une case est `à vérifier`, demander
avant de produire du code qui en dépend.

| Composant | Version | Environnement / notes |
|-----------|---------|-----------------------|
| {{ex. Python}} | {{3.x}} | {{où il s'exécute}} |
| {{ex. Postgres / PostGIS}} | {{x.x / x.x}} | |
| {{ex. ArcGIS Enterprise / ExB}} | {{x.x}} | |
| {{ex. FME / QGIS}} | {{x.x}} | |

- **Paquets / bibliothèques** : {{disponibles, imposés, gestionnaire
  autorisé (pip/conda), environnement verrouillé ou non}}
- **Environnements** : {{dev / recette / prod, OS, accès réseau/proxy}}

## 7. Conventions spécifiques
{{Outils, conventions propres au projet — uniquement ce qui
s'ajoute à la CHARTE}}

## 8. Grilles de revue spécifiques
{{Checklists par type de livrable, utilisées par le revieweur en plus de
sa grille socle}}

## 9. Décisions en attente (ADR)
Propriétaire : `architecte`. Un ADR ouvert ne bloque que les tâches
listées dans sa colonne « Tâches bloquées » : une analyse, une doc, un
test ou une maquette qui n'en dépend pas peut avancer.

| ADR | Sujet | Tâches bloquées en attendant | Statut |
|-----|-------|------------------------------|--------|
| ADR-001 | {{...}} | {{ex. écriture du schéma, migrations}} | À décider |

## 10. Suivi du projet
Tableau des incréments et des recettes, roadmap / backlog, registre des
risques et historique des revues : **`docs/suivi-projet.md`** (mis à jour
via `/geoid:cloturer-session`). Ils ne vivent pas ici pour garder ce
fichier court — il est lu à chaque session. Seul l'**incrément en cours**
est repris ci-dessus (§2), en deux lignes.

## 11. Journal des décisions
| Date | Sujet | Décision | Justification |
|------|-------|----------|---------------|
| {{AAAA-MM-JJ}} | {{...}} | {{...}} | {{...}} |
