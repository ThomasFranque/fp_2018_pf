import pygame, random
import math
from settings import *

class Decor(pygame.sprite.Sprite):
    def __init__(self,screen,FPS):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((26,29))
        self.image=pygame.image.load("Sprites/decor/plant.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, ((15*5)*3, 14*3))
        self.still=pygame.image.load("Sprites/decor/plantStill.png").convert_alpha()
        self.still = pygame.transform.scale(self.still,(15*3, 14*3))
        self.rect = self.still.get_rect()
        self.rect.center = (759, 262)

        self.screen=screen
        self.FPS = FPS

        self.nImg=5 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 56 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 15*3 #sprite size x
        self.h = 14*3 #sprite size y

    def update(self):
        #ANIMATION vvvvvvvvvvvvvvvv
        if self.cImg >=self.nImg-1:
            self.delay += 1
            if self.delay == self.FPS-(self.totalDelay-44):#fazer o ultimo frame demorar mais (barely unnoticeable)
                self.cImg = 0
                self.delay=0
        else:
            if self.delay >= self.FPS-self.totalDelay:
                self.cImg+= 1
                self.delay=0
            else:
                self.delay+=1

        self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))
        


class Door(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (-55, 170)
        self.sprite = pygame.image.load("Sprites/obstacles/wall.png").convert_alpha()
        self.lock = pygame.image.load("Sprites/obstacles/lock.png").convert_alpha()
        self.lock = pygame.transform.scale(self.lock, (55, 70))

class Key(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((26,29))
        self.image = pygame.image.load("Sprites/key/keySheet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, ((26*12)*3, 29*3))
        self.still = pygame.image.load("Sprites/key/keyStill.png").convert_alpha()
        self.still = pygame.transform.scale(self.still, (26*3, 29*3))
        self.rect = self.still.get_rect()
        self.rect.center = (300, 380)#300 e 360
        self.exists = True

        self.screen=screen

        self.nImg=12 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 58 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 26*3 #sprite size x
        self.h = 29*3 #sprite size y

    def updateSprite(self):
        #ANIMATION vvvvvvvvvvvvvvvv
        if self.cImg >=self.nImg-1:
            self.delay += 1
            if self.delay == FPS-self.totalDelay:#fazer o ultimo frame demorar mais (barely unnoticeable)
                self.cImg = 0
        else:
            if self.delay == FPS-self.totalDelay:
                self.cImg+= 1
                self.delay=0
            else:
                self.delay+=1

        self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))
        

class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((110,90))
        self.image.set_alpha(250)
        self.rect = self.image.get_rect()

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((520,10))
        self.image.set_alpha(250)  
        self.rect = self.image.get_rect()
        self.rect.center = (280, 255)

class RockH(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,165))
        self.image.set_alpha(250)  
        self.rect = self.image.get_rect()
        self.rect.center = (280, 255)


