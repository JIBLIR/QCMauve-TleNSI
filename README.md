<img width="1918" height="1078" alt="Capture d&#39;écran 2026-05-14 190230" src="https://github.com/user-attachments/assets/39541e9d-3adf-4042-9501-17c0d0dfaee9" />

## Jb
### Semaine 1 ~ 9 - 15 mars :
#### ~ _I Création de setup.sql afin d'instancier les tables sql_

_pour le setup des fichiers sql, nous avons besoin de différents prérequis :_  \
            1. **Installation de Mysql ou Mariadb**  \
            2. **Création d'une database PQCM02, avec** 
            
  ```sql 
CREATE DATABASE PQCM02;
```

3. **instanciation du fichier setup.sql**
le fichier setup.sql permet d'instancier toutes les tables de la database


```sql
USE PQCM02;
SOURCE ./setup.sql;
```


une fois ces étapes réalisés dans le terminal avec mysql, nous pouvons utiliser nos QCMs depuis la base de données


#### ~ _II Création de questionnaire.sql afin de tester notre database avec un petit programme_
### Semaine ~ 6 - 12 avril :
#### ~ _III Application de questionnaire.sql au Site pour faire un QCM_
### 23 avril :
#### ~ _IV Correction des bugs de connexion et fusion des codes_
### 14 mai amélioration de l'interface web :
#### ~ _V Correction des bugs de connexion et fusion des codes_
## Jules
### Journée du 7-8 mars

Creation du site:
            Creation du bouton pour sélectioner la classe voulu. 
             Creation du bouton pour se connecter et créer un compte.
### Journée du 13 mars : 
   Installation d'enregistrement en sql dans creer_compte

### Journée du 29 mars :
   Ajout de la partie de cryptage puis recherche du bon mdp dans la base de donnée dans la fonction connection
### Semaine du 12 avril : 
   Modification de la partie cryptage avec la mise en place de la bibliotheque bcrypt qui hach le mdp 
   Puis mise en place d'un debut de chopse pour l'autentification directement sur le site 
### Samedi 18 avril :
   Ajout de deux fonctions une qui permet d'ajouter des qcms si l'on est connecté et en tant que professeur puis une autre qui permet de suprimmer des qcms si l'on est connecter en tant que professeur aussi. J'ai pu aussi mettre une condition dans le creer_compte avec que si le nom de user donné par la personne qui veut créer un compte est deja prise alors l'utilisateur qui crée le compte est signallé que le nom est deja prit. J'ai aussi donc mis en place le system de session qui permet de restreindre certaines parties du sites.  
