import pygame, sys, math, random
from Game import *

def drawPlayer():
    global walkCount
    if walkCount  +1 >= 3:
        walkCount = 0
    if left:
        win.blit(walkLeft [walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight [walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit (char, (x, y))
        
    pygame.display.update()
