# Projet GéoID — non cadré

⚠️ **Ce projet n'a pas encore été cadré.**

Règles applicables dès maintenant :
1. Lire `CHARTE.md` (règles transverses du pôle GéoID) — elle s'applique
   intégralement.
2. Le plugin d'équipe `geoid` (agents, skills et commandes du pôle) est
   **déjà déclaré** dans `.claude/settings.json` : il s'installe
   automatiquement au démarrage de la session, sans manipulation. Au besoin,
   vérifier avec `/plugin` que `geoid` est bien actif ; il se met à jour tout
   seul (`autoUpdate`).
3. Avant toute production significative, proposer à l'utilisateur de lancer
   la commande **`geoid:cadrer-projet`**, qui mènera l'entretien de cadrage
   et remplacera ce fichier par le CLAUDE.md du projet (objectif, données,
   livrables, équipe d'agents retenue, points à arbitrer).
4. En attendant le cadrage : répondre aux questions, explorer l'existant,
   mais ne pas engager de développement structurant.

Agents fournis par le plugin `geoid` (invocables `@geoid:<agent>`) :
`architecte`, `developpeur`, `analyste_sig`, `revieweur`, `documentaliste`,
`chef_projet`, `mentor`. Les agents skill-builder (`interviewer_skill`,
`redacteur_skill`, `critique_skill`) vivent dans le plugin `geoid-meta`,
réservé au mainteneur du socle : ils sont absents des projets d'équipe par
construction. Des spécialisations du développeur sont disponibles dans
`specialisations/` (template résiduel) et la seule retenue est copiée au
cadrage selon la famille de projet.
