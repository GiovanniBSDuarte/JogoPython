import pygame
import os
import player

WIN_WIDTH = 900
WIN_HEIGHT = 500

ENTITY_WIDTH = 33.75
ENTITY_HEIGTH = 45

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Jogo Python")

FPS = 60


player_pos = [((WIN_WIDTH-player.WIDTH)/2),(WIN_HEIGHT-player.HEIGTH)]
SKELETON = pygame.image.load(os.path.join('code\imagens','skeleton.png'))
SKELETON = pygame.transform.flip(pygame.transform.scale(SKELETON,(ENTITY_WIDTH,ENTITY_HEIGTH)),1,0)

def draw_window():
    WIN.fill((255,255,255))
    WIN.blit(SKELETON, (((WIN_WIDTH-ENTITY_WIDTH)/2),(0)))
    WIN.blit(player.PLAYER, player_pos)
    pygame.display.update()


def main(): 
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_pos[0] - player.VEL >= 0:
            player_pos[0] -= player.VEL

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_pos[0] + player.VEL + ENTITY_WIDTH<= WIN_WIDTH:    
            player_pos[0] += player.VEL

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_pos[1] - player.VEL >= 0:
            player_pos[1] -= player.VEL

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_pos[1] + player.VEL + ENTITY_HEIGTH <= WIN_HEIGHT:    
            player_pos[1] += player.VEL
                   
        
        draw_window()

    pygame.quit()



if __name__ == "__main__":
    main()