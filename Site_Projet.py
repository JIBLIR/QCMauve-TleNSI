import cherrypy
import os
import mysql.connector
import bcrypt  # ---> Biblio pour le cryptage de mdp


# =============Site WEB=============#
def menu():

    if "role" in cherrypy.session and cherrypy.session["role"] == 1:
        bouton = '''
        <li><a href="/ajout_qcm">Ajout Qcm</a></li>
        <li><a href="/sup">Supprimer un Qcm</a></li>
        <li id="co"><a href="/deconnexion">Se déconnecter</a></li>
        '''
        statut = ' Accès Professeur'

    elif "user" in cherrypy.session:
        bouton = '''
        <li id="co"><a href="/deconnexion">Se déconnecter</a></li>
        '''
        statut = 'Accès Étudiant'

    else:
        bouton = '''
        <li id="co"><a href="/connection">Se connecter</a></li>
        '''
        statut = 'Accès Visiteur'

    return """
    <div id="nav">
        <ul>
            <li><a href="/">Accueil</a></li>

            <li class="dropdown">
                <a href="#">Classe</a>
                <ul class="dropdown-menu">
                    <li><a href="/seconde">Seconde</a></li>
                    <li><a href="/premiere">Première</a></li>
                    <li><a href="/terminale">Terminale</a></li>
                </ul>
            </li>

            """ + bouton + statut + """
        </ul>
    </div>
    """

def index():
    if "user" in cherrypy.session:
        message = '<img src="https://images7.memedroid.com/images/UPLOADED844/59be7d31cb08b.jpeg">' + '<br> <i>Vous pouvez désormais ajouter et supprimer des QCMs</i>'
    else:
        message = '<img src="https://storage.googleapis.com/proudcity/elgl/uploads/2023/04/yoda.jpg" alt="alternatetext">' + "<br> <i>Bonjour, vous voilà sur une page web où l'on peut reviser plusieures matières de différentes classes.</i>"
    return """
<!DOCTYPE html>
<html>
    <head>
    <meta charset="utf-8">
    <title>Mon site Web</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100..800&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="/style_projet_Bd_NSI.css">
</head>
    <body>
        <h1>QCMauve</h1>
        
        """ + menu() + message + """
    </body>
</html>

	"""


index.exposed = True


def seconde(reponse=None, action=None):

    index_question = cherrypy.session.get('index_question_seconde', 0)
    baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="PQCM02")
    cur = baseDeDonnees.cursor()
    cur.execute("SELECT * FROM questions WHERE classe = 2")
    questions = cur.fetchall()

    if len(questions) == 0:
        return "<h1>Aucune question pour Seconde</h1>"

    if index_question >= len(questions):
        index_question = 0

    question = questions[index_question]

    message = ""

    if action == "valider":
    
        if reponse is None or reponse == "":
            message = "Veuillez sélectionner une réponse."
        elif str(reponse) == str(question[6]):
            message = "Bonne réponse !"
        else:
            message = f"Faux ! Bonne réponse : {question[int(question[6]) + 1]}"

    elif action == "suivante":
        index_question += 1

    if index_question >= len(questions):
        index_question = 0

    cherrypy.session['index_question_seconde'] = index_question


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
		<h1>QCMauve</h1>

		""" + menu() + f""" {question[1]}
    <form method="post" action="/seconde">
    <ol>
    <li> {question[2]} <input type="radio" value="1" name="reponse"  /> </li>
    <li> {question[3]} <input type="radio" value="2" name="reponse" /> </li>
    <li> {question[4]} <input type="radio" value="3" name="reponse" /> </li>
    <li> {question[5]} <input type="radio" value="4" name="reponse" /> </li>
    </ol>
    <button type="submit" name="action" value="valider">Valider</button>

    <button type="submit" name="action" value="suivante">Question Suivante</button>
	
    
    </form>

    <p>{message}</p>

    </body>
