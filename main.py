import pygame;

pygame.init()


window = pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Cyborgnetical's Snake Game")

# Global Variables
gravity = 0.1

# Player Code
player = pygame.surface.Surface((100,100))
player.fill((255,255,255))
player = pygame.image.load("img/Guy_Umbrella.png").convert_alpha()
player = pygame.transform.scale(player,(300,300))

player_x = 0
player_y = 0
x_spd = 0
y_spd = 0



rainDrop_1 = pygame.surface.Surface((50,50))
rainDrop_1.fill((255,255,255))
rainDrop_1_x = 0
rainDrop_1_y = 0
rainDrop_1_y_spd = 0

# game loopus thing, its never lupus - dr house
while True: 
   

    player_x+=x_spd
    player_y+=y_spd+gravity

    rainDrop_1_y -= -0.1

    window.fill((0,0,0))
    window.blit(player,(player_x,player_y))
    window.blit(rainDrop_1,(rainDrop_1_x,rainDrop_1_y))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_spd = -0.2
            if event.key == pygame.K_RIGHT:
                x_spd = 0.2
            if event.key == pygame.K_UP:
                y_spd = -0.2
            if event.key == pygame.K_DOWN:
                y_spd = 0.2
        else: 
            x_spd = 0
            y_spd = 0

        if event.type == pygame.QUIT:
            quit(0)
