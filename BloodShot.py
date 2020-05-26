import pygame, sys, math, random

class Bullet():
    def __init__(self, Pos=[0,0], rad, direction):
        self.image = pygame.image.load("Images/Enemies/bloodshot1.png")
        self.rect = self.image.get_rect(center = Pos)
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        self.direction = direction
        self.vel = 8 * direction
        self.kind = "bullet"
        
    def update(self, size):
        pass
        



