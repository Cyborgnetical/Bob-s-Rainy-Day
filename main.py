import pygame;
import random;

pygame.init()

# window and display stuff
window = pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Cyborgnetical's Snake Game")
font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 74)




# Global Variables
gravity = 0.2
size = 40
# -\left(x-2\right)\left(x+0\right)


# Player Code
player = pygame.surface.Surface((size,size))
player.fill((255,255,255))
#player = pygame.image.load("imgs/Guy_Umbrella.png").convert_alpha()
#player = pygame.transform.scale(player,(size,size))

player_x = 0
player_y = 600-size
x_spd = 0
y_spd = 0
player_hp = 5

jumptimer = 0

jumping = False

display_player_hp = font.render("Health: "+str(player_hp),True,(255, 255, 255))


# Rain Code
raindrops  = []


class RainDrop:
    def __init__(self):
        self.x = random.randint(0,800)
        self.y = 0-random.randint(0,600)
        self.size = size
        self.display = pygame.surface.Surface((size,size))
        self.display.fill((255,255,255))
        #self.display = pygame.image.load("imgs/Raindrop.png").convert_alpha()
        #self.display = pygame.transform.scale(self.display,(self.size,self.size))

for i in range(10):
    rainDrop = RainDrop()
    raindrops.append(rainDrop)


# empty object for cords cuz player and im too lazy to program it into a proper object
class Empty:
    def __init__(self,x,y):
        self.x = x
        self.y = y
# other game logic

# wasted 1 hour and 30 mintues on this part
def SquareCollision(Cords1,Cords2):
    return (
    (Cords1.x <= Cords2.x+size) and
    (Cords1.x+size >= Cords2.x) and
    (Cords1.y <= Cords2.y+size) and
    (Cords1.y+size >= Cords2.y)
    )

# game loopus thing, its never lupus - dr house
while True: 
   

    player_x+=x_spd
    if(jumping == True):
        jumptimer+=1
        player_y-=gravity*3
    
    if(jumptimer>=1*60):
        jumping = False
        jumptimer = 0
        print("jumped")
    
    
    # player_y+=y_spd+gravity

    # NOTE: "i" in python is not a int, but the objetct???
    for i in raindrops:
        i.y+=gravity

    if(player_y>=600-size):
        player_y = 600-size
    else:
        player_y += gravity
    window.fill((0,0,0))
    window.blit(player,(player_x,player_y))

    for i in raindrops:
        if(SquareCollision(Empty(player_x,player_y),i)):
            player_hp-=1
            display_player_hp = font.render("Health: "+str(player_hp),True,(255, 255, 255))
        if(i.y>600-size or SquareCollision(Empty(player_x,player_y),i) ):
            i.y=0
            i.x=random.randint(0,800)
        
        window.blit(i.display,(i.x,i.y))

    window.blit(display_player_hp, (0,0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_spd = -0.2
            if event.key == pygame.K_RIGHT:
                x_spd = 0.2
            if event.key == pygame.K_UP:
                jumping = True
            if event.key == pygame.K_DOWN:
                y_spd = 0.2
        else: 
            x_spd = 0
            y_spd = 0

        if event.type == pygame.QUIT:
            quit(0)
