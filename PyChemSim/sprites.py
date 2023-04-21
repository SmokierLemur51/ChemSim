"""
	Sprites are 2D pieces of art.

	Pygame Uses
		- Used to combine a surface, a rect and many additional features like animations or sound
		- 

	Drawing in pygame
		- Display surface object is the only thing displayed
		- Additional surfaces can be added but they need to be attached to the display surface

		- You cannot move an image by itself, YOU MUST PUT A RECT AROUND IT

		- You can combine multiple sprites in a group and interact with them together
		
"""

import pygame, sys

class Crosshair(pygame.sprite.Sprite):
	def __init__(self, width, height, pos_x, pos_y, color):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = [pos_x, pos_y] # draw it in the center


def get_resolution():
	info = pygame.display.Info()
	width, height = info.current_w, info.current_h
	return (width, height)


# == General Setup == 
pygame.init()
clock = pygame.time.Clock()

# == Screen == 
res = get_resolution()
screen = pygame.display.set_mode(res)

# == Crosshair == 
crosshair = Crosshair(50, 50, 100, 100, (255, 255, 255))

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)


# == Game Events == 
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()
	crosshair_group.draw(screen) # tell it the surface to draw on
	clock.tick(60)