import pygame;

pygame.init()


window = pygame.display.set_mode((800,600))
window.fill((0,0,0))
# odd.
pygame.display.set_caption("Cyborgnetical's Snake Game")

player = pygame.surface.Surface((100,100))
player.fill((255,255,255))
player_x = 0
player_y = 0
x_spd = 0
y_spd = 0

falling_object = pygame.surface.Surface((50,50))
falling_object.fill((255,255,255))
falling_object_x = 0
falling_object_y = 0
falling_object_x_spd = 0
falling_object_y_spd = 0

# game loopus thing, its never lupus - dr house
while True: 
   

    player_x+=x_spd
    player_y+=y_spd

    window.fill((0,0,0))
    window.blit(player,(player_x,player_y))
    window.blit(falling_object,(falling_object_x,falling_object_y))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_spd = -2
            if event.key == pygame.K_RIGHT:
                x_spd = 2
            if event.key == pygame.K_UP:
                y_spd = -2
            if event.key == pygame.K_DOWN:
                y_spd = 2
        else: 
            x_spd = 0
            y_spd = 0

        if event.type == pygame.QUIT:
            quit(0)
