import pygame, sys, math, random

class SideSpikeL():
    def __init__(self, Pos=[0,0]):
        self.image = pygame.image.load("Images/Enemies/side.png")
        self.rect = self.image.get_rect(center = Pos)
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        self.kind = "sidespikel"
        
    def update(self, size):
        pass
        

