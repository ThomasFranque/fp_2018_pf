import pygame, sys, random
from pygame.locals import *
from settings import *
import playerObject, gameObjects, menu
import os

# Set up pygame
pygame.mixer.pre_init(44100,-16,2,1024)#preload dos sons
pygame.init()
mainClock = pygame.time.Clock()

size = (WINDOWWIDTH, WINDOWHEIGHT)
screen = pygame.display.set_mode(size)

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption(TITLE)


zona1 = pygame.image.load("Sprites/WIP/zona_1/zona_1_unfinished.png").convert_alpha()
zona1 = pygame.transform.scale(zona1, (1280, 720))

zona2 = pygame.image.load("Sprites/WIP/zona_2/zona_2_unfinished.png").convert_alpha()
zona2 = pygame.transform.scale(zona2, (1280, 720))

zona1_1 = pygame.image.load("Sprites/WIP/zona_1_1/zona_1_1_unfinished.gif").convert_alpha()
zona1_1 = pygame.transform.scale(zona1_1, (1280, 720))

#music/sounds
music = pygame.mixer.music.load('Sounds/bgmusic.wav')
pygame.mixer.music.play(-1)
doorSound = pygame.mixer.Sound('Sounds/door.wav')
thumpSound = pygame.mixer.Sound('Sounds/fall.wav')
shotHitWallSound = pygame.mixer.Sound('Sounds/hitWall.wav')
speedSound = pygame.mixer.Sound('Sounds/speed.wav')
areaChange = pygame.mixer.Sound('Sounds/areaChange.wav')
stalkerKill = pygame.mixer.Sound('Sounds/stalkerKill.wav')
victory = pygame.mixer.Sound('Sounds/victory.wav')

# Set up variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

currentArea = 0
    #0 - Zona 1
    #1 - Zona 1.1
    #2 - Zona 2
    #3 - Zona 2.1

windowSurface.fill(BLUE)
windowSurface.fill(GREEN)
windowSurface.fill(RED)
windowSurface.fill(YEET)


''''''
player = playerObject.Player(screen)
menu = menu.menu(screen)

"PARA A ZONA_1"
all_sprites = pygame.sprite.Group()
rocksU = pygame.sprite.Group()
rocksD = pygame.sprite.Group()
rocksL = pygame.sprite.Group()
rocksR = pygame.sprite.Group()
keys = pygame.sprite.Group()
doors = pygame.sprite.Group()
walls = pygame.sprite.Group()

door1 = gameObjects.Door()
all_sprites.add(door1)
doors.add(door1)

wall = gameObjects.Wall()
all_sprites.add(wall)
walls.add(wall)
wall.rect.topleft = (30, 300)

yellowKey = gameObjects.Key(screen)
all_sprites.add(yellowKey)
keys.add(yellowKey)

rockU = gameObjects.Rock()#queda para cima orginal
all_sprites.add(rockU)
rocksU.add(rockU)

rockD = gameObjects.Rock()#queda para baixo original
all_sprites.add(rockD)
rocksD.add(rockD)
rockD.rect.center = (280, 265)

rockL = gameObjects.RockH()#queda para esquerda original
all_sprites.add(rockL)
rocksL.add(rockL)
rockL.rect.topleft = (535,265)

rockR = gameObjects.RockH()#queda para direita original
all_sprites.add(rockR)
rocksR.add(rockR)
rockR.rect.topleft = (520,270)

rockU2 = gameObjects.Rock()
all_sprites.add(rockU2)
rocksU.add(rockU2)
rockU2.rect.center = (800, 435)

rockD2 = gameObjects.Rock()
all_sprites.add(rockD2)
rocksD.add(rockD2)
rockD2.rect.center = (800, 440)

rockL2 = gameObjects.RockH()
all_sprites.add(rockL2)
rocksL.add(rockL2)
rockL2.rect.topleft = (800,55)

