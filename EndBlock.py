import pygame, sys, math

class END():
    def __init__(self, Pos=[0,0]):
        self.image = pygame.image.load("Images/Tiles/end.png")
        self.rect = self.image.get_rect(center = Pos)
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        self.kind = "end"
        
    def update(self, size):
        pass
        
