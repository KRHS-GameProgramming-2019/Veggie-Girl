import game, sys, math

def loadLevel (lev):
    f = open(lev, "r")
    lines = f.readlines()
    f.close()
    
    size = 25
    offset = size/2
    tiles = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
        
    lines = newLines
    
    
    for y, line in enumerate (lines):
        for x, c in enumerate (line):
            if c == "#":
                tiles += [Wall([x*size+offset, y*size+offset])]
                
    return tiles


#loadLevel("Levels/W1lL1.lvl")
