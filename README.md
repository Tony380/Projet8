# Projet8
Créez une plateforme pour amateurs de Nutella

## Présentation
Purbeurre est une application qui permet de trouver un substitut plus sain pour un produit
que vous utilisez au quotidien.

Pour cela, l'application utilise la base de données d'OpenFoodFacts.

Tapez le nom du produit que vous voulez substituer. 
Une liste de substituts possibles apparaît.

Vous pouvez voir la fiche de ce produit qui contient ses repères nutritionnels.

Vous pouvez aussi selectionner ce produit afin de le sauvegarder dans vos favoris si 
vous possédez un compte utilisateur.

## Installation et utilisation sur votre ordinateur
Pour utiliser l'application sur votre serveur local:

1. Clonez ce projet sur votre ordinateur.
2. Installez les dépendances du fichier requirements.txt.
3. Vous aurez besoin de créer une base de données avec postgreSQL nommée 'purbeurre'.
Vous pouvez configurer les options qui vous sont personnelles dans le fichier settings.py
dans la partie DATABASE = { }.
4. Toujours dans le fichier settings.py, configurez l'option 'ALLOWED_HOSTS' de la manière suivante:

        ALLOWED_HOSTS = ['*']
        
5. Générez une clé secrète dans la console comme suit:

        $ python
    
        import random, string
    
        "".join([random.choice(string.printable) for _ in range(24)])

6. Gardez cette clé dans vos variables d'environnement en tant que 'SECRET_KEY'.
7. Enfin, lancez le fichier manage.py en console de cette manière:
python manage.py runserver


## L'application en ligne
Cette application est aussi utilisable en ligne.

Elle est hébergée sur Heroku et utilisable [ici](https://purbeurre2020.herokuapp.com "purbeurre").

## Information complétaire
Le tableau Trello relatif à ce projet se trouve [ici](https://trello.com/b/RhX1abT3/projet-8 "Tableau Trello").

