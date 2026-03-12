# importation
import mysql.connector

# ATTENTION !! : les valeurs peuvent changer selon les paramètres mysql de l'ordinateur
# ici on a identifiant : nsi, mot de passe : nsi et database : P02QCM en localhost
baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")

# on créé un curseur de la base de données
curseur = baseDeDonnees.cursor()
# le curseur est stocké dans la liste questions qui est composé de toutes les colonnes du tableau questions
curseur.execute('select * from questions')
questions = curseur.fetchall()

# on itère une question contenu dans les questions (c'est concret)
for question in questions:
	# on affiche la question (de la colonne 1 de la table)
	print(question[1])
	# on affiche les réponses possibles
	# les réponses possibles sont stockées dans les colonnes 2,3,4,5
	for i in range(2,6):
		print(f'{i-1}. {question[i]}')
	# on demande la réponse
	rep = int(input('>>'))
	# on vérifie la réponse avec la colonne 6 du tableau : la bonne réponse qui a pour valeurs possibles [1,2,3,4]
	if rep == question[6]: print('bonne réponse!!')
	else: print('faux')

# on sauvegarde et on ferme la base de données
baseDeDonnees.commit()
baseDeDonnees.close()