rockR2 = gameObjects.RockH()
all_sprites.add(rockR2)
rocksR.add(rockR2)
rockR2.rect.topleft = (775,55)

rockL3 = gameObjects.RockH()
all_sprites.add(rockL3)
rocksL.add(rockL3)
rockL3.rect.topleft = (1050,245)

rockR3 = gameObjects.RockH()
all_sprites.add(rockR3)
rocksR.add(rockR3)
rockR3.rect.topleft = (1020,245)

stalker_1 = gameObjects.Stalker(screen)
stalker_1.rect.center = (500,WINDOWHEIGHT-140)
stalker_2 = gameObjects.Stalker(screen)
stalker_2.rect.center = (WINDOWWIDTH - 100,100)
stalker_3 = gameObjects.Stalker(screen)
stalker_3.rect.center = (WINDOWWIDTH - 100,WINDOWHEIGHT-140)

plant = gameObjects.Decor(screen,FPS)
plant2 = gameObjects.Decor(screen,FPS)
plant2.rect.center=(400,271)

"PARA A ZONA_2"
all_sprites2 = pygame.sprite.Group()
rocksUZ2 = pygame.sprite.Group()
rocksDZ2 = pygame.sprite.Group()
rocksLZ2 = pygame.sprite.Group()
rocksRZ2 = pygame.sprite.Group()
keysZ2 = pygame.sprite.Group()
doorsZ2 = pygame.sprite.Group()
wallsZ2 = pygame.sprite.Group()

zona_2_animated = gameObjects.Background(screen,FPS)

doorZ2 = gameObjects.Door()
all_sprites2.add(doorZ2)
doorsZ2.add(doorZ2)
doorZ2.rect.center = (480,15)

yellowKeyZ2 = gameObjects.Key(screen)
all_sprites2.add(yellowKeyZ2)
keysZ2.add(yellowKeyZ2)
yellowKeyZ2.rect.center = (1150,300)

rockUZ2 = gameObjects.Rock()
all_sprites2.add(rockUZ2)
rocksUZ2.add(rockUZ2)
rockUZ2.rect.center = (360,250)

rockDZ2 = gameObjects.Rock()
all_sprites2.add(rockDZ2)
rocksDZ2.add(rockDZ2)
rockDZ2.rect.center = (360,255)

rockUZ2_2 = gameObjects.Rock()
all_sprites2.add(rockUZ2_2)
rocksUZ2.add(rockUZ2_2)
rockUZ2_2.rect.center = (900,250)

rockDZ2_2 = gameObjects.Rock()
all_sprites2.add(rockDZ2_2)
rocksDZ2.add(rockDZ2_2)
rockDZ2_2.rect.center = (900,255)

rockUZ2_3 = gameObjects.Rock()
all_sprites2.add(rockUZ2_3)
rocksUZ2.add(rockUZ2_3)
rockUZ2_3.rect.center = (1150,250)

rockDZ2_3 = gameObjects.Rock()
all_sprites2.add(rockDZ2_3)
rocksDZ2.add(rockDZ2_3)
rockDZ2_3.rect.center = (1150,255)

rockLZ2 = gameObjects.RockH()
all_sprites2.add(rockLZ2)
rocksLZ2.add(rockLZ2)
rockLZ2.rect.center = (850,350)

rockRZ2 = gameObjects.RockH()
all_sprites2.add(rockRZ2)
rocksRZ2.add(rockRZ2)
rockRZ2.rect.center = (875,350)

rockLZ2_2 = gameObjects.RockH()
all_sprites2.add(rockLZ2_2)
rocksLZ2.add(rockLZ2_2)
rockLZ2_2.rect.center = (850,460)

rockRZ2_2 = gameObjects.RockH()
all_sprites2.add(rockRZ2_2)
rocksRZ2.add(rockRZ2_2)
rockRZ2_2.rect.center = (875,460)

