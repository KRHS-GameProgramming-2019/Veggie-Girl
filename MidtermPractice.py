import pygame, sys, math

class Ball():
    def __init__(self, fastness = [1,1], starting = [0,0]):
        self.picture = pygame.image.load("Images/Player/Broccolistanding.png")
        
    def moveSelf(self):
        pass 
        
    def hitWall(self, size):
        pass
        
    def hitOtherBall(self, otherBall):
        pass
        
pygame.init()

clock = pygame.time.Clock()

width = 600
height = 400
size = width, height

screen = pygame.display.set_mode(size)

ball = Ball([3,3], [width/2, height/2])

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
    
    ball.moveSelf()
    ball.hitWall(size)
    
    screen.fill((0,0,0))
    screen.blit(ball.picture, ball.rectangle)
    pygame.display.flip() 
    clock.tick(60)
