import pygame 
   
pygame.init() 

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
black = (0, 0, 0)
red = (225, 0, 0)

X = 400
Y = 400
  
display_surface = pygame.display.set_mode((X, Y )) 

pygame.display.set_caption('Show Text') 
 
font = pygame.font.Font('freesansbold.ttf', 32) 
 
text = font.render("Veggie Girl", True, black) 
  
textRect = text.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (X // 2, Y // 2) 

  

while True : 
  

    display_surface.fill(white) 
  
    # copying the text surface object 
    # to the display surface object  
    # at the center coordinate. 
    display_surface.blit(text, textRect) 
  

    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            pygame.quit()
            quit() 
  
  
        pygame.display.update()
