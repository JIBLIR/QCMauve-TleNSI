import cherrypy
import os
import mysql.connector
import bcrypt # ---> Biblio pour le cryptage de mdp

#=============Site WEB=============#
def menu():
    if "user" in cherrypy.session:
        bouton = '<li id="co"><a href="/deconnexion">Se déconnecter</a></li>'
    else:
        bouton = '<li id="co"><a href="/connection">Se connecter</a></li>'

    return """
    <div id="nav">
        <ul>
            <li><a href="/">Accueil</a></li>
            <li>Classe
                <ul>
                    <li><a href="/seconde">Seconde</a></li>
                    <li><a href="/premiere">Première</a></li>
                    <li><a href="/terminale">Terminale</a></li>
                </ul>
            </li>
			<li><a href="/ajout_qcm">Ajout Qcm</a></li>
            <li><a href="/sup">Suprimmer un Qcm</a></li>
            """ + bouton + """
        </ul>
    </div>
    """

def index():
    return """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Mon site Web</title>
        <link rel="stylesheet" href="/style_projet_Bd_NSI.css">
    </head>
    <body>
        <h1>Site pour faire des qcm</h1>
        
        """ + menu() + """

        <p>Bonjour, vous voilà sur une page web où l'on peut reviser plusieures matiéres de différent classes.</p>
    </body>
</html>

	"""

index.exposed = True

def seconde(reponse=None):
    import mysql.connector

    index_question = cherrypy.session.get('index_question', 0)
    baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="P02QCM")
    curseur = baseDeDonnees.cursor()
    curseur.execute('select * from questions')
    questions = curseur.fetchall()
    question = questions[(index_question)]

    message = ""
    if reponse is not None:
        if str(reponse) == str(question[6]):
            message = 'bonne réponse!!'
            index_question += 1
        else:
            message = f'faux, {question[int(question[6]) + 1]}'
    cherrypy.session['index_question'] = index_question


    baseDeDonnees.close()

    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
		<link rel="stylesheet" href="/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>Site pour faire des qcm</h1>

		""" + menu() + f""" {question[1]}
    <form method="post" action="/seconde">
    <ol>
    <li> {question[2]} <input type="radio" value="1" name="reponse"  /> </li>
    <li> {question[3]} <input type="radio" value="2" name="reponse" /> </li>
    <li> {question[4]} <input type="radio" value="3" name="reponse" /> </li>
    <li> {question[5]} <input type="radio" value="4" name="reponse" /> </li>
    </ol>
    <button type="submit">Valider</button>
	
    <button type="submit" action="/seconde">Question Suivante</button>
    </form>

    <p>{message}</p>

    </body>
</html>
    """
seconde.exposed = True

def premiere():
    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
		<link rel="stylesheet" href="/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>Site pour faire des qcm</h1>

		""" + menu() + """
        
		<p>Premiere</p>
	</body>
</html>

	"""

premiere.exposed = True

def terminale():
    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
		<link rel="stylesheet" href="/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>Site pour faire des qcm</h1>

		""" + menu() + """
        
		<p>Terminale</p>
	</body>
</html>

	"""

terminale.exposed = True

#============= Ajout de Qcm =============#
def ajout_qcm(question=None,rep1=None,rep2=None,rep3=None,rep4=None,bonne_rep=None,matiere=None):

    if "role" not in cherrypy.session:
        raise cherrypy.HTTPRedirect("/connection")

    if cherrypy.session["role"] == 0:
        raise cherrypy.HTTPRedirect("/")

    if rep1 and rep2 and rep3 and rep4 and question :
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")
        cur = baseDeDonnees.cursor()
        cur.execute(
        "INSERT INTO questions (question,reponse1,reponse2,reponse3,reponse4,bonne_reponse,matiere) VALUES (%s,%s,%s,%s,%s,%s,%s)",(question,rep1,rep2,rep3,rep4,bonne_rep,matiere)
        )
        baseDeDonnees.commit()
        cur.close()
        baseDeDonnees.close()

    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Ajouter QCM</title>
		<link rel="stylesheet" href="/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>Ajouter un QCM</h1>
        
		""" + menu() + """
        
        <form method="post" action="/ajout_qcm">
			<input type="text" name="question" placeholder="Question"  required>
			<input type="text" name="rep1" placeholder="Réponse"  required>
			<input type="text" name="rep2" placeholder="Réponse"  required>
            <input type="text" name="rep3" placeholder="Réponse"  required>
            <input type="text" name="rep4" placeholder="Réponse"  required>
            <input type="number" name="bonne_rep" min="1" max="4"  required>
            <input type="text" name="matiere" placeholder="Matière"  required>
		<button type="submit">Valider</button>
		</form>
	</body>
</html>
"""
ajout_qcm.exposed = True

#============= Suppression =============#

def sup(id=None,question=None):

    if "role" not in cherrypy.session:
        raise cherrypy.HTTPRedirect("/connection")

    if cherrypy.session["role"] == 0:
        raise cherrypy.HTTPRedirect("/")

    liste_questions = ""
    message = ""

    if question :
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")
        cur = baseDeDonnees.cursor()
        cur.execute("SELECT id_question, question FROM questions WHERE question LIKE %s",("%" + question + "%",))
        resultat = cur.fetchall()

        if resultat :
            for liste in resultat:
                    id_question = liste[0]
                    question_l = liste[1]

                    liste_questions += """
                    <p>
                    """ + str(id_question) + """ - """ + question_l + """
                    <a href="/sup?id=""" + str(id_question) + """">Supprimer</a>
                    </p>
                """
        else:
            message = "<p>Aucune question trouvée.</p>"
        cur.close()
        baseDeDonnees.close()

    if id :
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")
        cur = baseDeDonnees.cursor()
        cur.execute("DELETE FROM questions WHERE id_question = %s",(id,))
        baseDeDonnees.commit()

        message = "<p>Question supprimée.</p>"

        cur.close()
        baseDeDonnees.close()

    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Ajouter QCM</title>
		<link rel="stylesheet" href="/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>Ajouter un QCM</h1>
        
		""" + menu() + """
        
        """ + message + """
        
        """ + liste_questions + """
        
		<form method="post" action="/sup">
    		<input type="text" name="question" placeholder="Chercher une question à supprimer" required>
    		<button type="submit">Valider</button>
		</form>
        
	</body>
