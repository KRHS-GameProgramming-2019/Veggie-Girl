import pygame, sys, math, random
from Player import *
from Items import *
from Levels import *
from Bosses import *
from SaltSpike import *
from Sounds import *
from Steak import *
from Tilesets import *

clock = pygame.time.Clock();

size = [900, 700]
screen = pygame.display.set_mode(size)


screen.fill((64, 128, 255))
pygame.display.flip()
clock.tick(60)
print(clock.get_fps())
