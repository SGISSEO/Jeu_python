# 1) La fenêtre du jeu :

# Créer la fenêtre du jeu est la première étape. Il s'agit de la fenêtre qui accueille les éléments graphiques qui composent le jeu.

# On commence par importer Pygame.

import pygame
from random import *

# Puis on initialise Pygame.

pygame.init()

# Les deux lignes précédentes sont systématiquement présentes dès lors que l'on utilise Pygame.

# Définissons maintenant les dimensions de la fenêtre.

HAUTEUR_FENETRE = 600
LARGEUR_FENETRE = 600

# Puis nous définissons la couleur de fond de la fenêtre.

COULEUR_FOND = (255, 255, 255)

# Et enfin, nous utilisons la commande d'affichage de la fenêtre.

ECRAN = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))

# Si vous lancez le programme, la fenêtre du jeu s'affiche avec un fond blanc.
# Aucune indication sur la durée de l'affichage n'est apportée, on la voit donc s'ouvrir et se fermer le temps d'une fraction de seconde.

# 2) La boucle du jeu :

# Pour définir la boucle du jeu, nous commençons par définir un booléen : si sa valeur est True, la boucle se poursuit, elle s'interrompt sinon.

ARRET_JEU = False

# La fonction pygame.event.get()permet d'intercepter tous les évènements entrants notamment depuis le clavier, la souris, etc.
# Si on appuie sur la touche [Esc], alors le jeu est interrompu.Ce ci est permis en utilisant les évènements du clavier suivants :
# touche appuyée (pygame.KEYDOWN) et touche [Esc] ou  (Echap] (pygame.K_ESCAPE).

# On définit donc ainsi la boucle de jeu :

while not ARRET_JEU:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print("EVENT.TYPE: " + event.type.__str__())
            if event.key == pygame.K_ESCAPE:
                ARRET_JEU = True

# La fenêtre s'affiche et l'affichage s'interrompt dès qu'on appuie sur [Esc].

# 3) Le système de coordonnées Pygame :

# En Python/Pygame, mais finalement en conception graphique informatique en général, le système de coordonnées est le suivant :

# - L'écran est muni d'un système de coordonnées orthonormé.
# - L'origine du repère, le point (0,0), est le point supérieur gauche de l'écran.
# - L'axe des y est l'axe vertical orienté vers le bas.
# - L'axe des x est l'axe horizontal orienté vers la droite.

# 4) Les variables du jeu :

# Nous allons avoir des variables liées à la fusée que le joueur déplace.
# Nous allons avoir des variables liées aux deux planètes qui << tombent >> du ciel.
# Et nous allons avoir des variables plus transversales qui servent notamment à compter les points.

# Variables FUSEE :

XX_FUSEE = 210
YY_FUSEE = 300
LARGEUR_FUSEE = 88
HAUTEUR_FUSEE = 175
MOUVEMENT_XX_FUSEE = 0

# Variables PLANETES :

XX_PLANETE = randint(30, 130)
YY_PLANETE = 20
LARGEUR_PLANETE = 111
HAUTEUR_PLANETE = 80
XX_ENTRE_PLANETES = 350
YY_ENTRE_PLANETE = 125
VITESSE_PLANETES = 3

# Points et divers :

POINTS = 0
FONT = pygame.font.Font(None, 24)
SCORE = FONT.render("0 points", 1, (255, 0, 0))

# IMAGES :

IMG_FUSEE = pygame.image.load("FUSEE.png")
IMG_PLANETE_GAUCHE = pygame.image.load("PLANETE.png")
IMG_PLANETE_DROITE = pygame.image.load("PLANETE.png")

# 5) Les variables liées à la fusée :

