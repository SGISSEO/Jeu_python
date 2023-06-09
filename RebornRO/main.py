import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Ragnarok Online")

# Chargement des images des personnages
image_archer = pygame.image.load("archer.png")
image_magicien = pygame.image.load("magicien.png")

# Classe pour représenter un personnage
class Personnage(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def afficher(self):
        fenetre.blit(self.image, self.rect)

# Création des instances de personnages
archer = Personnage(image_archer, 100, 100)
magicien = Personnage(image_magicien, 200, 200)

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    fenetre.fill((255, 255, 255))

    # Afficher les personnages
    archer.afficher()
    magicien.afficher()

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()

