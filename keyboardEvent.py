import pygame
pygame.init()

w_width = 500
w_height = 500

screen = pygame.display.set_mode((w_width,w_height))

pygame.display.set_caption("Keyboard Events")

#///////KEYBOARD EVENTS
x = 0
y = 0

width = 50
height = 50
velocity = 1
clock = pygame.time.Clock()



done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    #returns bool
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y-= velocity
    if keys[pygame.K_DOWN]:
        y += velocity
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity

    screen.fill("white")
    pygame.draw.rect(screen, "black", (x,y,width,height))
    #Set the frameRate with module TICK CLOCK
    clock.tick(60)



    pygame.display.flip()