# importation des bibliotheques
import cherrypy
import os
import mysql.connector
import bcrypt  # bibliotheque pour le cryptage du mot de passe


# ============= Site WEB =============#

def ouvrir_connexion_bd():
    """Ouvre une connexion MySQL en utf8mb4. Cette fonction permet la stabilité en n'ayant pas de caractères spéciaux qui occasionnerait une gène pour l'utilisateur"""
    return mysql.connector.connect(
        host="localhost",
        user="nsi",
        password="nsi",
        database="P02QCM",
        charset="utf8mb4",
        use_unicode=True
    )

def menu():
    """Cree le menu de navigation selon le role de l'utilisateur."""
    # si l'utilisateur est professeur, on affiche les boutons professeurs
    if "role" in cherrypy.session and cherrypy.session["role"] == 1:
        bouton = '''
        <li><a href="/ajout_qcm">Ajout Qcm</a></li>
        <li><a href="/sup">Supprimer un Qcm</a></li>
        <li><a href="/stats">Staats</a></li>
        <li id="co"><a href="/deconnexion">Se déconnecter</a></li>
        '''
        statut = ' Accès Professeur'

    # si l'utilisateur est connecte comme eleve, on affiche les boutons eleves
    elif "user" in cherrypy.session:
        bouton = '''
        <li><a href="/stats">Stats</a></li>
        <li id="co"><a href="/deconnexion">Se déconnecter</a></li>
        '''
        statut = 'Accès Étudiant'

    # sinon on affiche le bouton de connexion
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
    """Affiche la page d'accueil du site."""
    # message different selon que l'utilisateur soit connecte ou non
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


def moteurqcm(reponse=None, matiere=None, classe=None, note=None):
    """Gere le deroulement du QCM, les reponses et la note."""
    # recuperation des informations de session si elles ne sont pas donnees
    if matiere is None:
        matiere = cherrypy.session.get('matiere', None)
    if classe is None:
        classe = cherrypy.session.get('classe', None)
    if note is None:
        note = cherrypy.session.get('note', 0)
    print(matiere, classe, note)
    cherrypy.session['matiere'] = matiere
    cherrypy.session['classe'] = classe
    cherrypy.session['note'] = note
    import mysql.connector

    # recuperation de l'index de la question actuelle
    index_question = cherrypy.session.get('index_question', 0)
    print(index_question)

    # connexion a la base de donnees
    baseDeDonnees = ouvrir_connexion_bd()
    curseur = baseDeDonnees.cursor()

    # si une classe et une matiere sont choisies, on peut lancer le qcm
    if classe is not None and matiere is not None:
        curseur.execute(f"select * from questions where classe = {classe} AND matiere = '{matiere}';")
        questions = curseur.fetchall()
        question = questions[(index_question)]

        # creation du formulaire de la question courante
        qcm = f""" {question[1]}
            <form method="post" action="/moteurqcm">
            <ol>
            <li> {question[2]} <input type="radio" value="1" name="reponse"  /> </li>
            <li> {question[3]} <input type="radio" value="2" name="reponse" /> </li>
            <li> {question[4]} <input type="radio" value="3" name="reponse" /> </li>
            <li> {question[5]} <input type="radio" value="4" name="reponse" /> </li>
            </ol>
            <button type="submit">Valider</button>

            </form>
            question {index_question + 1} sur {len(questions)} questions | {note}/{len(questions)}
            """

        if reponse is not None:

            # verification de la reponse choisie par l'utilisateur
            if str(reponse) == str(question[6]):
                index_question += 1
                cherrypy.session['note'] += 1
                qcm = f"bonne réponse, {question[int(question[6]) + 1]} "
            else:
                index_question += 1
                qcm = f"faux, la bonne réponse était {question[int(question[6]) + 1]} "

            note = cherrypy.session.get('note', 0)

            # si le qcm n'est pas fini, on propose la question suivante
            if index_question < len(questions):
                qcm += f"""
                <form method="post" action="/moteurqcm">
                <button type="submit">Question Suivante</button>
                </form>
                """

            else:
                # calcul du pourcentage final quand le qcm est termine
                pourcentage = (note / len(questions)) * 100
                qcm += f"<p>{pourcentage} % , Fin du QCM</p>"

                # si l'utilisateur est connecte, on enregistre ou met a jour sa note
                if "user" in cherrypy.session:
                    curseur.execute(f'SELECT id_user FROM notes WHERE matiere = "{matiere}" AND classe = {classe} AND id_user = (SELECT id FROM utilisateur WHERE nom_user = "{cherrypy.session["user"]}");')
                    resultat = curseur.fetchone()

                    # insertion si aucune note n'existe encore
                    if resultat is None:
                        curseur.execute(f'INSERT INTO notes VALUES ((SELECT id FROM utilisateur WHERE nom_user = "{cherrypy.session["user"]}"), {pourcentage}, "{matiere}", {classe});')
                    # mise a jour si une note existe deja
                    else:
                        curseur.execute(f'UPDATE notes SET valeur = {pourcentage} WHERE matiere = "{matiere}" AND classe = {classe} AND id_user = (SELECT id FROM utilisateur WHERE nom_user = "{cherrypy.session["user"]}");')

        # sauvegarde de l'index de question dans la session
        cherrypy.session['index_question'] = index_question
    # si aucune matiere n'est choisie, on n'affiche pas de qcm
    else:
        qcm = ""

    # fermeture de la connexion a la base de donnees
    curseur.close()
    baseDeDonnees.close()

    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
        <link rel="stylesheet" href="/static/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>QCMauve</h1>

		""" + menu() + qcm + """
    </body>
