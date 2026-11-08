import pygame;
import random;

pygame.init()


window = pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Cyborgnetical's Snake Game")

# Global Variables
gravity = 0.1
size = 40

# Player Code
player = pygame.surface.Surface((100,100))
player.fill((255,255,255))
player = pygame.image.load("imgs/Guy_Umbrella.png").convert_alpha()
player = pygame.transform.scale(player,(size,size))

player_x = 0
player_y = 0
x_spd = 0
y_spd = 0


raindrops  = []

class RainDrop:
    def __init__(self):
        self.x = random.randint(0,800)
        self.y = random.randint(0,100)
        self.size = size
        self.display = pygame.image.load("imgs/Raindrop.png").convert_alpha()
        self.display = pygame.transform.scale(self.display,(self.size,self.size))

    def update(self):
        return f"{self.brand} {self.model} with {self.storage}GB"

for i in range(30):
    rainDrop = RainDrop()
    raindrops.append(rainDrop)

# game loopus thing, its never lupus - dr house
while True: 
   

    player_x+=x_spd
    player_y+=y_spd+gravity

    # NOTE: "i" in python is not a int, but the objetct???
    for i in raindrops:
        i.y+=gravity

    window.fill((0,0,0))
    window.blit(player,(player_x,player_y))

    for i in raindrops:
        window.blit(i.display,(i.x,i.y))


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
