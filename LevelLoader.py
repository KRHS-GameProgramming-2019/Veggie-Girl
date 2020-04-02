import pygame, sys, math
from Wall import *
from Ground import *
from Dirt import *

def loadLevel (lev):
    f = open(lev, "r")
    lines = f.readlines()
    f.close()
    
    size = 25
    offset = size/2
    tiles = []
    walls = []
    grounds = []
    dirts = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
        
    lines = newLines
    
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls += [VineWall([x*size+offset, y*size+offset])]
            if c == "G":
                grounds += [Ground([x*size+offset, y*size+offset])]
            if c == "D":
                dirts += [Dirt([x*size+offset, y*size+offset])]
    
    tiles = [walls, grounds, dirts]
    return tiles

#loadLevel("Levels/W1lL1.lvl")
