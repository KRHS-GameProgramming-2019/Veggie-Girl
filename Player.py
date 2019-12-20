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
        
        self.gravity = 1 #Gravity for basic kinematic physics model, can be tuned for feel -CS
    
    def move(self):
        # You don't have any code in here! 
        # Inserting default code from ball demo. -CS
        
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def update(self):
        # default update function from ball demo -CS
        self.move()
        
        # how I'd do a jump, at least the basic -CS
        if self.isJump: #Are we jumping? 
            if self.rect.bottom <= self.floor: #Have we hit the floor?
                self.speedy += self.gravity #Add gavity to the speed each round. Oddly adding a positve gavity slows you down going up since positve y is down. Each round the self.speedy gets less negative until it hits zero then it goes positive at an increasing rate until you hit the ground. This is based on basic projectile motion kinematics, but it actually reflects how the world works.
            else: #We've hit/passed through the floor
                self.isJump = False #Stop jumping
                self.speedy = 0 #No really, stop jumping
                self.rect.bottom = self.floor #Put us on the floor since we might have passed through it.
    
    def jump(self): #just spitballing a basic jump. I put it in it's own function to keep the code clean and allow to re-implent it if you want to. It might be best to move this code into the go method when direction is "jump" -CS
        if not self.isJump: #prevents multi-jumps
            self.isJump = True #Hey we're jumping here!
            self.speedy = -2 * self.maxSpeed; #you move -speedy to jump and I scaled it by 2 since it was more of a hop at just -self.maxSpeed
        
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
        