</html>
    """


seconde.exposed = True


def premiere(reponse=None, action=None):

    index_question = cherrypy.session.get('index_question_premiere', 0)
    baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="PQCM02")
    cur = baseDeDonnees.cursor()
    cur.execute("SELECT * FROM questions WHERE classe = 1")
    questions = cur.fetchall()

    if len(questions) == 0:
        return "<h1>Aucune question pour Premiere</h1>"

    if index_question >= len(questions):
        index_question = 0

    question = questions[index_question]

    message = ""

    if action == "valider":
    
        if reponse is None or reponse == "":
            message = "Veuillez sélectionner une réponse."
        elif str(reponse) == str(question[6]):
            message = "Bonne réponse !"
        else:
            message = f"Faux ! Bonne réponse : {question[int(question[6]) + 1]}"

    elif action == "suivante":
        index_question += 1

    if index_question >= len(questions):
        index_question = 0

    cherrypy.session['index_question_premiere'] = index_question


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
		<h1>QCMauve</h1>

		""" + menu() + f""" {question[1]}
    <form method="post" action="/premiere">
    <ol>
    <li> {question[2]} <input type="radio" value="1" name="reponse"  /> </li>
    <li> {question[3]} <input type="radio" value="2" name="reponse" /> </li>
    <li> {question[4]} <input type="radio" value="3" name="reponse" /> </li>
    <li> {question[5]} <input type="radio" value="4" name="reponse" /> </li>
    </ol>
    <button type="submit" name="action" value="valider">Valider</button>

    <button type="submit" name="action" value="suivante">Question Suivante</button>
	
    
    </form>

    <p>{message}</p>

    </body>
</html>
    """


premiere.exposed = True


def terminale(reponse=None, action=None):
    index_question = cherrypy.session.get('index_question_terminale', 0)
    baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="PQCM02")
    cur = baseDeDonnees.cursor()
    cur.execute("SELECT * FROM questions WHERE classe = 0")
    questions = cur.fetchall()

    if len(questions) == 0:
        return "<h1>Aucune question pour Terminale</h1>"

    if index_question >= len(questions):
        index_question = 0

    question = questions[index_question]

    message = ""

    if action == "valider":
    
        if reponse is None or reponse == "":
            message = "Veuillez sélectionner une réponse."
        elif str(reponse) == str(question[6]):
            message = "Bonne réponse !"
        else:
            message = f"Faux ! Bonne réponse : {question[int(question[6]) + 1]}"

    elif action == "suivante":
        index_question += 1

    if index_question >= len(questions):
        index_question = 0

    cherrypy.session['index_question_terminale'] = index_question


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
		<h1>QCMauve</h1>

		""" + menu() + f""" {question[1]}
    <form method="post" action="/terminale">
    <ol>
    <li> {question[2]} <input type="radio" value="1" name="reponse"  /> </li>
    <li> {question[3]} <input type="radio" value="2" name="reponse" /> </li>
    <li> {question[4]} <input type="radio" value="3" name="reponse" /> </li>
    <li> {question[5]} <input type="radio" value="4" name="reponse" /> </li>
    </ol>
    <button type="submit" name="action" value="valider">Valider</button>

    <button type="submit" name="action" value="suivante">Question Suivante</button>
	
    
    </form>

    <p>{message}</p>

    </body>
</html>
    """

terminale.exposed = True


# ============= Ajout de Qcm =============#
def ajout_qcm(question=None, rep1=None, rep2=None, rep3=None, rep4=None, bonne_rep=None, matiere=None, classe=None):
    if "role" not in cherrypy.session:
        raise cherrypy.HTTPRedirect("/connection")

    if cherrypy.session["role"] == 0:
        raise cherrypy.HTTPRedirect("/")

    if rep1 and rep2 and rep3 and rep4 and question and classe:
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="PQCM02")
        cur = baseDeDonnees.cursor()
        cur.execute(
            "INSERT INTO questions (question,reponse1,reponse2,reponse3,reponse4,bonne_reponse,matiere,classe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (question, rep1, rep2, rep3, rep4, bonne_rep, matiere, classe)
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
            <select name="classe" required>
                <option value="">Sélectionner une classe</option>
                <option value="2">Seconde</option>
                <option value="1">Première</option>
                <option value="0">Terminale</option>
            </select>
		<button type="submit">Valider</button>
		</form>
	</body>
</html>
"""


ajout_qcm.exposed = True


# ============= Suppression =============#

def sup(id=None, question=None):
    if "role" not in cherrypy.session:
        raise cherrypy.HTTPRedirect("/connection")

    if cherrypy.session["role"] == 0:
        raise cherrypy.HTTPRedirect("/")

    liste_questions = ""
    message = ""

    if question:
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="PQCM02")
        cur = baseDeDonnees.cursor()
        cur.execute("SELECT id_question, question FROM questions WHERE question LIKE %s", ("%" + question + "%",))
        resultat = cur.fetchall()

        if resultat:
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

    if id:
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="PQCM02")
        cur = baseDeDonnees.cursor()
        cur.execute("DELETE FROM questions WHERE id_question = %s", (id,))
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


