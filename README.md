<h1 align="center">API</h1>

<p align="center"><b>L'API est hébergée sur Heroku. Pour des raisons financières, le serveur est désactivé en dehors des phases de test.</b></p>

# C'est quoi API ?
Il s'agit de l'API construit afin de retourner la probabilité de faire défaut des clients de home Credit Risk Default. 

La page d'accueil ne comprend qu'un simple message de bienvenue.

# Découpage des dossiers
- **main.py** : fichier principal contenant le code de l'API
- **requirements.txt** : contient toutes les dépendances à installer pour faire marcher l'API
- **runtime.txt** : signale à Heroku avec quel langage exécuter l'application
- **Procfile** : contient la ligne de commande que Heroku doit exécuter pour que l'API se mette en marche
- **model.pkl** : modèle avec lequel la prédiction du score est réalisée
- **test.py** :  tests unitaires de l'API
- **model.py** : contient la classe pour valider les données d'entrée et la classe pour réaliser le predict_proba du modèle final.