</html>
    """


moteurqcm.exposed = True


def seconde():
    """Affiche les matieres disponibles pour la classe de seconde."""
    import mysql.connector

    # initialisation des variables de session pour un nouveau qcm
    cherrypy.session['classe'] = 2
    cherrypy.session['note'] = 0
    cherrypy.session['index_question'] = 0

    # connexion a la base pour recuperer les matieres disponibles
    baseDeDonnees = ouvrir_connexion_bd()
    curseur = baseDeDonnees.cursor()

    curseur.execute('SELECT DISTINCT matiere from questions WHERE classe = 2;')
    matieres = curseur.fetchall()
    boutons = ""

    # creation des boutons radio pour chaque matiere
    for i in range(len(matieres)):
        print(matieres[i][0])
        matiere = matieres[i][0]
        boutons += f'<li> {matiere} <input type="radio" value="{matiere}" name="matiere"  /> </li>'

    # fermeture de la base de donnees
    curseur.close()
    baseDeDonnees.close()
    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
        <link rel="stylesheet" href="/static/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>QCMauve</h1>

		""" + menu() + f"""
        <form method="post" action="/moteurqcm">
    <ol>
    {boutons}
    </ol>
    <button type="submit">Valider</button>
    </form>
	</body>
</html>

	"""


seconde.exposed = True


def premiere():
    """Affiche les matieres disponibles pour la classe de premiere."""
    import mysql.connector

    # initialisation des variables de session pour un nouveau qcm
    cherrypy.session['classe'] = 1
    cherrypy.session['note'] = 0
    cherrypy.session['index_question'] = 0

    # connexion a la base pour recuperer les matieres disponibles
    baseDeDonnees = ouvrir_connexion_bd()
    curseur = baseDeDonnees.cursor()

    curseur.execute('SELECT DISTINCT matiere from questions WHERE classe = 1;')
    matieres = curseur.fetchall()
    boutons = ""

    # creation des boutons radio pour chaque matiere
    for i in range(len(matieres)):
        print(matieres[i][0])
        matiere = matieres[i][0]
        boutons += f'<li> {matiere} <input type="radio" value="{matiere}" name="matiere"  /> </li>'

    # fermeture de la base de donnees
    curseur.close()
    baseDeDonnees.close()
    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
        <link rel="stylesheet" href="/static/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>QCMauve</h1>

		""" + menu() + f"""
        <form method="post" action="/moteurqcm">
    <ol>
    {boutons}
    </ol>
    <button type="submit">Valider</button>
    </form>
	</body>
