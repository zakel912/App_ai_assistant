# App_ai_assistant

Ce projet permet de créer une application web prototype servant notamment à développer une interface utilisateur et simuler une interaction avec un assistant AI qui n'est ici qu'une simple fonction rules-based.

## Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés :
- Python 3.6 au minimum, version utilisé : Python 3.12.3
- Flask

## Créez un environnement virtuel :
  python -m venv venv

## Activez l'environnement virtuel :
Sur Windows :
  venv\Scripts\activate

Sur Linux/MacOS :
  source venv/bin/activate

## Installez les dépendances requises :
  pip install -r requirements.txt

## Utilisation
Lancez l'application Flask : flask run
  
L'application sera accessible à l'adresse suivante : http://127.0.0.1:5000/.

## Structure du Projet
- app.py: Le point d'entrée principal de l'application Flask.

- main.py: Contient une logique simpliste d'un chatbot, pour simuler ses réponses et les utiliser sur l'interface.

- templates/: Dossier contenant les fichiers HTML (si une interface web est utilisée).

- static/: Dossier contenant les fichiers statiques comme CSS, JavaScript, et images.
