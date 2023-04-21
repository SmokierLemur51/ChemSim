import pygame


def get_resolution():
	information = pygame.display.Info()
	res = (information.current_w, information.current_h)
	return res


def draw_background(screen, color):
	return screen.fill(color)



# remove obj oriented and just make it functions
class Plant:

	def __init__(self, screen, color, size):
		self.color = color 
		self.size = size
		self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

		self.nutrients = {
			"water_value": 50,
			"nutrient_value": 50,
		}

		pygame.draw.circle(screen, self.color, self.player_pos, self.size)

	def feed_plant(self):
		self.nutrients["nutrient_value"] += 25

	def water_plant(selfda):
		self.nutrients["water_value"] += 25

	def grow(self):
		if (self.nutrients["water_value"] >= 100) and (self.nutrients["nutrient_value"] >= 75):
			self.size += (self.size / 2)
		else:
			print(False)

def main():
	# pygame setup
	pygame.init()

	resolution = get_resolution()
	screen = pygame.display.set_mode(resolution)
	clock = pygame.time.Clock()
	running = True
	dt = 0

	# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

	while running:
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			draw_background(screen, "brown")

			plant = Plant(screen, "green", 40)

			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				player_pos.y -= 300 * dt

			if keys[pygame.K_s]:
				player_pos.y += 300 * dt

			if keys[pygame.K_a]:
				player_pos.x -= 300 * dt

			if keys[pygame.K_d]:
				player_pos.x += 300 * dt

			if keys[pygame.K_SPACE]:
				plant.feed_plant()
				plant.water_plant()
				plant.grow()


			# flip the display to put your work on screen
			pygame.display.flip()

			''' dt is delta time in seconds since last frame, used for
			 	limits fps to 60
			 	framerate-independant physics
			'''
			dt = clock.tick(60) / 1000

	pygame.quit()

main()