</html>
"""
sup.exposed = True

#============= Connection =============#
def connection(identifiant=None, Mot_de_passe=None):

    if identifiant and Mot_de_passe:

        try:
            baseDeDonnees = mysql.connector.connect(host="localhost",user="nsi",password="nsi",database="P02QCM"
            )

            cur = baseDeDonnees.cursor()

            cur.execute(
                "SELECT mdp_user, metier FROM utilisateur WHERE nom_user = %s",(identifiant,)
            )

            resultat = cur.fetchone()

            if resultat:
                mdp_stocke = resultat[0]
                metier = resultat[1]
                # ERREUR : SI LE MDP EST FAUX
                if bcrypt.checkpw(Mot_de_passe.encode(), mdp_stocke.encode()):
                    cherrypy.session["user"] = identifiant
                    cherrypy.session["role"] = metier
                    raise cherrypy.HTTPRedirect("/")
                else:
                    print("Mot de passe incorrect")

            else:
                print("Utilisateur inconnu")

            cur.close()
            baseDeDonnees.close()

        except mysql.connector.Error :
            print("Erreur base de données")

    return"""
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
		<link rel="stylesheet" href="/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>Site pour faire des qcm</h1>
		
		""" + menu() + """
        
		<div id="inter_co">  
			<p style="text-decoration: underline">Se connecter</p>
			<form method="post" action="/connection">
				<input type="text" name="identifiant" placeholder="Identifiant"  required>
				<input type="password" name="Mot_de_passe" placeholder="Mot de passe" required>
			<button type="submit">Valider</button>
			</form>
			<p> <a href="/creer_compte"> Créer un compte </a> </p>
		</div>
	</body>
</html>

	"""

connection.exposed = True

#============= DECONNEXION =============#
def deconnexion():
    cherrypy.session.pop("user", None)
    raise cherrypy.HTTPRedirect("/")

deconnexion.exposed = True

#============= Creation de compte =============#
def creer_compte(Profession = None,identifiant = None,Mot_de_passe = None):
    message = ""
    if Profession and identifiant and Mot_de_passe :
        Profession = int(Profession)
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")
        cur = baseDeDonnees.cursor()
        cur.execute(
            "SELECT * from utilisateur WHERE nom_user = %s",(identifiant,)
		)
        result = cur.fetchall()
        if result :
            message = "<p style='color:red;'>Identifiant déjà pris</p>"
        else :
            mot_de_passe_hash = bcrypt.hashpw(Mot_de_passe.encode(), bcrypt.gensalt())
            cur.execute(
            "INSERT INTO utilisateur (nom_user,mdp_user,metier) VALUES (%s,%s,%s)",(identifiant,mot_de_passe_hash,Profession)
            )
            baseDeDonnees.commit()
            message = "<p style='color:green;'>Compte créé avec succès</p>"
        cur.close()
        baseDeDonnees.close()
    return """
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Mon site Web</title>
                    <link rel="stylesheet" href="/style_projet_Bd_NSI.css">
                </head>
                <body>
                    <h1>Site pour faire des qcm</h1>
                    
                    """ + menu() + """
                    
                    <div id="inter_co">  
                    <p style="text-decoration: underline">Créer un compte</p>
                        <form method="post" action="/creer_compte">
                            <select name="Profession">
                                <option value="1">Professeur</option>
                                <option value="0">Elève</option>
                            </select>
                            <input type="text" name="identifiant" placeholder="Identifiant"  required>
                            <input type="password" name="Mot_de_passe" placeholder="Mot de passe" minlength="16" required>
                        
                        <button type="submit">Valider</button>
                        </form>
                        
                        <p > <a href="/connection">Se connecter </a> </p>
                    </div>
                    """ + message + """
                </body>
            </html>"""

creer_compte.exposed = True

#=============Partie pour la mise en ligne du serveur=============#

#ip perso : 192.168.1.8
#ip lycée : 172.16.100.22

cherrypy.config.update({
	"server.socket_host"	:"127.0.0.1",
	"server.socket_port"	:5432,
	"server.socket_pool"	:5,
	"tools.sessions.on"		:True,
	"tools.encode.encoding"	:"utf-8",
	"tools.staticdir.on"	:True,
	"tools.staticdir.dir": os.path.join(os.getcwd(), "static_2")
})

cherrypy.tree.mount(index, "/")
cherrypy.tree.mount(seconde, "/seconde")
cherrypy.tree.mount(premiere, "/premiere")
cherrypy.tree.mount(terminale, "/terminale")
cherrypy.tree.mount(ajout_qcm, "/ajout_qcm")
cherrypy.tree.mount(sup, "/sup")
cherrypy.tree.mount(connection, "/connection")
cherrypy.tree.mount(deconnexion, "/deconnexion")
cherrypy.tree.mount(creer_compte, "/creer_compte")



cherrypy.engine.start()
cherrypy.engine.block()
