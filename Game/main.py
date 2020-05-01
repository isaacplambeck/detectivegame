import pygame, sys, math
from spriteSheetToList import *


def moveManual(rect, speed, width):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rect.x = rect.x + speed
    if keys[pygame.K_LEFT]:
        rect.x = rect.x - speed
    if keys[pygame.K_UP]:
        rect.y = rect.y - speed
    if keys[pygame.K_DOWN]:
        rect.y = rect.y + speed
    if rect.left < 0:
        rect.left = 0
    if rect.right > width:
        rect.right = width
    return rect
    

pygame.init()
pygame.display.init()
screeninfo = pygame.display.Info()
clock = pygame.time.Clock()
FPS = 60
size = width, height = screeninfo.current_w, screeninfo.current_h
black = 0,0,0
white = 255,255,255
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
floor = pygame.image.load("floor.jpg").convert()
floor = pygame.transform.scale(floor,[width, height])
speed = 4
count = 0
frames = 0
animation_speed = 5

bullets=[]

Player = pygame.image.load("PlayerRight.png")
Player = pygame.transform.scale(Player, (200,200))
Playerrect = Player.get_rect()
Playerrect.bottom = height - 500
Gun = pygame.image.load("PlayerArmRight.png")
Gun = pygame.transform.scale(Gun, (200,200))
Gunrect = Gun.get_rect()
Gunrect.right = width - 100



while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Player = pygame.image.load("PlayerArmRight.png")
                    Player = pygame.transform.scale(Player, (200,200))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Player = pygame.image.load("PlayerArmLeft.png")
                    Player = pygame.transform.scale(Player, (200,200))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    Player = pygame.image.load("PlayerRight.png")
                    Player = pygame.transform.scale(Player, (200,200))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Player = pygame.image.load("PlayerLeft.png")
                    Player = pygame.transform.scale(Player, (200,200))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Player = pygame.image.load("PlayerRight.png")
                    Player = pygame.transform.scale(Player, (200,200))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Player = pygame.image.load("PlayerUp.png")
                    Player = pygame.transform.scale(Player, (200,200))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Player = pygame.image.load("PlayerDown.png")
                    Player = pygame.transform.scale(Player, (200,200))
                





        PLayerrect = moveManual (Playerrect, speed, width)

        

        screen.blit(floor, (0,0))


        
        screen.blit(Player, Playerrect)
        screen.blit(Gun, Gunrect)
        pygame.display.flip()
        clock.tick(FPS)
            
