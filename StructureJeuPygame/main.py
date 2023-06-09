# 1) Comme n'importe quel module ou bibliothèque que l'on utilise dans un programme Python, il faut importer Pygame
# import pygame


# En tout début de programme, il s'agit d'initialiser Pygame en écrivant la ligne suivante :
# pygame.init()


# 2) Affichage de la fenêtre :
# Il  faut réfléchir au périmètre physique du jeu et donc très rapidement définir la taille de la fenêtre de jeu.
# Ainsi, on définit grâce à la fonction set_mode, une fenêtre de 600 pixels de largeur sur 400 pixels de hauteur.
# On se propose également d'inscrire un titre dans la fenêtre grâce à la fonction set_caption.
# FENETRE = pygame.display.set_mode((600, 400))
# pygame.display.set_caption("Ma fenêtre")
# A noter que l'écriture ((600, 400)) signifie que l'on passe un tuple en paramètre.


# 3) Le tuple size de set_mode :
# Un tuple en langage Python correspond à une liste, mais avec la spécificité que cette liste n'est pas modifiable.
# Prenons exemple de création d'un tuple pour illustrer la syntaxe à utiliser.
# tuple = ('A', 'B', 'C', 'D')
# Le tuple size permet de définir la largeur et la hauteur de la fenêtre de jeu, en l'occurence 600 pixels de largeur sur 400 pixels de hauteur.
# On a donc un tuple défini ainsi :
# size = (600, 400)


# 4) Le paramètre flags de set_mode :
# Le paramètre flags permet de définir un ou plusieurs comportements, car ils sont combinables.
# Les valeurs principales qui sont utilisables sont :
# pygame.FULLSCREEN
# ppygame.DOUBLEBUF
# ppygame.HWSURFACE
# pygame.OPENGL
# pygame.RESIZABLE
# pygame.NOFRAME
# Ainsi, si nous voulons un affichage en plein écran par défaut (pygame.FULLSCREEN)
# Et que les dimensions de la fenêtre soient modifiables par la personne utilisant le programme (pygame.RESIZABLE), nous allons écrire flags ainsi :
# flags = pygame.FULLSCREEN | pygame.RESIZABLE
# Le code du programme peut alors ressembler à cela :
# import pygame
# pygame.init()
# size = (600, 400)
# flags = pygame.FULLSCREEN | pygame.RESIZABLE
# FENETRE = pygame.display.set_mode(size, flags)
# pygame.display.set_caption("Ma fenêtre")


# 5) Rappels concernant la boucle de jeu :
# Une boucle de jeu (game loop) est une boucle infinie qui s'interrompra grâce à l'atteinte de certains critères et qui schématiquement effectue les tâches suivantes à chaque itération.
# 1. Vérifier que les conditions d'arrêt ne sont pas atteintes, auquel cas, interrompre la boucle.
# 2. Mettre à jour les ressources nécessaires pour l'itération courante.
# 3. Obtenir les entrées soit issues du système soit issues de l'interaction avec le joueur.
# 4. Mettre à jour l'ensemble des entités qui caractérisent le jeu.
# 5. Rafraîchir l'écran.


# 6) Les surfaces Pygame :
# Une surface se crée de différentes manières, selon le type de surfaces que l'on désire afficher :
# - image.load(), quand il s'agit d'une image.
# - font.render(), quand il s'agit d'afficher du texte.
# - pygame.Surface(), pour une surface qui n'a rien de spécial à la création.
# - pygame.display.set_mode(), pour la fenêtre de jeu, qui est également une surface (un peu particulière).
# On peut d'ores et déjà citer blit qui permet de déplacer une surface de type image, et fill qui permet de remplir une surface avec une couleur de fond donnée


