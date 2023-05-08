import requests
import json

# Remplacez les variables suivantes par les vôtres
repo_owner = "votre_nom_d_utilisateur"
repo_name = "nom_de_votre_projet"
project_id = "l'id_de_votre_projet"
access_token = "votre_token_d_acces_personnel"

# Créer une tâche dans le projet GitHub
def create_task(task_title):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/projects/{project_id}/tasks"
    headers = {
        "Accept": "application/vnd.github.inertia-preview+json",
        "Authorization": f"token {access_token}"
    }
    data = {
        "content": task_title
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        print(f"La tâche '{task_title}' a été créée avec succès !")
    else:
        print(f"La création de la tâche '{task_title}' a échoué avec le code d'état {response.status_code} : {response.content}")

# Ajouter les tâches à votre projet GitHub
tasks = [
    "Tâche 1",
    "Tâche 2",
    "Tâche 3"
]

for task in tasks:
    create_task(task)
