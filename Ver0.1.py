  #Pygame template - skeletong for a new pygame project
# A Game For Brick Breaker
# 刘炅 presents

import pygame
import random
import os

WIDTH = 480
HEIGHT = 600
FPS = 60
v=10
SPEEDx = random.choice(range(-10,10))
SPEEDy = int(-(v**2-int(SPEEDx)**2)**1/2)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up assets folders 
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        #Initialize the original position
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH -10, HEIGHT -10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT -5
        self.speedx = 0
        
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed() #Tells us every key that is pressed at the moment
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = +5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def shoot(self):
        #Link the Player to the bullet
        bullet1 = Bullet1(self.rect.centerx, self.rect.top)
        'bullet2 = Bullet2(self.rect.right, self.rect.top)'
        'bullet3 = Bullet3(self.rect.centerx, self.rect.top)'
        all_sprites.add(bullet1)
        bullets.add(bullet1)
        '''all_sprites.add(bullet2)
        bullets.add(bullet2)
        all_sprites.add(bullet3)
        bullets.add(bullet3) '''
     
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        #self.speedy = random.randrange(1, 8)
        #self.speedx = random.randrange(-3, 3)
        
    '''def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH +20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
    '''
    
'''class Bullet3 (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10       
        
    def update(self):
        self.rect.y  += self.speedy 
        # Kill it if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill() 

class Bullet2 (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.speedx = -5       
        
    def update(self):
        self.rect.y  += self.speedy 
        self.rect.x  += self.speedx 
        # Kill it if it moves off the top of the screen
        if self.rect.bottom < 0 or self.rect.left <0:
            self.kill() 
'''
class Bullet1 (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = SPEEDy
        self.speedx = SPEEDx
    
        
    def update(self):
        self.rect.y  += self.speedy 
        self.rect.x  += self.speedx 
        # Kill it if it moves off the top of the screen
        if self.rect.bottom < 0 or self.rect.right > WIDTH:
            self.kill() 


#Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#Game Loop
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    # Update
    all_sprites.update()
    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True ) #kill A or B?
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # After drawing everything, flip the display
    pygame.display.flip()
    
t=0
while t<10000:
    screen.fill(WHITE)     
    t +=1
pygame.quit() 
