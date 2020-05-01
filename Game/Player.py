import pygame
from spriteSheetToList import *

class Player:
    def __init__ (self, speed, height, image, numcolums):
        self.image = pygame.image.load(image).convert_alpha()
        ##self.image = pygame.transform.scale(self.image,[55,55])
        self.image = spriteSheetToList(self.image, numcolums)

        self.mask = pygame.mask.from_surface(self.image[0])
        self.rect = self.image[0].get_rect()
        self.rect = height
        self.screenHeight = height
        self.speed = speed
        self.count = 0
        self.frames = 0
        self.animationSpeed = 10
        self.health = 3
        self.starttime = 9000000000

    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)

    def update(self, width, FPS):
        self.frames += 1
        if self.frames%(FPS / self.animationSpeed) == 0:
            self.count += 1
      
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x = self.rect.x - self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        
