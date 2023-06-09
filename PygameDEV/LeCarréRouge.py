import sys, pygame

rouge = 255, 0, 0
bleu = 0, 0, 255

pygame.init()
fenetre = pygame.display.set_mode((400,400))
pygame.display.set_caption("Le carré qui rebondit")

clock = pygame.time.Clock()

XX = 300
DEPLACEMENT = 3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    fenetre.fill(bleu)

    XX += DEPLACEMENT

    if XX >= 320:
        XX = 320
        DEPLACEMENT = -3
    elif XX <= 0:
        XX = 0
        DEPLACEMENT = 3

    pygame.draw.rect(fenetre, rouge, (XX, 200, 80, 80))
    pygame.display.flip()