# 7) La fenêtre de jeu, une surface particulière :
# La notion de surface inclut également la fenêtre du jeu elle-même, précédemment créée.
# En effet, quand on écrit la ligne suivante, on crée en définitive une surface.
# fenetre = pygame.display.set_mode((400, 400))
# On crée finalement la surface au sens de Pygame, qui représente le périmètre du jeu lui-même.
# C'est ce que l'on appelle parfois la fenêtre d'affichage.
# Cette super-surface en quelque sorte, ou en tout cas la surface originelle, est forcèment unique.


# 8) Exemple de manipulation d'une surface :
# import pygame
# pygame.init()
# pygame.display.set_caption(u'Surface')
# fenetre = pygame.display.set_mode((400, 400))

# bleu = (0, 0, 255)
# bleu_surface = pygame.Surface((400, 400))
# bleu_surface.fill(bleu)
# fenetre.blit(bleu_surface, (0, 0))

# pygame.display.flip()

# while true:
# event = pygame.event.wait()
# if event.type == pygame.QUIT:
# break

# pygame.quit()
# Ce code permet de colorer en bleu le fond de la fenêtre affichée.

# On définit une surface qui correspond à la taille de la fenêtre.
# bleu_surface = pygame.Surface((400, 400))

# On la colorie en bleu.
# bleu_surface.fill(bleu)

# On la positionne en coordonnées (0,0), donc à l'angle supérieur gauche de la fenêtre affichée.
# fenetre.blit(bleu_surface, (0, 0))

# On met à jour l'affichage de la fenêtre.
# pygame.display.flip()

# On ne quitte la fenêtre du jeu que si l'utilisateur réalise une action en conséquence prise en charge par le code suivant.
# while true:
# event = pygame.event.wait()
# if event.type == pygame.QUIT:
# break
# pygame.quit()


# 9) Manipulation de la surface :
# On veut colorer le fond de la fenêtre.
# On reprend donc dans la ligne suivante les dimensions largeur et hauteur de la fenêtre elle-même.
# bleu_surface = pygame.Surface((400, 400))

# On aurait pu utiliser la fonction get_size en remplaçant la ligne précédente par celle qui suit :
# FOND = pygame.Surface(fenetre.get_size())


# 10) Surface ou copie de surface ? :
# Dans cet exemple, on a modifié directement la couleur de fond correspondant à la surface relative à la fenêtre de jeu.
# Mais on aurait pu tout autant colorer une copie de cette dernière, copie réalisée à l'aide de la fonction convert.
# bleu_surface = pygame.Surface((400, 400))
# bleu_surface = bleu_surface.convert()
# bleu_surface.fill(bleu)

# C'est le rôle de la ligne utilisant convert que de justement faire une copie de la surface et de ne pas travailler directement sur la première instance de Surface.
# La surface issue de l'appel de convert est relative à l'espace colorimétrique et donc à la manière d'enregistrer pour chaque pixel la couleur associée.
# Ceci est particulièrement vrai pour le chargement d'image (fonction pygame.image.load) :
# Il est en effet une bonne pratique d'appeler systématiquement convert lors du chargement d'une image.
# Il est donc préférable, en termes de performances de jeu, d'écrire ceci :
# surfaceImage = pygame.image.load("MonImage.jpg").convert()
# Plutôt que d'écrire cela :
# surfaceImage = pygame.image.load("MonImage.jpg")


# 11) Coloration de la surface :
# On colore la surface avec la couleur bleue.
# bleu_surface.fill(bleu)
# On utilise la fonction fill pour << remplir >> une surface d'une couleur donnée.


# 12) Gestion des couleurs :
# La gestion des couleurs est une problématique relative aux surfaces dont on cherche parfois à colorer l'intérieur.

# Si on reprend ce fragment de code :
# bleu = (0, 0, 255)
# bleu_surface.fill(bleu)

# On voit qu'une couleur est définie par un triplet de trois grandeurs numériques.
# Chacune de ces grandeurs est un entier compris entre 0 et 255, ce qui fait 256 valeurs possibles.
# Ce système de codification se nomme codage RGB (Red Green Blue, Rouge - Vert - Bleu).
# Chaque composante du triplet étant en effet une déclinaison respective du rouge, du vert et du bleu.

