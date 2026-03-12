
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";



DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nom_user` TINYTEXT,
  `mdp_user` TINYTEXT,
  `metier` int(1),
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=121 DEFAULT CHARSET=utf8;

INSERT INTO `utilisateur` (`id`,`nom_user`, `mdp_user`, `metier`) VALUES
(0,'Jules','mdp1',0),
(1,'Jb','mdp2',1); 


DROP TABLE IF EXISTS `notes`;
CREATE TABLE IF NOT EXISTS `notes` (
  `id_user` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `valeur` TINYINT,
  `matiere` TINYTEXT,
  `id_question` int(10),
  PRIMARY KEY (`id_user`)
) ENGINE=MyISAM AUTO_INCREMENT=121 DEFAULT CHARSET=utf8;

INSERT INTO `notes` (`id_user`,`valeur`, `matiere`, `id_question`) VALUES
(0,1,'histoire',0),
(1,0,'philosophie',1); 









DROP TABLE IF EXISTS `questions`;
CREATE TABLE IF NOT EXISTS `questions` (
  `id_question` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `question` TINYTEXT,
  `reponse1` TINYTEXT,
  `reponse2` TINYTEXT,
  `reponse3` TINYTEXT,
  `reponse4` TINYTEXT,
  `bonne_reponse` int(1),
  `matiere`  TINYTEXT,
  PRIMARY KEY (`id_question`)
) ENGINE=MyISAM AUTO_INCREMENT=121 DEFAULT CHARSET=utf8;

INSERT INTO `questions` (`id_question`,`question`, `reponse1`, `reponse2`,`reponse3`,`reponse4`,`bonne_reponse`,`matiere`) VALUES
(0,'capitale du Bahreïn ?','Doha','Dubaï','Manama','Riyad',3,'histoire'),
(1,'Quel philosophe critique la morale religieuse ?','Sextus Empiricus','Nietzsche','Mill','Karl Marx',2,'philosophie'); 




COMMIT;

