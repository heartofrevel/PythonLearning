import pygame
import sys
from pygame.locals import *
from time import sleep
from random import randrange

red = (255,0,0)
blue = (0,0,255)
yellow=(255,255,0)

direction = ["right", "left", "up", "down"]

pygame.init()

setDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("First Game")

img = pygame.image.load('evilSquare.png')

FPS=200
imgX = 20
imgY = 20
pixMove = 5

rand = randrange(0,3)
movement = direction[rand]
fpsTime = pygame.time.Clock()

while True:
	setDisplay.fill((0,0,0))
	if movement == 'down':
		imgY += pixMove
		if imgY > 500:
			img = pygame.transform.rotate(img, 90)
			movement = "right"

	elif movement == "right":
		imgX += pixMove
		if imgX > 700:
			img = pygame.transform.rotate(img, 90)
			movement = "up" 

	elif movement == "up":
		imgY -= pixMove
		if imgY < 50:
			img = pygame.transform.rotate(img, 90)
			movement = "left"

	elif movement == "left":
		imgX -= pixMove
		if imgX < 50:
			img = pygame.transform.rotate(img, 90)
			movement = "down"

	setDisplay.blit(img, (imgX, imgY))
	for event in pygame.event.get():
		print event
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsTime.tick(FPS)