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
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.maxSpeed = 5 
        self.speed = [self.speedx, self.speedy] = [0,0] 
        self.animationTimer = 0 
        self.animationTimerMax = 60/10 
        self.floor = self.rect.bottom 
        self.gravity = 1 
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def animate(self):
        if self.animationTimer >= self.animationTimerMax:
            self.animationTimer = 0
            if self.frame >= self.maxFrame:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]
    
    def update(self):
        
        self.move()
        self.animate()
        
        if self.isJump:
            if self.rect.bottom <= self.floor:
                self.speedy += self.gravity
            else: 
                self.isJump = False 
                self.speedy = 0 
                self.rect.bottom = self.floor 
    
    def jump(self): 
        if not self.isJump:
            self.isJump = True 
            self.speedy = -2 * self.maxSpeed; 
        
    def go(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.images = self.walkLeftImages
            self.maxFrame = len(self.images)-1
            self.frame = 0
        elif direction == "right":
            self.speedx = self.maxSpeed
            self.images = self.walkRightImages
            self.maxFrame = len(self.images)-1
            self.frame = 0
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        