shooter_1 = gameObjects.Shooter(screen,shotHitWallSound,speedSound,0,-1, 200, 630)
shooter_2 = gameObjects.Shooter(screen,shotHitWallSound,speedSound,-1,0, WINDOWWIDTH-80,405)
shooter_2.usedImage = shooter_2.shotLeft

menu.start_screen()
# MAIN GAME LOOP.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    if currentArea == 0 and player.rect.left <= 10 and player.rect.top < 250 and player.rect.top > 0:
        currentArea = 2
        player.rect.right = WINDOWWIDTH - 21
        areaChange.play()
    elif player.rect.right >= WINDOWWIDTH - 20  and player.rect.top < 259 and player.rect.top > 0 and currentArea != 0:
        currentArea = 0 
        player.rect.left = 21
        areaChange.play()
    if currentArea == 2 and player.rect.left > 415 and player.rect.right < 545 and player.rect.top < 70:
        currentArea = 3
        pygame.mixer.music.stop()
        victory.play()
        player.rect.center=(int(WINDOWWIDTH/2),int(WINDOWHEIGHT+100))
    
    #door1 desctruction
    if player.has_KEY == True: 
            door1.kill()
            doorSound.play()
            player.has_KEY = False

    #TEMP.
    if currentArea <= 0:
        screen.blit(zona1,(0,0))

    #death
    if player.hp == 0:
        #puts player on start
        currentArea = 0
        player.rect.center = (80, 150)
        pygame.mixer.music.unpause()
        #resets hp
        player.hp = 3
        #resets door 1st zone
        door1.kill()
        door1 = gameObjects.Door()
        all_sprites.add(door1)
        doors.add(door1)
        #resets key 1st zone
        yellowKey = gameObjects.Key(screen)
        all_sprites.add(yellowKey)
        keys.add(yellowKey)
        #resets stalkers 1st zone
        stalker_1 = gameObjects.Stalker(screen)
        stalker_1.rect.center = (500,WINDOWHEIGHT-140)
        stalker_2 = gameObjects.Stalker(screen)
        stalker_2.rect.center = (WINDOWWIDTH - 100,100)
        stalker_3 = gameObjects.Stalker(screen)
        stalker_3.rect.center = (WINDOWWIDTH - 100,WINDOWHEIGHT-140)
        #resets door 2nd zone
        doorZ2.kill()
        doorZ2 = gameObjects.Door()
        all_sprites2.add(doorZ2)
        doorsZ2.add(doorZ2)
        doorZ2.rect.center = (480,15)
        #resets key 2nd zone
        yellowKeyZ2 = gameObjects.Key(screen)
        all_sprites2.add(yellowKeyZ2)
        keysZ2.add(yellowKeyZ2)
        yellowKeyZ2.rect.center = (1150,300)   

    if currentArea == 0: #JOGADOR ESTÁ NA ZONA 1

        #check for colisions here
        if pygame.sprite.spritecollide(player, rocksU, False):
            player.rect.y -= 75
            player.hp -= 1
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksD, False):
            player.rect.y += 75
            player.hp -= 1
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksL, False):
            player.rect.x += 75
            player.hp -= 1
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksR, False):
            player.rect.x -= 75
            player.hp -= 1
            thumpSound.play()

        #inimigos a colidir com buracos e player############
        if pygame.sprite.spritecollide(stalker_1, rocksU, False):
            stalker_1.rect.y -= 15
        if pygame.sprite.spritecollide(stalker_1, rocksD, False):
            stalker_1.rect.y += 15
        if pygame.sprite.spritecollide(stalker_1, rocksL, False):
            stalker_1.rect.x += 15
        if pygame.sprite.spritecollide(stalker_1, rocksR, False):
            stalker_1.rect.x -= 15    
            
        if pygame.sprite.spritecollide(stalker_2, rocksU, False):
            stalker_2.rect.y -= 15
        if pygame.sprite.spritecollide(stalker_2, rocksD, False):
            stalker_2.rect.y += 15
        if pygame.sprite.spritecollide(stalker_2, rocksL, False):
            stalker_2.rect.x += 15
        if pygame.sprite.spritecollide(stalker_2, rocksR, False):
            stalker_2.rect.x -= 15

        if pygame.sprite.spritecollide(stalker_3, rocksU, False):
            stalker_3.rect.y -= 15
        if pygame.sprite.spritecollide(stalker_3, rocksD, False):
            stalker_3.rect.y += 15
        if pygame.sprite.spritecollide(stalker_3, rocksL, False):
            stalker_3.rect.x += 15
        if pygame.sprite.spritecollide(stalker_3, rocksR, False):
            stalker_3.rect.x -= 15

        #stalker BAD TOUCH
        if player.rect.colliderect(stalker_1.rect) or player.rect.colliderect(stalker_2.rect) or player.rect.colliderect(stalker_3.rect):
            delay = 0
            pygame.mixer.music.pause()
            stalkerKill.play()
            while True:
                delay += 1
                if delay >= 60*5:
                    pygame.mixer.music.unpause()
                    #changes hp
                    player.hp -= 1
                    if yellowKey.exists == False:
                        player.rect.center = (80, WINDOWHEIGHT-200)
                    else:
                        player.rect.center = (80, 150)
                    break
        ###############################           
        if pygame.sprite.spritecollide(player, doors, False):
            player.rect.x += PLAYERSPEED

        hits = pygame.sprite.spritecollide(player, keys, True)
        if hits:
            player.has_KEY = True

        #contacto com o totem
        if pygame.sprite.spritecollide(player, walls, False):
            player.rect.x += PLAYERSPEED
            player.rect.y += PLAYERSPEED 

        #all_sprites.draw(windowSurface)

        # commit renders
        plant.update()
        
        if player.has_KEY == True:
            yellowKey.exists = False      
        if yellowKey.exists == True:
            yellowKey.updateSprite()
            screen.blit(door1.sprite,(-20,20))

        stalker_1.update(player,FPS)
        stalker_2.update(player,FPS)
        stalker_3.update(player,FPS)

    #JOGADOR ESTÁ NA ZONA 2 ###########################################
    elif currentArea == 2:
        #check for colisions here
        player.has_KEY = False
        
        if pygame.sprite.spritecollide(player, rocksUZ2, False):
            player.rect.y -= 75
            player.hp -= 1
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksDZ2, False):
            player.rect.y += 75
            player.hp -= 1
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksLZ2, False):
            player.rect.x -= 75
            player.hp -= 1
            thumpSound.play()
        if pygame.sprite.spritecollide(player, rocksRZ2, False):
            player.rect.x += 75
            player.hp -= 1
            thumpSound.play()
        if pygame.sprite.spritecollide(player, doorsZ2, False):
            player.rect.y += PLAYERSPEED
        hits = pygame.sprite.spritecollide(player, keysZ2, True)
        
        if hits:
            player.has_KEY = True           
        if player.has_KEY == True:
            yellowKeyZ2.exists = False           
        if player.has_KEY == True: 
            doorZ2.kill()
            doorSound.play()
            player.has_KEY = False
            
        #commit renders
        zona_2_animated.update()
        
        if yellowKeyZ2.exists == True:
            yellowKeyZ2.updateSprite()
            screen.blit(doorZ2.lock,(458,20))

        plant2.update()
        #all_sprites2.draw(windowSurface)
        #all_sprites2.update()

        shooter_1.update(player,FPS)
        shooter_2.update(player,FPS)
        
    #AREA 3 (FINAL)#######################################################
    elif currentArea == 3:
        screen.fill(BLACK)
        
    player.update(False,menu) if currentArea != 3 else player.update(True,menu)
    
    pygame.display.flip()
    mainClock.tick(FPS)
    dlt = mainClock.tick(FPS) / 1000