# ============= Connection =============#
def connection(identifiant=None, Mot_de_passe=None):
    message = ""
    if identifiant and Mot_de_passe:

        try:
            baseDeDonnees = mysql.connector.connect(host="localhost", user="nsi", password="nsi", database="PQCM02"
                                                    )

            cur = baseDeDonnees.cursor()

            cur.execute(
                "SELECT mdp_user, metier FROM utilisateur WHERE nom_user = %s", (identifiant,)
            )

            resultat = cur.fetchone()

            if resultat:
                mdp_stocke = resultat[0]
                metier = resultat[1]
                try:
                    if bcrypt.checkpw(Mot_de_passe.encode(), mdp_stocke.encode()):
                        cherrypy.session["user"] = identifiant
                        cherrypy.session["role"] = metier
                        raise cherrypy.HTTPRedirect("/")
                    else:
                        message = "<p style='color:red;'>Mot de passe incorrect</p>"
                except cherrypy.HTTPRedirect:
                    raise
                except Exception as e:
                    message = "<p style='color:red;'>Erreur lors de la connexion</p>"
                    print(f"Erreur : {e}")

            else:
                message = "<p style='color:red;'>Identifiants incorrects</p>"

            cur.close()
            baseDeDonnees.close()

        except mysql.connector.Error:
            print("Erreur base de données")

    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
        <link rel="stylesheet" href="/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>QCMauve</h1>
		
		""" + menu() + '<img src = "https://preview.redd.it/star-wars-death-star-2560x1440-v0-2081l20zh4by.png?auto=webp&s=7f0aa73f483d647681238ea2c5ce169f4db24604" width="1500" >' + """
        
		<div id="inter_co">  
			<p style="text-decoration: underline">Se connecter</p>
			<form method="post" action="/connection">
				<input type="text" name="identifiant" placeholder="Identifiant"  required>
				<input type="password" name="Mot_de_passe" placeholder="Mot de passe" required>
			<button type="submit">Valider</button>
			</form>
            """+message +"""
			<p> <a href="/creer_compte"> Créer un compte </a> </p>
		</div>
	</body>
</html>

	"""

connection.exposed = True


# ============= DECONNEXION =============#
def deconnexion():
    cherrypy.session.pop("user", None)
    cherrypy.session.pop("role", None)
    raise cherrypy.HTTPRedirect("/")

deconnexion.exposed = True


# ============= Creation de compte =============#
def creer_compte(Profession=None, identifiant=None, Mot_de_passe=None):
    message = ""
    if Profession and identifiant and Mot_de_passe:
        Profession = int(Profession)
        baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password="nsi", database="PQCM02")
        cur = baseDeDonnees.cursor()
        cur.execute(
            "SELECT * from utilisateur WHERE nom_user = %s", (identifiant,)
        )
        result = cur.fetchall()
        if result:
            message = "<p style='color:red;'>Identifiant déjà pris</p>"
        else:
            mot_de_passe_hash = bcrypt.hashpw(Mot_de_passe.encode(), bcrypt.gensalt()).decode()
            cur.execute(
                "INSERT INTO utilisateur (nom_user,mdp_user,metier) VALUES (%s,%s,%s)",
                (identifiant, mot_de_passe_hash, Profession)
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
                    <h1>QCMauve</h1>
                    
                    """ + menu() + '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvPZL842vqhNJ6p5MsIx3rHYoefjOyZczXTg&s" style="transform: scale(2); margin: 120px;"> <br> <i>pour rejoindre le côté obscur veillez créer un compte</i>' + """
                    <div id="inter_co">  
                    <p style="text-decoration: underline">Créer un compte</p>
                        <form method="post" action="/creer_compte">
                            <select name="Profession">
                                <option value="1">Professeur</option>
                                <option value="0">Elève</option>
                            </select>
                            <input type="text" name="identifiant" placeholder="Identifiant"  required>
                            <input type="password" name="Mot_de_passe" placeholder="Mot de passe" minlength="8" required>
                        
                        <button type="submit">Valider</button>
                        </form>
                        
                        <p > <a href="/connection">Se connecter </a> </p>
                    </div>
                    """ + message + """
                </body>
            </html>"""


creer_compte.exposed = True

# =============Partie pour la mise en ligne du serveur=============#

# ip perso : 192.168.1.8
# ip lycée : 172.16.100.22

cherrypy.config.update({
    "server.socket_host": "192.168.1.8",
    "server.socket_port": 8083,
    "server.socket_pool": 5,
    "tools.sessions.on": True,
    "tools.encode.encoding": "utf-8",
    "tools.staticdir.on": True,
    "tools.staticdir.dir": os.path.join(os.path.dirname(__file__), "static_2")
})

# Monter le dossier static_2 sous /static pour servir les fichiers CSS/JS/images
static_dir = os.path.join(os.path.dirname(__file__), "static_2")
cherrypy.tree.mount(None, "/static", {'/': {'tools.staticdir.on': True, 'tools.staticdir.dir': static_dir}})

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
