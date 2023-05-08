# Task_github
Ce script utilise la bibliothèque requests pour effectuer des requêtes HTTP à l'API REST de GitHub. Il utilise également le module json pour formater les données envoyées avec la requête.

Vous devez remplacer les variables suivantes par les vôtres :

 - repo_owner : le nom d'utilisateur du propriétaire du référentiel.
 - repo_name : le nom de votre projet.
 - project_id : l'ID de votre projet GitHub.
 - access_token : votre jeton d'accès personnel généré précédemment.

Le script parcourt ensuite la liste des tâches et appelle la fonction create_task pour chaque tâche. La fonction create_task envoie une requête POST à l'API REST de GitHub pour créer une nouvelle tâche dans votre projet.

Si la tâche est créée avec succès, le script affichera un message de confirmation. Sinon, le script affichera un message d'erreur avec le code d'état de la réponse.

Vous pouvez exécuter ce script sur votre ordinateur
