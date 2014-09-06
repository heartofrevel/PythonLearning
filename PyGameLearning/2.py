import pygame
import sys
from pygame.locals import *


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
bg = black

fps = 30
dispWidth = 800
dispHeight = 600
cellSize = 10

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

def runGame():
	startX = 3
	startY = 3
	coords = [{'x':startX, 'y':startY}]
	direction = RIGHT

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				if event.key == (K_LEFT or K_a):
					direction = LEFT

				elif event.key == (K_RIGHT or K_d):
					direction = RIGHT

				elif event.key == (K_DOWN or K_s):
					direvtion = DOWN

				elif eventy.key == (K_UP or K_w):
					direction = UP

		if direction == UP:
			newCell = {'x':coords[0]['x'], 'y':coords[0]['y']-1}
