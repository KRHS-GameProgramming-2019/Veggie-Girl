import pygame, sys, math

def loadLevel (lev):
    f = open(lev, "r")
    lines = f.readlines()
    f.close()
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
        
    lines = newLines
    
    print(lines)

loadLevel("Levels/W1lL1.lvl")
