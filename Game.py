import sys, math, pygame, random
from Player import *
from Tilesets import *
from Sounds import *
from Levels import *
from Items import *
from Bosses import *
from SaltSpike import *
from Steak import *
pygame.init()

screenLength = 500
screenWidth = 500
win = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Veggie Girl")

walkLeft = [pygame.image.load("Images/Player/BroccoliL1final.png")]
walkRight = [pygame.image.load("Images/Player/BroccoliR1.png")]
char = pygame.image.load("Images/Player/Broccolistanding.png")

clock = pygame.time.Clock()

class player():
    def__init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
    
    def draw()


def redrawGameWindow():
	global walkCount

	win.fill((0, 0, 0))
	


	pygame.display.update()

veggie = player(300, 410, 40, 60)
run = True
while run:
	clock.tick(27)
	for event in pygame.event.get():
		if event == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and veggie.x > veggie.vel:
		veggie.x -= veggie.vel
		veggie.left = True
		veggie.right = False
	elif keys[pygame.K_RIGHT] and x < screenWidth - veggie.width - veggie.vel:
		veggie.x += veggie.vel
		veggie.left = False
		veggie.right = True
	else:
		veggie.right = False
		veggie.left = False
		veggie.walkCount = 0

	if not(isJump):
		if keys[pygame.K_SPACE]:
			veggie.isJump = True

			veggie.walkCount = 0
	else:
		if veggie.jumpCount >= -10:
			neg = 1
			if veggie.jumpCount < 0:
                neg = -1
			veggie.y -= (veggie.jumpCount ** 2) * 0.3 * neg
			veggie.jumpCount -= 1
		else:
			veggie.isJump = False
			veggie.jumpCount = 10

	redrawGameWindow()

pygame.quit()
