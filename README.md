# LitReview

Lit review est une application web permettant de demander des critiques de livres, ainsi que

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

Tous cest comptes ont le même mot de passe:

testpass1


## Remarque

Votre ordinateur doit être connecté à internet, car LitReview importe des ressources extérieures (bulma via cdn).
