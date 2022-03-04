# LITReview

Lit review est une application web permettant de demander des critiques de livres, ainsi que de 
repondre à ces demandes en écrivant des critiques.

## Installation et lancement

### 1 - Téléchargez
Téléchargez et décompressez ce depot github, ou clonez-le.

### 2 - Environement virtuel
Placez-vous dans le répertoire racine du projet (au même niveau que le fichier 'manage.py')
Installez votre environement virtuel:
(développé avec la version 3.9 de python, il se peut qu'une verison plus ancienne pose problème pour les dépendences)
Tapez en console:

```sh
python3 -m venv env
```

et activez cet environnement virtuel:

```sh
source env/bin/activate
```

### 3 - Installez les dépendences

```sh
pip install -r requirements.txt
```


### 4 - Lancez le serveur

```sh
./manage.py runserver
```

### 5 - Accédez à l'application
Dans votre navigateur, allez à l'adresse suivante:

http://localhost:8000

## Données de test

Dans les données fournies (fichier db.sqlite3), vous trouverez trois comptes utilisateurs dont les logins sont:
- tata
- toto
- tutu

et un compte administrateur:
- admin

Tous ces comptes ont le même mot de passe:

testpass1


## Remarque

Votre ordinateur doit être connecté à internet, car LitReview importe des ressources extérieures (bulma et material design via cdn).

## Utilisation de l'application

La page d'accueil vous propose soit de créer un nouveau compte, soit de vous connecter avec un compte existant.
Une fois connecté, vous êtes redirigé vers votre flux. Une barre de navigation vous permet de choisir entre différentes fonctionnalités:

### Flux

Ici vous verrez s'afficher tous les posts qui vous concernent (les votre et ceux des utilisateurs que vous suivez).
Une pagination vous permet d'accéder aux posts plus anciens.
La page de flux vous propose aussi deux options:
- demander une critique
- créer une critique  
Ces deux options vous redirigeront vers des formulaires adaptés.  
Dans votre flux, les demandes de critiques qui n'ont pas encore reçu de réponse apparaissent avec un bouton "créer une critique", utilisez ce bouton pour répondre à la demande avec le formulaire qui vous sera proposé.


### Posts

Ici vont s'afficher vos propre posts, vous pouvez soit les modifier (un formulaire vous sera alors proposé), soit les supprimer.


### Abonnements

Cette fonctionnalité vous propose de suivre des utilisateurs, ou au contraire de vous désabonner.
Pour suivre un utilisateur, il suffit de taper son nom dans le champ, puis cliquer sur "envoyer".

Pour se désabonner, cliquez sur le bouton "se désabonner" correspondant, une confirmation vous sera demandée.


### LITReview
Cliquer sur "LitReview" vous raménera à la page d'accueil.

### Se deconnecter
Déconnecte l'utilisateur.
