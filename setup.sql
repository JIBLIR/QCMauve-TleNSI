SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

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
) ENGINE=MyISAM AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4;

INSERT INTO `utilisateur` (`id`, `nom_user`, `mdp_user`, `metier`) VALUES
(0, 'Jules', 'mdp1', 0),
(1, 'Jb', 'mdp2', 1);

DROP TABLE IF EXISTS `notes`;
CREATE TABLE IF NOT EXISTS `notes` (
  `id_user` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `valeur` DECIMAL(5,2),
  `matiere` VARCHAR(50),
  `classe` int(1),
  PRIMARY KEY (`id_user`, `matiere`, `classe`)
) ENGINE=MyISAM AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4;

INSERT INTO `notes` (`id_user`, `valeur`, `matiere`, `classe`) VALUES
(0, 1, 'histoire', 0),
(1, 0, 'philosophie', 1);

DROP TABLE IF EXISTS `questions`;
CREATE TABLE IF NOT EXISTS `questions` (
  `id_question` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `question` TINYTEXT,
  `reponse1` TINYTEXT,
  `reponse2` TINYTEXT,
  `reponse3` TINYTEXT,
  `reponse4` TINYTEXT,
  `bonne_reponse` int(1),
  `matiere` TINYTEXT,
  `classe` int(1) DEFAULT 2,
  PRIMARY KEY (`id_question`)
) ENGINE=MyISAM AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4;

