### Semaine 1 ~ 9 - 15 mars :
### Jb
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
### Jules
### Journée du 7-8 mars

Creation du site:
            Creation du bouton pour sélectioner la classe voulu.
            Creation du bouton pour se connecter et créer un compte 

### Journée du 13 mars : 
   Installation d'enregistrement en sql dans creer_compte



