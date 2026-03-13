import cherrypy 
import os
import mysql.connector

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
        <h1>Site pour passion</h1>

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
        <h1>Site pour passion</h1>

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
        <p>Seconde</p>
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
        <h1>Site pour passion</h1>

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
        <h1>Site pour passion</h1>

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

def connection():


	return """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Mon site Web</title>
        <link rel="stylesheet" href="/style_projet_Bd_NSI.css">
    </head>
    <body>
        <h1>Site pour passion</h1>

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
                <input type="text" name="identifiant" placeholder="Identifiant" required>
		    	<input type="text" name="Mot de passe" placeholder="Mot de passe" required>
            <button type="submit">Valider</button>
		    </form>
		    <p > <a href=/créer_compte >Créer un compte </a> </p>
		</div>
    </body>
</html>

	"""

connection.exposed = True 

def creer_compte(Profession = None,identifiant = None,Mot_de_passe = None):

	if Profession and identifiant and Mot_de_passe :
		Profession = int(Profession)
		baseDeDonnees = mysql.connector.connect(host="localhost", user='nsi', password = "nsi", database="P02QCM")
		cur = baseDeDonnees.cursor()
		cur.execute(
		"INSERT INTO utilisateur (nom_user,mdp_user,metier) VALUES (?,?,?)",(identifiant,Mot_de_passe,Profession)
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
cherrypy.tree.mount(connection, "/connection")
cherrypy.tree.mount(creer_compte, "/creer_compte")

cherrypy.engine.start()
cherrypy.engine.block()
