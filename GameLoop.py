import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill("white")
pygame.display.set_caption("Quick Game")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.display.flip()