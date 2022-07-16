import pygame
import sys

pygame.init()
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Название игры!')

player = pygame.image.load('pers_1.png')
background = pygame.image.load('back.jpg')

x = 10
y = 10
speed = 5

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

    window.blit(background, (0, 0))
    window.blit(player, (x, y))
    pygame.display.update()
pygame.quit()
