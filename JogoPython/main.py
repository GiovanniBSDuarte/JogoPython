import pygame
import os

WIN_WIDTH = 900
WIN_HEIGHT = 500

ENTITY_WIDTH = 75
ENTITY_HEIGHT = 100

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Game Porra")

FPS = 60

PLAYER = pygame.image.load(os.path.join('imagens','player.png'))
PLAYER = pygame.transform.scale(PLAYER,(ENTITY_WIDTH,ENTITY_HEIGHT))
SKELETON = pygame.image.load(os.path.join('imagens','skeleton.png'))
SKELETON = pygame.transform.flip(pygame.transform.scale(SKELETON,(ENTITY_WIDTH,ENTITY_HEIGHT)),1,0)

def draw_window():
    WIN.fill((255,255,255))
    WIN.blit(PLAYER, (((WIN_WIDTH-ENTITY_WIDTH)/2),(WIN_HEIGHT-ENTITY_HEIGHT)))
    WIN.blit(SKELETON, (((WIN_WIDTH-ENTITY_WIDTH)/2),(0)))
    pygame.display.update()


def main(): 
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()



if __name__ == "__main__":
    main()