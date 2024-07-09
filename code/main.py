import pygame
import os

winWidth = 900
winHeight = 500

entityWidth = 75
entityHeight = 100

WIN = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Jogo Python")

FPS = 60

PLAYER = pygame.image.load(os.path.join('code\imagens','player.png'))
PLAYER = pygame.transform.scale(PLAYER,(entityWidth,entityHeight))
SKELETON = pygame.image.load(os.path.join('code\imagens','skeleton.png'))
SKELETON = pygame.transform.flip(pygame.transform.scale(SKELETON,(entityWidth,entityHeight)),1,0)

def draw_window():
    WIN.fill((255,255,255))
    WIN.blit(PLAYER, (((winWidth-entityWidth)/2),(winHeight-entityHeight)))
    WIN.blit(SKELETON, (((winWidth-entityWidth)/2),(0)))
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