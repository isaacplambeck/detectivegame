import pygame, sys, math
from pygame.locals import *

pygame.init()

#setup the window with a 720p resolution and a title
winX, winY = 1280, 720
display = pygame.display.set_mode((winX, winY))
winTitle = pygame.display.set_caption("Game name")

#Colours
cBlack = (0, 0, 0)

#setup the clock and FPS limit
FPS = 60
clock = pygame.time.Clock()

#sprite groups
allSprites = pygame.sprite.Group()

#background image
bg = pygame.image.load("floor.jpg")

class Player(pygame.sprite.Sprite):
    def __init__(self, speed):
        #import the __init__ from the Sprite class
        pygame.sprite.Sprite.__init__(self)
        #sets the objects speed to the speed argument
        self.speed = speed
        #set the soldiers image
        self.image = pygame.image.load("Player.png")
        #get the rectangle of the image (used for movement later)
        self.rect = self.image.get_rect()
        #sets starting position
        self.rect.x, self.rect.y = winX/2, winY/2

    def checkPlayerMovement(self):
        """Check if user has pressed any movement buttons
            and sets the characters position accordingly."""
        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            self.rect.y -= self.speed
        if pressed[K_s]:
            self.rect.y += self.speed
        if pressed[K_a]:
            self.rect.x -= self.speed
        if pressed[K_d]:
            self.rect.x += self.speed

    def checkMouseMovement(self):
        """Check if user has moved the mouse and rotates the
            character accordingly."""
        mX, mY = pygame.mouse.get_pos()
        angleRad = math.atan2(self.rect.y-mY, mX-self.rect.x)
        angleDeg = math.degrees(angleRad)
        self.image = pygame.transform.rotate(self.image, angleDeg)

    def update(self):
        """Performs all movement and drawing functions and shit
            for the object"""
        self.checkPlayerMovement()
        self.checkMouseMovement()
        #draw the image at the given coordinate
        display.blit(self.image, (self.rect.x, self.rect.y))

def updateAll():
    #fill the window with black
    display.blit(bg, (0, 0))
    #update all sprites
    allSprites.update()
    #keeps FPS at 60
    clock.tick(FPS)
    #updates the display
    pygame.display.flip()

#creates a player with a speed of 5
mainChar = Player(5)
#add the player character to main sprite group
allSprites.add(mainChar)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    updateAll()
