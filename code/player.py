import pygame
import os
WIDTH = 33.75
HEIGTH = 45


PLAYER = pygame.image.load(os.path.join('code\imagens','PLAYER.png'))
PLAYER = pygame.transform.scale(PLAYER,(WIDTH,HEIGTH))
VEL = 5