# On spécifie que l'image de la fusée a son angle supérieur gauche positionné à un point de coordonnées initiales (XX_FUSEE, YY_FUSEE).
# Sachant que l'image elle-même a une taille fixe de LARGEUR_FUSEE sur HAUTEUR_FUSEE.
# Le joueur déplace la position de la fusée, donc la coordonnée XX_FUSEE varie (YY_FUSEE reste constante, car le déplacement s'effectue latéralement, de gauche à droite, uniquement).
# Enfin, MOUVEMENT_XX_FUSEE correspond au déplacement latéral de la fusée à chaque itération de la boucle de jeu.
# Sa valeur est soit négative (déplacement à gauche), soit positive (déplacement à droite).

# 6) Les variables liées aux deux planètes qui << tombent >> :

# De manière relativement similaire, on définit le coin gauche de la première image de planète.
# Il faut que sa position initiale diffère à chaque itération pour créer un effet de surprise.
# C'est pour cela que l'on met de l'aléatoire dans sa position en choisissant au hazard son abscisse.
# On veut simplement que cette valeur selon l'axe des x soit comprise entre 30 et 130.
# Un tel tirage aléatoire s'écrit grâce à la fonction Python randint.
# randint étant une fonction du module random, il faut donc importer préalablement le module random dans le code.

# OUTRE XX_PLANETE, YY_PLANETE est valorisée.
# Comme pour la fusée, on définit une largeur et une hauteur d'image de chaque planète : LARGEUR_PLANETE et HAUTEUR_PLANETE.
# On peut ensuite facilement définir la position de la seconde planète grâce à XX_ENTRE_PLANETES et YY_ENTRE_PLANETES.
# Enfin, la vitesse de déplacement vertical des planètes est fixée à 5 au travers de la variable VITESSE_PLANETES.

# 7) Les variables relatives au comptage des points :

# On définit trois autres variables.
# Une variable entière POINTS contenant le nombre de points obtenus.
# Une variable FONT qui définit la police de caractères utilisée, en particulier pour l'affichage en temps réel du nombre de points grâce à la variable SCORE.

# 8) Les variables relatives aux images :

# Ici il s'agit de charger les images adéquates pour chacun des trois objets graphiques, à savoir la fusée et les deux planètes qui tombent.
# Une seule image est utilisée pour les deux objets graphiques de planètes.
# On aurait bien sûr pu prendre deux images différentes pour les deux planètes.

# 9) Les déplacements de la fusée :

# Pour simplifier au plus la mobilité de la fusée, nous faisons le choix suivant :
# - Quand on appuie sur la touche [Flèche à droite] du clavier, la fusée va à droite.
# - Quand on appuie sur la touche [Flèche à gauche] du clavier, la fusée va à gauche.
# Il faut donc détecter l'évènement clavier, tester que cela concerne la touche [Flèche à droite], et vérifier qu'il s'agit d'un appui sur la touche ou une fin d'appui sur la touche.
# En pseudo-code, on a la séquence suivante :
# - On teste l'évènement courant.
# - S'il s'agit d'un appui d'une touche et si cette touche est la touche [Flèche à droite], alors on valorise MOUVEMENT_XX_FUSEE à la valeur 4.
# - S'il s'agit d'un relâchement de touche [Flèche à droite], alors on valorise MOUVEMENT_XX_FUSEE à la valeur -4.

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            MOUVEMENT_XX_FUSEE = 4
    elif event.type == pygame.KEYUP:
        MOUVEMENT_XX_FUSEE = -4

# Il s'agit maintenant de modifier l'affichage de la fusée en fonction du traitement précédent.
# On commence par mettre à jour la coordonnée en x de la fusée :

XX_FUSEE = XX_FUSEE + MOUVEMENT_XX_FUSEE

# Puis on signifie à Pygame d'afficher la fusée en fonction des coordonnées mises à jour:

ECRAN.blit(IMG_FUSEE, (XX_FUSEE, YY_FUSEE))

# Dans la boucle de jeu, on signifie enfin à Pygame de mettre à jour tous les objets graphiques susceptibles d'avoir changé au cours de l'itération courante, ce qui implique évidemment la fusée :

pygame.display.update()

# 10) Les déplacements des planètes :

