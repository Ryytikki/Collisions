import pygame, sys, math, os
from pygame.locals import *
	
def load_image(name):
	full_path = os.path.dirname(os.path.realpath(sys.argv[0]))
	image = pygame.image.load(full_path + "\\"+ name).convert_alpha()
	return(image)
	
class Player(pygame.sprite.Sprite):

	def __init__(self, ID):
		pygame.sprite.Sprite.__init__(self)		
		
		self.image = load_image("blob.png")
		self.rect = self.image.get_rect()
		self.rect.center = (20.0, 500.0)
	
		self.x_direction = 0
		self.speed = 10
		
	def update(self):
		self.keyboard_controls()
		
	def keyboard_controls(self):
		# Keyboard controls
		for event in pygame.event.get():
			# Quits the program
			if event.type == QUIT:
				pygame.quit()
			
			# Key press handling
			if event.type == KEYDOWN:
				# If escape is pressed, close
				if event.key == K_ESCAPE:
					pygame.event.post(pygame.event.Event(QUIT))
				
				# X movement
				if event.key == K_a:
					self.x_direction = -1
					
				if event.key == K_d:
					self.x_direction = 1
						
			# Key release hadling
			if event.type == KEYUP:
				# Refreshes the events
				pygame.event.pump()
				# Creates a list of pressed keys
				key_list = pygame.key.get_pressed()
				# If A is up
				if event.key == K_a:
					# But D is down
					if key_list[pygame.K_d] == True:
						# Swap directions
						self.x_direction = 1
					# But D is up
					else:
						# Stop moving
						self.x_direction = 0
				# Same for D
				if event.key == K_d:
					if key_list[pygame.K_a] == True:
						self.x_direction = -1
					else:
						self.x_direction = 0
						
		self.rect[0] += self.speed * self.x_direction			
