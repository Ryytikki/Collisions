import pygame, sys
from pygame.locals import *
from player import Player
from vector_collisions import *

# Useful to have as a function
def load_image(name):
	image = pygame.image.load(name).convert_alpha()
	return(image)

def main():
	# Boring intialization stuff
	pygame.init()
	fpsclock = pygame.time.Clock()
	window_surface = pygame.display.set_mode((1336, 768))
	pygame.display.set_caption("Collision test")
	
	# Test map, entity map blank till i code the conversion system
	map_file = ["0000000300", "0010000250", "0020000250", "0040000450", "0060000450","006010001","1000000450"]
	entity_file = []
	
	black_colour = pygame.Color(0,0,0)
	
	# define the objects
	player = Player(1)
	player.rect[0] = 0
	map = Collision_map(map_file, entity_file, 1336)

	#window_surface.blit(player.image, (1,200))
	
	while True:
		# reset the screen
		window_surface.fill(black_colour)
		# Check for collisions
		map.ground_collision(player,[0,0])
		tracer = map.draw_map()
		# Apply gravity and update the screen
		window_surface.blit(tracer, (0,0))
		window_surface.blit(player.image, (player.rect[0] - 112, player.rect[1] - 125))
		player.rect[1] += 10
		player.update()
		pygame.display.update()
		fpsclock.tick(30)

if __name__ == '__main__':
	main()