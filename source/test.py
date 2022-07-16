import os
import sys

import pygame

pygame.init()
window = pygame.display.set_mode((1400, 600))
pygame.display.set_caption('REVIZOR')

player = pygame.image.load(os.path.join('data', 'pers_2.png'))
#  background = pygame.image.load(os.path.join('data', 'back.jpg'))

x = 0
y = 0
speed = 20

clock = pygame.time.Clock()
run = True
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed

    #  window.blit(background, (0, 0))
    window.fill((0, 0, 0))
    window.blit(player, (x, y))
    pygame.display.update()
pygame.quit()
