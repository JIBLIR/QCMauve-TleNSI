import cherrypy 
import os
import mysql.connector

#=============Partie pour le cryptage du mdp=============#
def pgcd(a,b):
	if a == b :return a
	elif a > b : return pgcd(a-b,b)
	else: return pgcd(a,b-a)

q = 17
p = 19
m = (p-1)*(q-1)
n = q * p
e = 2
while pgcd(e,m) != 1: 
	e += 1
d = 0
while (d*e) % m != 1:
	d += 1

def crypter(message):
    # crypte un nombre
	global e, n
	e1 = e
	texte_crypte = 1
	while e1 > 0:
		texte_crypte *= message
		texte_crypte %= n
		e1 -= 1
	return texte_crypte


def decrypter(texte_crypte):
    # decrypte un nombre
	global d, n
	d1 = d
	decrypte = 1
	while d1 > 0:
		decrypte *= texte_crypte
		decrypte %= n
		d1 -= 1
	return decrypte

#=============Site WEB=============#
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
				<li id="co"><a href="/connection">Se connecter</a></li>
            </ul>
        </div>  
        <p>Bonjour, vous voilà sur une page web où l'on peut reviser plusieures matiéres de différent classes.</p>
    </body>
</html>

	"""

index.exposed = True 

def seconde():
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
				<li id="co"><a href="/connection">Se connecter</a></li>
			</ul>
		</div>  
		<h1>Seconde</h1><br>
		<p>Questions en Maths</p>
			<input type="number" id="nb_ques_Maths_Snd" name="nb_ques_Maths_Snd" min="1" max="5" value="1"/>
			<button type="submit">Valider</button>
			<br>
		<p>Questions en Physique</p>
			<input type="number" id="nb_ques_Physique_Snd" name="nb_ques_Physique_Snd" min="1" max="5" value="1"/>
			<button type="submit">Valider</button>
			<br>
		<p>Questions en Autres</p>
			<input type="number" id="nb_ques_Autre_Snd" name="nb_ques_Autre_Snd" min="1" max="5" value="1"/>
			<button type="submit">Valider</button>
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
				<li id="co"><a href="/connection">Se connecter</a></li>
			</ul>
		</div>  
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
				<li id="co"><a href="/connection">Se connecter</a></li>
			</ul>
		</div>  
		<p>Terminale</p>
	</body>
</html>

	"""

terminale.exposed = True 

def connection(identifiant = None,Mot_de_passe = None):

	if identifiant and Mot_de_passe:
		mdp_cryp2 = crypter(Mot_de_passe)
		baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")
		cur = baseDeDonnees.cursor()
		requete = "SELECT * FROM utilisateur WHERE nom_user = %s AND mdp_user = %s"
		cur.execute(requete, (identifiant, mdp_cryp2))

		resultat = cur.fetchone()  # récupère 1 résultat

		if resultat:
			print("Connexion réussie ")
		else:
			print("Identifiant ou mot de passe incorrect ")

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
				<li id="co"><a href=/connection>Se connecter</a></li>
			</ul>
		</div>
		<div id="inter_co">  
			<p style="text-decoration: underline">Se connecter</p>
			<form method="post" action="/connection">
				<input type="text" name="identifiant" placeholder="Identifiant"  required>
				<input type="password" name="Mot_de_passe" placeholder="Mot de passe" required>
			<button type="submit">Valider</button>
			</form>
			<p> <a href=/creer_compte> Créer un compte </a> </p>
		</div>
	</body>
</html>

	"""

connection.exposed = True 

def creer_compte(Profession = None,identifiant = None,Mot_de_passe = None):

	if Profession and identifiant and Mot_de_passe :
		Profession = int(Profession)
		Mdp_cryp = crypter(Mot_de_passe)
		baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")
		cur = baseDeDonnees.cursor()
		cur.execute(
		"INSERT INTO utilisateur (nom_user,mdp_user,metier) VALUES (%s,%s,%s)",(identifiant,Mdp_cryp,Profession)
		)
		baseDeDonnees.commit()
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
				<li id="co"><a href=/connection>Se connecter</a></li>
			</ul>
		</div>
		<div id="inter_co">  
		<p style="text-decoration: underline">Créer un compte</p>
			<form method="post" action="/creation">
				<select name="Profesion">
					<option value="1">Profeseur</option>
					<option value="0">Elève</option>
				</select>
				<input type="text" name="identifiant" placeholder="Identifiant"  required>
				<input type="password" name="Mot_de_passe" placeholder="Mot de passe" minlength="16" required>
			
			<button type="submit">Valider</button>
			</form>
			<p > <a href=/connection >Se connecter </a> </p>
		</div>
	</body>
</html>

	"""

creer_compte.exposed = True 

#=============Partie lancage du serveur=============#
cherrypy.config.update({
	"server.socket_host"	:"172.16.100.22", 
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
cherrypy.tree.mount(connection, "/connection")
cherrypy.tree.mount(creer_compte, "/creer_compte")



cherrypy.engine.start()
cherrypy.engine.block()
