import pygame
# Pygame est une bibliothèque qui regroupe beaucoup de sous module fesant chacun des actions différentes


pygame.init()
#  Pour pouvoir utiliser comme il faut la bibliothèque d'initialiser tout ses composants

screen = pygame.display.set_mode((400, 400))
# pygame.display est un sous module de pygame qui permet de gérer tout ce qui concerne les fenêtres d'écran
# Que sa soit pour Nommer la fenêtre , Gérer ses dimensions ou pour Gérer les paramètres d'initialisation
# Il suffit de stocker cette méthode dans une variable par convention on prendra l'habitude de la nommer (screen)

running = True
# Ce qui va permettre de laisser ouvert la fenêtre d'écran s'appelle "La boucle de jeu"
# On va créer un "booleen" qui représentera l'état de notre fenêtre / "True"
# Puis on va créer une boucle while qui vérifie à chaque tour  si ce "booleen" est bien assigné à "True"

image = pygame.image.load("Luffy.png").convert()

clock = pygame.time.Clock()

x = 0
y = 0



while running:
     for event in pygame.event.get():
# Il va falloir récupérer à chaque tour de notre boucle de jeu la liste des évenements actuellement trigger
         if event.type == pygame.QUIT:
# On parcours cette liste et pour chaque évenement trigger on vérifie son type s'il correspond à la fermeture de la fenêtre c-à-d à la constante (pygame.QUIT:)
             running = False
# On peut arrêter notre boucle infini en passant la variable (running) à (False) ce qui permettra d'arrêter l'exécution de la boucle du jeu
# Cela est un évenement de fermeture

         # if event.type == pygame.KEYDOWN:
          #  if event.key == pygame.K_LEFT:
           #     print("Gauche !")
            # if event.key == pygame.K_RIGHT:
             #   print("Droite !")
            # if event.key == pygame.K_UP:
             #   print("Haut !")
            # if event.key == pygame.K_DOWN:
             #   print("Bas !")

     # Les event.key sont utilisé pour définir une touche sur la quelle il faut appuyé pour faire bouger son personnage

     pressed = pygame.key.get_pressed()
     if pressed[pygame.K_LEFT]:
        x -= 1
        print("Gauche")
     if pressed[pygame.K_RIGHT]:
        x += 1
        print("Droite")
     if pressed[pygame.K_UP]:
        y -= 1
        print("Haut")
     if pressed[pygame.K_DOWN]:
        y += 1
        print("Bas")

     screen.fill((0, 0, 0))

     screen.blit(image, (x, y))

     pygame.display.flip()
     clock.tick(200)
pygame.QUIT()
# Finalement il ne reste plus qu'a déinitialiser les composants de pygame avec la simple instruction (pygame.QUIT())

# Les évènements qui sont:

# QUIT: fermeture ou alt + f4 qui est activé à chaque fois que le boutton de fermeture de l'application ou bien que la combinaison de touche alt + f4 qui sont enclenchés

# KEYDOWN: touche du clavier enfoncée qui est activé à chaque fois qu'une touche du clavier est appuyée { possèdent un attribut (event.key) qui prend une valeur qui leur sont propres à chaque touche du clavier
# KEYUP: touche du clavier relâchée qui est activé à chaque fois qu'une touche du clavier est relâchée  { possèdent un attribut (event.key) qui prend une valeur qui leur sont propres à chaque touche du clavier

# MOUSEBUTTONDOWN: bouton de la souris { Qui réagissent respectivement au mêmes actions que KEYDOWN et KEYUP {Ils ont un attribut event.pos qui est un tuple de 2 valeurs correspondant à leur coordonées de la souris au moment du clique} ou bien {un attribut (event.button) qui prendra une valeur différentes en fonctions du boutton de la souris qui est appuyée}
# MOUSEBUTTONUP: bouton de la souris   mais avec les bouttons de la souris}                                  {Ils ont un attribut event.pos qui est un tuple de 2 valeurs correspondant à leur coordonées de la souris au moment du clique} ou bien {un attribut (event.button) qui prendra une valeur différentes en fonctions du boutton de la souris qui est appuyée}

#MOUSEMOTION: mouvement de la souris qui est activé à chaque fois que la souris est déplacée

# Un joueur aura des (Attributs) qui sont:
# - Points de vie
# - Compétences
# - Armes
# - Etc...

# Un joueur aura des (méthodes) qui sont:
# - Se déplacer
# - Être bloqué
# - Etc...

