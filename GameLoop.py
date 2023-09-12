import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill("white")
pygame.display.set_caption("My First pygame program")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pygame.display.flip()