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
        #self.vel = 5 #redudnant variable? -CS
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.maxSpeed = 5 #set max speed to number, not golbal variable -CS
        self.speed = [self.speedx, self.speedy] = [0,0] #inline creation and assignment of speed, speedx -CS
        
        self.floor = self.rect.bottom # I need something to keep me from falling once I jump. This will go away (I think?) once you have blocks
        
        self.gravity = 1 #Gravity for basic kinematic physics model -CS
    
    def move(self):
        # You don't have any code in here! 
        # Inserting default code from ball demo. -CS
        
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def update(self):
        # default update function from ball demo -CS
        self.move()
        
        # how I'd do a jump, at least the basic -CS
        if self.isJump:
            if self.rect.bottom <= self.floor :
                self.speedy += self.gravity
            else:
                self.isJump = False
                self.speedy = 0
                self.rect.bottom = self.floor
    
    def jump(self): #just spitballing a basic jump -CS
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
        
