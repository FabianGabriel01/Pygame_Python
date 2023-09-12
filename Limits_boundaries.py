import pygame
pygame.init()

w_width = 500
w_height = 500

screen = pygame.display.set_mode((w_width,w_height))

pygame.display.set_caption("Limites on windows")

#///////KEYBOARD EVENTS
x = 0
y = 0

width = 50
height = 50
velocity = 10
clock = pygame.time.Clock()


 
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    #returns bool
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y>0:
        y-= velocity
    if keys[pygame.K_DOWN] and y< w_height-height:
        y += velocity
    if keys[pygame.K_LEFT] and x>0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < w_width- width:
        x += velocity

    screen.fill("white")
    pygame.draw.rect(screen, "black", (x,y,width,height))
    #Set the frameRate with module TICK CLOCK
    clock.tick(60)



    pygame.display.flip()