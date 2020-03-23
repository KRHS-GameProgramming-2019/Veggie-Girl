import pygame, sys, math

class VineWall():
    def __init__(self, Pos=[0,0]):
        self.image = pygame.image.load("Images/Tiles/VinesWall.png")
        self.rect = self.image.get_rect(center = Pos)
        
        self.kind = "wall"
        
    def update(self, size):
        pass
        
