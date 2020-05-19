import pygame, sys, math
from Wall import *
from Ground import *
from Dirt import *
from SaltSpike import *
from SideSpikeL import *
from SideSpikeR import *
from Floor import *
from FallBlock import *

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
    floors = []
    fallblocks = []
    saltspikels = []
    saltspikers = []
    sidespikes = []
    playerPos = []
    
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
                tiles += [VineWall([x*size+offset, y*size+offset])]
            if c == "G":
                tiles += [Ground([x*size+offset, y*size+offset])]
            if c == "D":
                tiles += [Dirt([x*size+offset, y*size+offset])]
            if c == "F":
                tiles += [Floor([x*size+offset, y*size+offset])]
            if c == "J":
                tiles += [FallBlock([x*size+offset, y*size+offset])]
            if c == "^":
                tiles += [SaltSpike([x*size+offset, y*size+offset + 4])]
            if c == "<":
                tiles += [SideSpikeL([x*size+offset, y*size+offset])]
            if c == ">":
                tiles += [SideSpikeR([x*size+offset, y*size+offset])]
    
            if c == "C":
                playerPos += [x*size+offset, y*size+offset]
    
    # ~ tiles = [walls, grounds, dirts, saltspikes, sidespikels, fallblocks, floors, playerPos]
    return tiles, playerPos

#loadLevel("Levels/W1lL2.lvl")