INSERT INTO `questions` (`id_question`, `question`, `reponse1`, `reponse2`, `reponse3`, `reponse4`, `bonne_reponse`, `matiere`, `classe`) VALUES
(0, 'Quel événement marque le début symbolique de la Révolution française ?', 'La prise de la Bastille', 'La Révolution de 1848', 'La chute de Napoléon', 'La bataille de Waterloo', 1, 'histoire', 0),
(1, 'Qui a été le premier empereur des Français ?', 'Louis XVI', 'Napoléon Bonaparte', 'Charles de Gaulle', 'Henri IV', 2, 'histoire', 0),
(2, 'Quel roi est associé au château de Versailles ?', 'Louis XIII', 'Louis XIV', 'Louis XV', 'Louis XVI', 2, 'histoire', 0),
(3, 'Quelle date correspond à la prise de la Bastille ?', '14 juillet 1789', '4 août 1789', '21 janvier 1793', '18 brumaire an VIII', 1, 'histoire', 0),
(4, 'Qui était Jeanne d’Arc ?', 'Une reine', 'Une résistante française du XVe siècle', 'Une impératrice', 'Une philosophe', 2, 'histoire', 0),
(5, 'En quelle année a eu lieu la chute de l’Empire romain d’Occident ?', '1453', '476', '1492', '1789', 2, 'histoire', 1),
(6, 'Quel traité met fin à la Première Guerre mondiale ?', 'Le traité de Rome', 'Le traité de Versailles', 'Le traité d’Utrecht', 'Le traité de Westphalie', 2, 'histoire', 1),
(7, 'Quelle bataille de 732 arrête une avancée musulmane en Europe occidentale ?', 'Bataille de Poitiers', 'Bataille de Tours', 'Bataille de Roncevaux', 'Bataille de Covadonga', 2, 'histoire', 1),
(8, 'Qui a été le dernier roi de France ?', 'Louis XVI', 'Napoléon III', 'Louis-Philippe', 'Charles X', 3, 'histoire', 1),
(9, 'Quel événement marque la fin officielle de la Seconde Guerre mondiale en Europe ?', 'Pearl Harbor', 'Débarquement de Normandie', 'Capitulation de l’Allemagne', 'Bataille de Stalingrad', 3, 'histoire', 1),
(10, 'Quelle réforme religieuse majeure a été initiée par Martin Luther en 1517 ?', 'Concile de Trente', 'Affichage des 95 thèses', 'Édit de Nantes', 'Paix d’Augsbourg', 2, 'histoire', 2),
(11, 'Quel traité a mis fin à la guerre de Trente Ans en 1648 ?', 'Traité de Westphalie', 'Traité de Versailles', 'Traité d’Utrecht', 'Paix de Münster', 1, 'histoire', 2),
(12, 'Quel concept est absent de la Déclaration des droits de l’homme et du citoyen de 1789 ?', 'Liberté', 'Égalité', 'Fraternité', 'Sûreté', 3, 'histoire', 2),
(13, 'Quel philosophe des Lumières a écrit « Du contrat social » ?', 'Voltaire', 'Montesquieu', 'Rousseau', 'Diderot', 3, 'histoire', 2),
(14, 'En quelle année Christophe Colomb arrive-t-il en Amérique ?', '1492', '1515', '1789', '1914', 1, 'histoire', 2),
(15, 'Quelle est la capitale du Canada ?', 'Toronto', 'Ottawa', 'Montréal', 'Vancouver', 2, 'géographie', 0),
(16, 'Quel est le plus grand continent du monde ?', 'Asie', 'Afrique', 'Europe', 'Océanie', 1, 'géographie', 0),
(17, 'Quel fleuve traverse l’Égypte ?', 'Le Nil', 'Le Danube', 'Le Rhône', 'Le Tibre', 1, 'géographie', 0),
(18, 'Quel est le plus grand océan de la planète ?', 'Océan Atlantique', 'Océan Indien', 'Océan Pacifique', 'Océan Arctique', 3, 'géographie', 0),
(19, 'Quel désert couvre une grande partie du nord de l’Afrique ?', 'Le Sahara', 'Le Gobi', 'Le Kalahari', 'Le Namib', 1, 'géographie', 0),
(20, 'Quel est le plus grand pays du monde en superficie ?', 'Chine', 'Canada', 'Russie', 'États-Unis', 3, 'géographie', 1),
(21, 'Dans quel océan se trouve l’île de Madagascar ?', 'Océan Indien', 'Océan Pacifique', 'Océan Atlantique', 'Océan Arctique', 1, 'géographie', 1),
(22, 'Quel est le plus haut sommet d’Afrique ?', 'Kilimandjaro', 'Mont Kenya', 'Mont Toubkal', 'Mont Cameroun', 1, 'géographie', 1),
(23, 'Quelle est la plus longue chaîne de montagnes du monde ?', 'Andes', 'Himalaya', 'Rocheuses', 'Atlas', 1, 'géographie', 1),
(24, 'Quel pays d’Amérique latine n’a pas de littoral sur l’océan Pacifique ?', 'Brésil', 'Uruguay', 'Paraguay', 'Argentine', 3, 'géographie', 1),
(25, 'Quel est le seul pays de cette liste qui s’étend sur trois continents habités ?', 'Turquie', 'Russie', 'Égypte', 'Danemark', 2, 'géographie', 2),
(26, 'Quel est le point le plus bas de la surface terrestre accessible sans plongée ?', 'Mer Morte', 'Lac Assal', 'Vallée de la Mort', 'Dépression de Qattara', 1, 'géographie', 2),
(27, 'Quel pays possède le plus grand désert chaud du monde ?', 'Arabie Saoudite', 'Australie', 'Algérie', 'Égypte', 3, 'géographie', 2),
(28, 'Quel fleuve traverse le plus de pays au monde ?', 'Nil', 'Amazonas', 'Danube', 'Yangzi Jiang', 3, 'géographie', 2),
(29, 'Quelle ville est la capitale de l’Australie ?', 'Sydney', 'Melbourne', 'Canberra', 'Brisbane', 3, 'géographie', 2),
(30, 'Quel philosophe a écrit Le Discours de la méthode ?', 'Voltaire', 'Descartes', 'Sartre', 'Platon', 2, 'philosophie', 0),
(31, 'Quel philosophe est associé à la phrase « Dieu est mort » ?', 'Kant', 'Nietzsche', 'Rousseau', 'Aristote', 2, 'philosophie', 0),
(32, 'Quelle notion est centrale chez Kant ?', 'Le devoir', 'Le hasard', 'La mémoire', 'La peur', 1, 'philosophie', 0),
(33, 'Quel courant pense que l’expérience est la source principale de la connaissance ?', 'L’empirisme', 'Le stoïcisme', 'Le cynisme', 'Le relativisme', 1, 'philosophie', 0),
(34, 'Quel philosophe est l’auteur du Contrat social ?', 'Socrate', 'Montesquieu', 'Rousseau', 'Hume', 3, 'philosophie', 0),
(35, 'Quel philosophe critique la morale religieuse ?', 'Sextus Empiricus', 'Nietzsche', 'Mill', 'Karl Marx', 2, 'philosophie', 1),
(36, 'Quel philosophe grec est le maître de Platon ?', 'Aristote', 'Socrate', 'Épicure', 'Zénon', 2, 'philosophie', 1),
(37, 'Quel courant philosophique cherche le bonheur par la maîtrise de soi ?', 'Stoïcisme', 'Empirisme', 'Rationalisme', 'Matérialisme', 1, 'philosophie', 1),
(38, 'Quel philosophe est connu pour le doute méthodique ?', 'Descartes', 'Spinoza', 'Hobbes', 'Bergson', 1, 'philosophie', 1),
(39, 'Quelle branche de la philosophie étudie la morale ?', 'Logique', 'Éthique', 'Métaphysique', 'Esthétique', 2, 'philosophie', 1),
(40, 'Quel philosophe a écrit La République ?', 'Platon', 'Sartre', 'Rousseau', 'Hegel', 1, 'philosophie', 2),
(41, 'Quelle notion désigne la capacité à choisir librement ?', 'Déterminisme', 'Libre arbitre', 'Contradiction', 'Mémoire', 2, 'philosophie', 2),
(42, 'Quel philosophe est associé à l’existentialisme ?', 'Sartre', 'Épicure', 'Kant', 'Locke', 1, 'philosophie', 2),
(43, 'Quel terme désigne une idée acceptée sans preuve dans un raisonnement ?', 'Axiome', 'Opinion', 'Préjugé', 'Syllogisme', 1, 'philosophie', 2),
(44, 'Quelle discipline étudie les règles du raisonnement correct ?', 'Éthique', 'Logique', 'Politique', 'Esthétique', 2, 'philosophie', 2),
(45, 'Comment appelle-t-on un récit écrit en vers ?', 'Un poème', 'Une maxime', 'Un discours', 'Une tragédie', 1, 'français', 0),
(46, 'Quelle figure de style repose sur une comparaison implicite ?', 'L’hyperbole', 'La métaphore', 'L’euphémisme', 'L’antithèse', 2, 'français', 0),
(47, 'Comment s’appelle le fait qu’un personnage parle seul sur scène ?', 'Un dialogue', 'Une tirade', 'Un monologue', 'Un aparté', 3, 'français', 0),
(48, 'Quel mot est l’antonyme de « obscur » ?', 'Clair', 'Froid', 'Lourd', 'Vieux', 1, 'français', 0),
(49, 'Quel type de texte raconte des événements avec un narrateur ?', 'Argumentatif', 'Descriptif', 'Narratif', 'Injonctif', 3, 'français', 0),
(50, 'Quelle figure de style exagère une idée ?', 'Hyperbole', 'Métaphore', 'Anaphore', 'Ellipse', 1, 'français', 1),
(51, 'Quel temps exprime souvent une action passée et terminée ?', 'Présent', 'Futur simple', 'Passé composé', 'Conditionnel', 3, 'français', 1),
(52, 'Comment appelle-t-on deux mots de sens contraire ?', 'Synonymes', 'Antonymes', 'Homonymes', 'Paronymes', 2, 'français', 1),
(53, 'Quel genre littéraire met souvent en scène des personnages sur scène ?', 'Théâtre', 'Roman', 'Essai', 'Article', 1, 'français', 1),
(54, 'Quel signe termine une phrase interrogative ?', 'Point', 'Virgule', 'Point d’interrogation', 'Deux-points', 3, 'français', 1),
(55, 'Quel auteur a écrit Les Misérables ?', 'Victor Hugo', 'Molière', 'Racine', 'Zola', 1, 'français', 2),
(56, 'Quelle figure répète un même mot en début de phrase ?', 'Anaphore', 'Antithèse', 'Métaphore', 'Périphrase', 1, 'français', 2),
(57, 'Comment appelle-t-on le narrateur qui dit « je » ?', 'Narrateur externe', 'Narrateur interne', 'Auteur', 'Lecteur', 2, 'français', 2),
(58, 'Quel mouvement littéraire valorise les sentiments au XIXe siècle ?', 'Romantisme', 'Classicisme', 'Naturalisme', 'Humanisme', 1, 'français', 2),
(59, 'Quel registre cherche à faire rire ?', 'Comique', 'Tragique', 'Lyrique', 'Épique', 1, 'français', 2),
(60, 'Combien font 7 × 8 ?', '54', '56', '48', '64', 2, 'mathématiques', 0),
(61, 'Combien font 12 ÷ 3 + 4 ?', '8', '6', '10', '4', 1, 'mathématiques', 0),
(62, 'Quelle est l’aire d’un rectangle de 5 cm sur 3 cm ?', '8 cm²', '12 cm²', '15 cm²', '18 cm²', 3, 'mathématiques', 0),
(63, 'Quelle est la racine carrée de 81 ?', '7', '8', '10', '9', 4, 'mathématiques', 0),
(64, 'Combien font 15 - 7 ?', '6', '8', '9', '7', 2, 'mathématiques', 0),
(65, 'Combien vaut 3² ?', '6', '9', '12', '8', 2, 'mathématiques', 1),
(66, 'Quel nombre est un nombre premier ?', '9', '15', '17', '21', 3, 'mathématiques', 1),
(67, 'Combien font 25 % de 80 ?', '10', '20', '25', '40', 2, 'mathématiques', 1),
(68, 'Quelle fraction est égale à 0,5 ?', '1/2', '1/3', '2/3', '3/4', 1, 'mathématiques', 1),
(69, 'Quel est le périmètre d’un carré de côté 4 cm ?', '8 cm', '12 cm', '16 cm', '20 cm', 3, 'mathématiques', 1),
(70, 'Quelle est la solution de x + 5 = 12 ?', '5', '6', '7', '8', 3, 'mathématiques', 2),
(71, 'Quel est le résultat de 2 × (3 + 4) ?', '10', '14', '20', '24', 2, 'mathématiques', 2),
(72, 'Quelle est la valeur de π arrondie au centième ?', '3,12', '3,14', '3,16', '3,18', 2, 'mathématiques', 2),
(73, 'Combien font 10³ ?', '30', '100', '1000', '10000', 3, 'mathématiques', 2),
(74, 'Quelle droite coupe un angle en deux angles égaux ?', 'Médiatrice', 'Bissectrice', 'Tangente', 'Sécante', 2, 'mathématiques', 2),
(75, 'Quel est le symbole chimique de l’eau ?', 'H2O', 'CO2', 'NaCl', 'O2', 1, 'sciences', 0),
(76, 'Quelle planète est la plus proche du Soleil ?', 'Vénus', 'Mercure', 'Mars', 'Terre', 2, 'sciences', 0),
(77, 'Quel organe pompe le sang dans le corps humain ?', 'Le foie', 'Le cerveau', 'Le cœur', 'Les poumons', 3, 'sciences', 0),
(78, 'Quel pigment permet aux plantes de capter la lumière ?', 'La chlorophylle', 'L’hémoglobine', 'La kératine', 'La mélanine', 1, 'sciences', 0),
(79, 'Quel gaz les êtres humains utilisent principalement pour respirer ?', 'Oxygène', 'Azote', 'Dioxyde de carbone', 'Hydrogène', 1, 'sciences', 0),
(80, 'Quel gaz est rejeté par les humains lors de l’expiration ?', 'Oxygène', 'Hydrogène', 'Dioxyde de carbone', 'Hélium', 3, 'sciences', 1),
(81, 'Quel état de la matière a une forme propre ?', 'Liquide', 'Gaz', 'Solide', 'Plasma', 3, 'sciences', 1),
(82, 'Quelle force attire les objets vers la Terre ?', 'Électricité', 'Gravité', 'Magnétisme', 'Frottement', 2, 'sciences', 1),
(83, 'Quel appareil mesure la température ?', 'Baromètre', 'Thermomètre', 'Anémomètre', 'Voltmètre', 2, 'sciences', 1),
(84, 'Quel astre est une étoile ?', 'La Lune', 'Mars', 'Le Soleil', 'Vénus', 3, 'sciences', 1),
(85, 'Quelle molécule porte l’information génétique ?', 'ADN', 'Glucose', 'Eau', 'Protéine', 1, 'sciences', 2),
(86, 'Quel phénomène transforme un liquide en gaz ?', 'Fusion', 'Solidification', 'Évaporation', 'Condensation', 3, 'sciences', 2),
(87, 'Quelle particule porte une charge négative ?', 'Proton', 'Neutron', 'Électron', 'Noyau', 3, 'sciences', 2),
(88, 'Quel système du corps humain permet les échanges gazeux ?', 'Système digestif', 'Système respiratoire', 'Système nerveux', 'Système osseux', 2, 'sciences', 2),
(89, 'Quelle énergie provient du Soleil ?', 'Énergie solaire', 'Énergie nucléaire', 'Énergie fossile', 'Énergie hydraulique', 1, 'sciences', 2);

COMMIT;