# L'idée est ici d'afficher deux planètes en haut de la fenêtre : celles-ci descendent et il s'agit donc pour la fusée de les éviter.
# En pseudo-code, on a la séquence suivante au sein de la boucle de jeu :
# - On affiche les deux planètes aux coordonnées respectives suivantes (XX_PLANETE, YY_PLANETE) et (XX_PLANETE + XX_ENTRE_PLANETES, YY_ENTRE_PLANETES).
# - On met à jour XX_PLANETE en lui ajoutant VITESSE_PLANETES.
# - On vérifie si le bas de la fenêtre est atteint :
# - Si oui, on réinitialise XX_PLANETE et YY_PLANETE pour qu'à la prochaine itération, on reparte d'en haut.
# - On met éventuellement à jour le score.

ECRAN.blit(IMG_PLANETE_GAUCHE, (XX_PLANETE, YY_PLANETE))
ECRAN.blit(IMG_PLANETE_DROITE, (XX_PLANETE + XX_ENTRE_PLANETES, YY_PLANETE + YY_ENTRE_PLANETE))
YY_PLANETE = YY_PLANETE + VITESSE_PLANETES
if YY_PLANETE > HAUTEUR_FENETRE:
    XX_PLANETE = randint(55, 150)
    YY_PLANETE = 25
POINTS = POINTS + 1
SCORE = FONT.render(str(POINTS) + " points", 1, (255, 0, 0))

# A noter que le test qui consiste à vérifier que la première planète n'a pas encore atteint le bas de la fenêtre est déjà ce qu'on appelle la gestion des collisions.
# En l'espèce, on vérifie si la planète a atteint le bas de la fenêtre, et le cas échéant, on gère la situation en repositionnant ladite planète en haut de la fenêtre.

# 11) Les collisions :

# On a déjà géré une collision : celle de la première planète avec les bord inférieur de la fenêtre.
# Nous devons également gérer les deux situations de collisions suivantes :
# 1. Quand la fusée atteint le bord gauche de la fenêtre ou le bord droit de la fenêtre.
# 2. Quand la fusée rencontre une des deux planètes, ce qui est justement l'enjeu de ce petit jeu vidéo.
# Le premier point est assuré par la gestion des collisions suivante :

if XX_FUSEE < -10 or XX_FUSEE > LARGEUR_FENETRE:
    ARRET_JEU = True

# Le second point est assuré par le code suivant dans lequel on teste la rencontre de la fusée avec chacune des deux planètes :

# PLANETE GAUCHE COLLISION :

POINT_BAS_DROIT_PREMIERE_PLANETE_X = XX_PLANETE + LARGEUR_PLANETE
POINT_BAS_DROIT_PREMIERE_PLANETE_Y = YY_PLANETE + HAUTEUR_PLANETE

if POINT_BAS_DROIT_PREMIERE_PLANETE_X > XX_FUSEE:
    if POINT_BAS_DROIT_PREMIERE_PLANETE_Y > YY_FUSEE:
        if POINT_BAS_DROIT_PREMIERE_PLANETE_Y < YY_FUSEE + HAUTEUR_FUSEE:
            ARRET_JEU = True

# PLANETE DROITE COLLISION :

POINT_BAS_GAUCHE_DEUXIEME_PLANETE_X = XX_PLANETE + XX_ENTRE_PLANETES
POINT_BAS_GAUCHE_DEUXIEME_PLANETE_Y = YY_PLANETE + YY_ENTRE_PLANETE + HAUTEUR_PLANETE

if XX_FUSEE + LARGEUR_FUSEE > POINT_BAS_GAUCHE_DEUXIEME_PLANETE_X:
    if XX_FUSEE < POINT_BAS_GAUCHE_DEUXIEME_PLANETE_Y:
        if XX_FUSEE + HAUTEUR_FUSEE > POINT_BAS_GAUCHE_DEUXIEME_PLANETE_Y:
            ARRET_JEU + True