</html>

	"""


premiere.exposed = True


def terminale():
    """Affiche les matieres disponibles pour la classe de terminale."""
    import mysql.connector

    # initialisation des variables de session pour un nouveau qcm
    cherrypy.session['classe'] = 0
    cherrypy.session['note'] = 0
    cherrypy.session['index_question'] = 0

    # connexion a la base pour recuperer les matieres disponibles
    baseDeDonnees = ouvrir_connexion_bd()
    curseur = baseDeDonnees.cursor()

    curseur.execute('SELECT DISTINCT matiere from questions WHERE classe = 0;')
    matieres = curseur.fetchall()
    boutons = ""

    # creation des boutons radio pour chaque matiere
    for i in range(len(matieres)):
        print(matieres[i][0])
        matiere = matieres[i][0]
        boutons += f'<li> {matiere} <input type="radio" value="{matiere}" name="matiere"  /> </li>'

    # fermeture de la base de donnees
    curseur.close()
    baseDeDonnees.close()
    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
        <link rel="stylesheet" href="/static/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>QCMauve</h1>

		""" + menu() + f"""
        <form method="post" action="/moteurqcm">
    <ol>
    {boutons}
    </ol>
    <button type="submit">Valider</button>
    </form>
	</body>
</html>

	"""


terminale.exposed = True


# ============= Ajout de Qcm =============#

def ajout_qcm(question=None, rep1=None, rep2=None, rep3=None, rep4=None, bonne_rep=None, matiere=None, classe=None):
    """Permet au professeur d'ajouter une question de QCM."""
    # si l'utilisateur n'est pas connecte, il est redirige vers la connexion
    if "role" not in cherrypy.session:
        raise cherrypy.HTTPRedirect("/connection")

    # si l'utilisateur est eleve, il n'a pas acces a cette page
    if cherrypy.session["role"] == 0:
        raise cherrypy.HTTPRedirect("/")

    # si tous les champs sont remplis, on ajoute la question dans la base
    if rep1 and rep2 and rep3 and rep4 and question and classe:
        baseDeDonnees = ouvrir_connexion_bd()
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
    """Permet au professeur de rechercher puis supprimer un QCM."""
    # verification du droit d'acces a la page
    if "role" not in cherrypy.session:
        raise cherrypy.HTTPRedirect("/connection")

    if cherrypy.session["role"] == 0:
        raise cherrypy.HTTPRedirect("/")

    liste_questions = ""
    message = ""

    # si une recherche est faite, on affiche les questions correspondantes
    if question:
        baseDeDonnees = ouvrir_connexion_bd()
        cur = baseDeDonnees.cursor()
        cur.execute("SELECT id_question, question FROM questions WHERE question LIKE %s", ("%" + question + "%",))
        resultat = cur.fetchall()

        if resultat:
            # affichage de toutes les questions trouvees avec un lien de suppression
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

    # si un identifiant est donne, on supprime directement la question
    if id:
        baseDeDonnees = ouvrir_connexion_bd()
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
    """Authentifie un utilisateur et ouvre sa session."""
    message = ""

    # si les champs sont remplis, on tente la connexion
    if identifiant and Mot_de_passe:

        try:
            # connexion a la base de donnees
            baseDeDonnees = ouvrir_connexion_bd()

            cur = baseDeDonnees.cursor()

            cur.execute(
                "SELECT mdp_user, metier FROM utilisateur WHERE nom_user = %s", (identifiant,)
            )

            resultat = cur.fetchone()

            # si l'utilisateur existe, on verifie le mot de passe
            if resultat:
                mdp_stocke = resultat[0]
                metier = resultat[1]
                try:
                    # comparaison du mot de passe saisi avec le hash stocke
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
                # message si l'identifiant n'existe pas
                message = "<p style='color:red;'>Identifiants incorrects</p>"

            cur.close()
            baseDeDonnees.close()

        # message d'erreur si la base est inaccessible
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
            """ + message + """
			<p> <a href="/creer_compte"> Créer un compte </a> </p>
		</div>
	</body>
