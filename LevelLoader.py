import pygame, sys, math
from Wall import *
from Ground import *
from Dirt import *
from EndBlock import *
from SaltSpike import *
from SideSpikeL import *
from SideSpikeR import *
from Floor import *
from CobbleWall import *
from FallBlock import *
from Steak import *

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
    steaks = []
    fallblocks = []
    saltspikels = []
    saltspikers = []
    sidespikes = []
    cobbles = []
    ends = []
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
            if c == "W":
                tiles += [Cobbled([x*size+offset, y*size+offset])]
            if c == "O":
                tiles += [END([x*size+offset, y*size+offset])]
            if c == "S":
                tiles += [Steak([x*size+offset, y*size+offset - 5])]
    
            if c == "C":
                playerPos += [x*size+offset, y*size+offset]
    
    return tiles, playerPos
