import pygame, sys, math, random



class Player():
    def __init__(self, pos):
        self.walkLeftImages = [pygame.image.load("Images/Player/BroccoliL1final.png")]
        self.walkRightImages = [pygame.image.load("Images/Player/BroccoliR1.png")]
        self.standImages = [pygame.image.load("Images/Player/Broccolistanding.png")]
        self.images = self.standImages
        self.frame = 0
        self.maxFrame = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(bottomleft = pos)
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    
    def move(self):
        pass
    
    def go(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.images = self.walkLeftImages
            self.maxFrame = len(self.images)-1
            self.frame = 0
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.images = self.imagesRight
            self.maxFrame = len(self.images)-1
            self.frame = 0
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        
