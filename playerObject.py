import pygame
import math
from settings import *
#TUDO DO JOGADOR ENCONTRA SE AQUI, CLASS, ONDE SE IMPORTA O SPRITE ETC...

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)

        self.resUp=pygame.image.load("Sprites/res/resUp.png")
        self.resUp = pygame.transform.scale(self.resUp, (1144, 52))
        self.resUpNoShadow = pygame.image.load("Sprites/res/resUpNoShadow.png")
        self.resUpNoShadow = pygame.transform.scale(self.resUpNoShadow, (1144, 52))
        self.resDown =pygame.image.load("Sprites/res/resDown.png")
        self.resDown = pygame.transform.scale(self.resDown, (1144, 52))
        self.resDownNoShadow = pygame.image.load("Sprites/res/resDownNoShadow.png")
        self.resDownNoShadow = pygame.transform.scale(self.resDownNoShadow, (1144, 52))
        self.resLeft=pygame.image.load("Sprites/res/resLeft.png")
        self.resLeft = pygame.transform.scale(self.resLeft, (416, 52))
        self.resRight=pygame.image.load("Sprites/res/resRight.png")
        self.resRight = pygame.transform.scale(self.resRight, (416, 52))
        self.image = self.resDown

        self.hp1 =pygame.image.load("Sprites/ui/hp1.png")
        self.hp1 = pygame.transform.scale(self.hp1, (20*2, 62*2))
        self.hp2 =pygame.image.load("Sprites/ui/hp2.png")
        self.hp2 = pygame.transform.scale(self.hp2, (20*2, 62*2))
        self.hp3 =pygame.image.load("Sprites/ui/hp3.png")
        self.hp3 = pygame.transform.scale(self.hp3, (20*2, 62*2))

        self.finalMsg = pygame.image.load("Sprites/ui/final.png")
        self.finalMsg = pygame.transform.scale(self.finalMsg, (350*2, 190*2))
        self.cutSceneMove = -1
                
        self.imageStill = pygame.image.load("Sprites/res/resStill.png")
        self.imageStill = pygame.transform.scale(self.imageStill, (52, 52))

        self.screen=screen
  
        self.nImg=22 #number of sprites
        self.cImg=0 #current sprite

        self.w = 52 #sprite size x
        self.h = 52 #sprite size y

        self.rect = self.imageStill.get_rect()#tirar um rectangulo do sprite
        self.rect.center = (80, 150)
        self.has_KEY = False
        self.hp = 3

    def update(self,finalCutscene,menu):
        keystate = pygame.key.get_pressed()
        if finalCutscene != True:
            if keystate[pygame.K_LEFT] and self.rect.x >= 10:
                self.rect.x -= PLAYERSPEED
                self.image=self.resLeft
                self.nImg = 8
                if self.cImg>8:
                    self.cImg=0
            if keystate[pygame.K_RIGHT] and self.rect.x <= WINDOWWIDTH - self.w - 20:
                self.rect.x += PLAYERSPEED
                self.image=self.resRight
                self.nImg = 8
                if self.cImg>8:
                    self.cImg=0
            if keystate[pygame.K_UP] and self.rect.y >= 70:
                self.rect.y -= PLAYERSPEED
                self.image=self.resUp
                self.nImg = 22
            if keystate[pygame.K_DOWN] and self.rect.y <= WINDOWHEIGHT - self.h - 20:
                self.rect.y += PLAYERSPEED
                self.image=self.resDown
                self.nImg = 22

            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > WINDOWHEIGHT:
                self.rect.bottom = WINDOWHEIGHT

        #ANIMATIONs vvvvvvvvvvvvvvvv
        if keystate[pygame.K_DOWN] or keystate[pygame.K_UP] or keystate[pygame.K_RIGHT] or keystate[pygame.K_LEFT] or finalCutscene == True: #Update sprite only when he moves
            if finalCutscene == True:
                self.nImg = 22
                if self.rect.bottom <= -10:
                    self.image = self.resDownNoShadow
                    self.cutSceneMove = 1
                elif self.rect.top >= WINDOWHEIGHT:
                    self.image = self.resUpNoShadow
                    if self.cutSceneMove == 1 and self.rect.top >= WINDOWHEIGHT + 190*2 + 100:
                        menu.quit_game()
                        
                    
                self.rect.y += self.cutSceneMove*PLAYERSPEED
                
            if self.cImg >=self.nImg-1:
                self.cImg = 0
            else:
                self.cImg+= 1

        self.screen.blit(self.image,self.rect,(self.cImg*self.w,0,self.w,self.h))
        if self.cutSceneMove == 1:
            self.screen.blit(self.finalMsg,(int(WINDOWHEIGHT/2)-50, self.rect.y - 190*2-100))

        if finalCutscene != True:
            #render the UI
            if self.hp >=3: 
                self.screen.blit(self.hp3,(5,5))
            elif self.hp ==2:
                    self.screen.blit(self.hp2,(5,5))
            elif self.hp <=1:
                self.screen.blit(self.hp1,(5,5))