# Ainsi :
# - (0,0,0) correspond au noir.
# - (255,255,255) correspond au blanc.
# - (255,0,0) correspond au rouge primaire.
# - (0,255,0) correspond au vert primaire.
# - (0,0,255) correspond au bleu primaire.


# 13) Système de coordonnées :
# On considère un repère orthonormé dont l'origine (0,0) est le point supérieur gauche de la fenêtre de jeu.
# L'axe horizontal x est l'axe orienté de gauche à droite.
# L'axe vertical y est lui orienté du haut vers le bas.
# Le positionnement des points supérieurs gauches des rectangles se fait grâce à la fonction blit.
# Le rafraîchissement de la fenêtre et donc l'affichage actualisé des surfaces se réalisent grâce à la fonction flip.


# 14) Gestion du temps :
# Ce module offre plusieurs fonctions qui permettent de chronométrer la session en cours (depuis le init) ou de faire une pause dans l'exécution par exemple.
# On utilise pour cela les deux fonctions suivantes :

# pygame.time.get_ticks
# pygame.time.wait ou pygame.time.delay

# Le module pygame.time inclut également un objet Clock qui permet d'aller plus loin dans la gestion du temps.
# On remarque au passage qu'en termes de typographie le nommage des fonctions en Pygame commence par une minuscule.
# Le nommage des objets (comme Surface ou Clock) commence lui par une majuscule.
# Un bon moyen de savoir en un coup d'oeil à quoi on a affaire.
# Ainsi, la ligne suivante insérée dans une boucle de jeu garantit de ne jamais aller plus << vite >> que 50 images par seconde.

# Clock.tick(50)

# Quelle que soit la plateforme sur laquelle vous programmez, la vitesse d'affichage sera forcément supérieure à 30 images par seconde, ce qui constitue un minimum.
# La fonction tick implémente la fonction SDL nommée SDL_Delay.
# Cette dernière n'est pas forcément présente sur toutes les plateformes.
# Auquel cas, tick est rendue inopérante.


# 15) Gestion des évènements dans Pygame :


# 16) La fonction pygame.event.get :
# Cette fonction permet d'obtenir tous les évènements en attente de traitement et qui sont disponibles dans une file d'attente dédiée.
# S'il n'y en a aucun, on obtient alors une collection vide.
# Cette réponse sous forme de collection justifie que l'on utilise en général une boucle for pour parcourir tous les évènements de la collection obtenue en appelant la fonction get.
# Par exemple :

# for event in pygame.event.get():
# if event.type == pygame.KEYDOWN:
# if event.key == pygame.K_ESCAPE:
# ARRET_JEU = True


# 17) La fonction pygame.event.wait :
# Une alternative à l'usage de get est d'utiliser wait.
# Cette fonction attend qu'un évènement survienne, et dès que celui-ci arrive, il est mis à disposition.

# for event in pygame.event.get():
# if event.type == pygame.QUIT :
# sys.exit()


# 18) La fonction pygame.event.poll :
# La fonction poll retourne un seul des évènements qui sont dans la file d'attente.
# Son usage est nettement plus fréquent que celui de get ou de wait.


# 19) Un exemple : le carré qui rebondit :
# On reprend le petit programme précédent en faisant du rectangle rouge un carré rouge.
# Surtout, on décide de déplacer ce carré latéralement (horizontalement) en le faisant rebondir sur les bords gauche et droit.
# On veut maîtriser la vitesse de défilement et on veut être sûr de ne pas aller plus vite que 50 images par seconde.

# clock.tick(50)

# Par ailleurs, on veut pouvoir quitter la simulation quand on le veut (pour cela, on utilise wait).

# for event in pygame.event.get():
# if event.type == pygame.QUIT:
# sys.exit()

















