</html>

	"""


connection.exposed = True


# ============= DECONNEXION =============#

def deconnexion():
    """Deconnecte l'utilisateur courant et le redirige."""
    # suppression des informations de session
    cherrypy.session.pop("user", None)
    cherrypy.session.pop("role", None)
    raise cherrypy.HTTPRedirect("/")


deconnexion.exposed = True


# ============= Creation de compte =============#

def creer_compte(Profession=None, identifiant=None, Mot_de_passe=None):
    """Cree un nouveau compte utilisateur avec mot de passe hache."""
    message = ""

    # si tous les champs sont remplis, on cree le compte
    if Profession and identifiant and Mot_de_passe:
        Profession = int(Profession)
        baseDeDonnees = ouvrir_connexion_bd()
        cur = baseDeDonnees.cursor()
        cur.execute(
            "SELECT * from utilisateur WHERE nom_user = %s", (identifiant,)
        )
        result = cur.fetchall()

        # verification que l'identifiant n'est pas deja pris
        if result:
            message = "<p style='color:red;'>Identifiant déjà pris</p>"
        else:
            # hashage du mot de passe avant l'enregistrement
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


def stats():
    """Affiche les statistiques de l'utilisateur connecte."""
    # connexion a la base pour recuperer les notes de l'utilisateur
    baseDeDonnees = ouvrir_connexion_bd()
    curseur = baseDeDonnees.cursor()
    curseur.execute(f'SELECT valeur, matiere,classe from notes,utilisateur WHERE notes.id_user = utilisateur.id AND utilisateur.nom_user = "{cherrypy.session["user"]}";')
    stats = curseur.fetchall()
    baseDeDonnees.close()
    curseur.close()
    infos = ''

    # affichage des statistiques recuperees
    for i in range(len(stats)):
        print(stats)
        stat = stats[i]
        infos += f' {stat[0]} % | {stat[1]} | {stat[2]}  <br> _________________ <br>'
    return """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Mon site Web</title>
        <link rel="stylesheet" href="/static/style_projet_Bd_NSI.css">
	</head>
	<body>
		<h1>QCMauve</h1>

		""" + menu() + f"""
        <form method="post" action="/moteurqcm">
    <ol>
    {infos}
	</body>
</html>

	"""


stats.exposed = True


# ============= Partie pour la mise en ligne du serveur =============#

# ip perso : 192.168.1.8
# ip lycée : 172.16.100.22

# configuration principale du serveur cherrypy
cherrypy.config.update({
    "server.socket_host": "127.0.0.1",
    "server.socket_port": 8088,
    "server.socket_pool": 5,
    "tools.sessions.on": True,
    "tools.encode.encoding": "utf-8",
    "tools.staticdir.on": True,
    "tools.staticdir.dir": os.path.join(os.path.dirname(__file__), "static_2")
})

# montage du dossier static_2 pour servir les fichiers css, js et images
static_dir = os.path.join(os.path.dirname(__file__), "static_2")
cherrypy.tree.mount(None, "/static", {'/': {'tools.staticdir.on': True, 'tools.staticdir.dir': static_dir}})

# association des fonctions avec les routes du site
cherrypy.tree.mount(index, "/")
cherrypy.tree.mount(seconde, "/seconde")
cherrypy.tree.mount(premiere, "/premiere")
cherrypy.tree.mount(terminale, "/terminale")
cherrypy.tree.mount(ajout_qcm, "/ajout_qcm")
cherrypy.tree.mount(sup, "/sup")
cherrypy.tree.mount(connection, "/connection")
cherrypy.tree.mount(deconnexion, "/deconnexion")
cherrypy.tree.mount(creer_compte, "/creer_compte")
cherrypy.tree.mount(moteurqcm, "/moteurqcm")
cherrypy.tree.mount(stats, "/stats")

# lancement du serveur web
cherrypy.engine.start()
cherrypy.engine.block()