class Stalker(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        
        self.stalkLeft=pygame.image.load("Sprites/enemies/stalkerLeft.png").convert_alpha()
        self.stalkLeft = pygame.transform.scale(self.stalkLeft, (140*4, 22*4))
        self.stalkRight=pygame.image.load("Sprites/enemies/stalkerRight.png").convert_alpha()
        self.stalkRight = pygame.transform.scale(self.stalkRight, (140*4, 22*4))
        
        self.image = self.stalkLeft
        
        self.imageStill = pygame.image.load("Sprites/enemies/stalkerStill.png").convert_alpha()
        self.imageStill = pygame.transform.scale(self.imageStill, (11*4, 20*4))

        self.screen=screen
  
        self.nImg=10 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 58 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 14*4 #sprite size x
        self.h = 22*4 #sprite size y

        self.rect = self.imageStill.get_rect()#tirar um rectangulo do sprite
        self.range = 350
        
    def update(self,player,FPS):
        if player.rect.x >= self.rect.x -self.range and player.rect.x <= self.rect.x +self.range and player.rect.y >= self.rect.y -(self.range-(int(self.range/3))) and player.rect.y <= self.rect.y +(self.range-(int(self.range/3))):
            if player.rect.x<self.rect.x: #esquerda
                self.rect.move_ip(-PLAYERSPEED+4,0)
                self.image=self.stalkLeft
            elif player.rect.x>self.rect.x: #direita
                self.rect.move_ip(PLAYERSPEED-4,0)
                self.image=self.stalkRight

            if player.rect.y<self.rect.y:
                self.rect.move_ip(0,-PLAYERSPEED+4)
            elif player.rect.y>self.rect.y:
                self.rect.move_ip(0,PLAYERSPEED-4)

            #ANIMATION vvvvvvvvvvvvvvvv
            if self.cImg >=self.nImg-1:
                self.delay += 1
                if self.delay == FPS-self.totalDelay:#fazer o ultimo frame demorar mais (barely noticeable)
                    self.cImg = 0
            else:
                if self.delay == FPS-self.totalDelay:
                    self.cImg+= 1
                    self.delay=0
                else:
                    self.delay+=1

            self.screen.blit(self.image,(self.rect.x,self.rect.y-10,self.rect[2],self.rect[3]),(self.cImg*self.w,0,self.w,self.h))
        else:
            self.image = self.imageStill
            self.screen.blit(self.image,self.rect)


class Shooter(pygame.sprite.Sprite):
    def __init__(self,screen,shotHitWallSound,speedSound,directionX,directionY,locationX,locationY):
        pygame.sprite.Sprite.__init__(self)

        self.shotHitWallSound = shotHitWallSound
        self.speedSound = speedSound
        self.directionX = directionX
        self.directionY = directionY
        
        self.screen=screen
        
        self.nImg=15 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 58 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 16*2 #sprite size x
        self.h = 16*2 #sprite size y

        #self.rect = self.shotStill.get_rect()#tirar um rectangulo do sprite

        #shot properties
        self.shotStill = pygame.image.load("Sprites/enemies/shotStill.png").convert_alpha()
        self.shotStill = pygame.transform.scale(self.shotStill, (16*2, 16*2))
        self.shotUp=pygame.image.load("Sprites/enemies/shotUp.png").convert_alpha()
        self.shotUp = pygame.transform.scale(self.shotUp , ((16*15)*2, 16*2))
        self.shotLeft=pygame.image.load("Sprites/enemies/shotLeft.png").convert_alpha()
        self.shotLeft = pygame.transform.scale(self.shotLeft, ((16*15)*2, 16*2))

        self.usedImage = self.shotUp

        self.rect = self.shotStill.get_rect()#tirar um rectangulo do sprite

        self.locationX = locationX 
        self.locationY = locationY
        
        self.shots=[]
        self.shotMinSize = 199
        self.shotMaxSize = 200
        self.shotMinSpeed = 1
        self.shotMaxSpeed = 15
        self.shotAddRate = 60
        self.shotAddCounter = 0
        
    def update(self,player,FPS): #directionX e directionY multiplica o valor, os valores serão apenas 1, -1 e 0 USADO NO MOVE THE SHOTS
        #create the shot                                                sendo o 1 cima->baixo ou esquerda->direita, o -1 baixo->cima direita->esquerda e o 0 parar
        self.shotAddCounter+=1
        if self.shotAddCounter == self.shotAddRate:
            self.shotAddCounter = 0 #####pygame.Rect(random.randint(100, 200 - baddieSize)#####
            self.shotSize = random.randint(self.shotMinSize, self.shotMaxSize)
            self.newShot = {'rect': pygame.Rect(self.locationX,self.locationY, 16*2, 16*2), 
                        'speed': random.randint(self.shotMinSpeed, self.shotMaxSpeed),
                        'surface':pygame.transform.scale(self.shotStill,(16*2,16*2)),
                        }
            self.shots.append(self.newShot)
            if self.newShot['speed'] >= 11:
                self.speedSound.play()
        
        # Move the shots
        for b in self.shots: #change sides here (up down etc..)
               b['rect'].move_ip(self.directionX*b['speed'],self.directionY*b['speed'])

        #render them shots
        #ANIMATION vvvvvvvvvvvvvvvv
        if self.cImg >=self.nImg-1:
            self.delay += 1
            if self.delay == FPS-self.totalDelay:#fazer o ultimo frame demorar mais (barely unnoticeable)
                    self.cImg = 0
                    self.delay=0
        else:
            if self.delay == FPS-self.totalDelay:
                    self.cImg+= 1
                    self.delay=0
            else:
                    self.delay+=1
                    
        for b in self.shots:
            self.screen.blit(self.usedImage,b['rect'],(self.cImg*self.w,0,self.w,self.h))

        #collision
        for b in self.shots:
            if player.rect.colliderect(b['rect']):
                player.hp-=1
                print(player.hp)
                
        # Delete shots went pass the limit or hit the player.
        for b in self.shots[:]:
            if b['rect'].top < 75 or b['rect'].left < 18 or player.rect.colliderect(b['rect']):
                self.shots.remove(b)
                self.shotHitWallSound.play()
                
class Background(pygame.sprite.Sprite):
    def __init__(self,screen,FPS):
        pygame.sprite.Sprite.__init__(self)
        self.zona2 = pygame.image.load("Sprites/WIP/zona_2/zona_2_unfinished.png").convert_alpha()
        self.zona2 = pygame.transform.scale(self.zona2, (1280, 720))
        self.zona2_anim = pygame.image.load("Sprites/WIP/zona_2/zona_2_animated.png").convert_alpha()
        self.zona2_anim = pygame.transform.scale(self.zona2_anim, (1280*8, 720))
        self.rect = self.zona2.get_rect()
        self.rect.topleft = (0, 0)

        self.screen=screen
        self.FPS = FPS

        self.nImg=8 #number of sprites
        self.cImg=0 #current sprite
        
        self.totalDelay = 58 #tempo antes de mudar de sprite (Quanto maior mais lento)
        self.delay = 0 #contagem do delay usado no update

        self.w = 1280 #sprite size x
        self.h = 720 #sprite size y

    def update(self):
        #ANIMATION vvvvvvvvvvvvvvvv
        if self.cImg >=self.nImg-1:
            self.delay += 1
            if self.delay == self.FPS-self.totalDelay:#fazer o ultimo frame demorar mais (barely unnoticeable)
                self.cImg = 0
        else:
            if self.delay >= self.FPS-self.totalDelay:
                self.cImg+= 1
                self.delay=0
            else:
                self.delay+=1

        self.screen.blit(self.zona2_anim,self.rect,(self.cImg*self.w,0,self.w,self.h))
