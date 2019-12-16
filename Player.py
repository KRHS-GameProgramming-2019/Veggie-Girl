import pygame, sys, math, random
from Game import *

walkLeft = [pygame.image.load("Images/Player/BroccoliL1final.png")]
walkRight = [pygame.image.load("Images/Player/BroccoliR1.png")]
char = pygame.image.load("Images/Player/Broccolistanding.png")

class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//1000], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//1000], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))
