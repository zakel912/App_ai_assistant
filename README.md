# App_ai_assistant
# Chatbot Rule-Based avec Flask

Ce projet est un chatbot simple basé sur des règles, développé avec le framework Flask. Le chatbot peut répondre à certaines commandes spécifiques selon des règles prédéfinies.

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- Python 3.6 au minimum, version utilisé : Python 3.12.3
- Flask

# Créez un environnement virtuel :
  python -m venv venv

# Activez l'environnement virtuel :
Sur Windows :
  venv\Scripts\activate

Sur Linux/MacOS :
  source venv/bin/activate

# Installez les dépendances requises :
  pip install -r requirements.txt

# Utilisation
Lancez l'application Flask :
  flask run
L'application sera accessible à l'adresse suivante : http://127.0.0.1:5000/.
L'application est notamment développer pour construire une interface utilisateur et simuler une vrai interaction avec un assistant AI

# Structure du Projet
app.py: Le point d'entrée principal de l'application Flask.
main.py: Contient une logique simpliste d'un chatbot, pour simuler ses réponses et les utiliser sur l'interface.
templates/: Dossier contenant les fichiers HTML (si une interface web est utilisée).
static/: Dossier contenant les fichiers statiques comme CSS, JavaScript, et images.
