import pygame


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]


    def move(self):
        # Méthode pour se déplacer
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        # Une méthode pour pouvoir afficher notre joueur
        screen.blit(self.image, self.rect)