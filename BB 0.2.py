#Bouncing Ball
#ver 0.1


import pygame
import os
import random


#Set windows feature
WIDTH = 480
HEIGHT = 600
FPS = 60


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


class LIMIT(pygame.sprite.Sprite):
    # sprite for the Background
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 14

    def update(self):
        self.rect.centerx = self.rect.centerx
        self.rect.bottom = self.rect.bottom



class BG(pygame.sprite.Sprite):
    # sprite for the Background
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(YELLOW)#for testing
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT

    def update(self):
        self.rect.centerx = self.rect.centerx
        self.rect.bottom = self.rect.bottom

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        #Initialize the original position
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 15))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT -10
        self.speedx = 0
        
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed() #Tells us every key that is pressed at the moment
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = +10
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def shoot(self):
        #Link the Player to the bullet
        bullet1 = Bullet1(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet1)
        bullets.add(bullet1)

    def sprite(self):
        print('hi')

        
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - 20)
        self.rect.y = random.randrange(HEIGHT - 100)
        
        if self.rect.bottom < 0 or self.rect.right > WIDTH:
            self.kill()
    
class Bullet1 (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedx = random.randint(-5,-5)
        self.speedy = -((7**2-self.speedx**2)**(1/2))
    
        
    def update(self):
        self.rect.y  += self.speedy 
        self.rect.x  += self.speedx 
        # Kill it if it moves off the screen
        if self.rect.top < 0:
            self.speedy = - self.speedy
        if self.rect.right > WIDTH or self.rect.right < 0:
            self.speedx = - self.speedx
        if self.rect.bottom > HEIGHT -20:
            self.kill()
            pygame.quit()

    def bounce(self):
        self.speedx = -self.speedx
        self.speedy = -self.speedy

#def spritecollide(spriteA,spriteB):
    


#Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BB 0.2")
clock = pygame.time.Clock()


mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
bg = BG()
all_sprites.add(bg)
limit = LIMIT()
all_sprites.add(limit)


for i in range(random.randint(10,30)):
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
    hits = pygame.sprite.groupcollide(mobs, bullets, True, False) #kill A or B?
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        Mob.kill(m)
    # check to see if a mob hit the player
    
    hits1 = pygame.sprite.groupcollide(bullets, player,True, True)
    for hit1 in hits1:
        b = Bullet1()
        all_sprites.add(b)
        Player.bounce(b)
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

'''2019-7-3
日志
发现‘sprite.spritecollide’函数不好用，无法解决两个sprite 的碰撞，亟待解决
希望运用135行的新函数
'''
