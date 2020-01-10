import pygame, sys, random, math 
pygame.init() 


font = pygame.font.Font('freesansbold.ttf', 32) 
 
text = font.render("Veggie Girl", True, black) 
  
textRect = text.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (X // 2, Y // 2) 

class title_screen():
	def __init__(self):
		self.white = (225, 225, 225)
		self.black = (0, 0 ,0)
		self.green = (0, 225, 0)
		self.blue = (0, 0, 225)
		self.red = (225, 0, 0)
		self.y = 500
		self.x = 500

