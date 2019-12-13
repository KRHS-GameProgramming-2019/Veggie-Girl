import sys, math, pygame, random
pygame.init()

clock = pygame.time.Clock()

x = 5
y = 425
height = 60
width = 40
screenLength = 500
screenWidth = 500
vel = 5
left = False
right = False
jumpCount = 10
isJump = False
walkCount = 0

win = pygame.display.set_mode((screenLength, screenWidth))
pygame.display.set_caption("Veggie Girl")

walkLeft = [pygame.image.load("Images/Player/BroccoliL1final.png")]
walkRight = [pygame.image.load("Images/Player/BroccoliR1.png")]
char = pygame.image.load("Images/Player/Broccolistanding.png")

def redrawGameWindow():
	global walkCount

	win.fill((0, 0, 0))
	
	if walkCount + 1 >= 3:
		walkcount = 0
	if left:
		win.blit(walkLeft[walkCount//1000], (x, y))
		walkCount += 1
	elif right:
		win.blit(walkRight[walkCount//1000], (x, y))
		walkCount += 1
	else:
		win.blit(char, (x, y))

	pygame.display.update()


run = True
while run:
	clock.tick(27)
	for event in pygame.event.get():
		if event == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
		left = True
		right = False
	elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
		x += vel
		left = False
		right = True
	else:
		right = False
		left = False
		walkCount = 0

	if not(isJump):
		if keys[pygame.K_SPACE]:
			isJump = True

			walkCount = 0
	else:
		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.3 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10

	redrawGameWindow()

pygame.quit()
