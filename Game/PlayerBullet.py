import pygame
from spriteSheetToList import *

class PlayerBullet:
    def __init__ (self, position):
        self.image = pygame.image.load("PlayerBullet.png").convert_alpha()
        self.image = spriteSheetToList(self.image, 1)

        self.mask = pygame.mask.from_surface(self.image[0])
        self.rect = self.image[0].get_rect()
        self.rect.center = position

        self.speed = 10
        self.frames = 0
        self.animationSpeed = 10
        self.count = 0

    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)

    def update(self, FPS):
        self.rect.x -= self.speed

    def delete(self):
        if self.rect.bottom < 0:
            return True
        else:
            return False

    def collision (self, target):
        offset = (target.rect.left - self.rect.left), (target.rect.top - self.rect.top)
        if self.mask.overlap(target.mask, offset) != None:
            return True
        else:
            return False
        
