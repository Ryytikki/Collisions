import pygame
from pygame.sprite import *
###############################################################
# Vector based collision system built for cocos2d by Ryytikki #
# Made of 2 parts, the ground map and the entity map          #
# You need to reconvert the map every time it changes with    #
# the convert_map and convert_entities functions. I split     #
# them on the offchance that you'll only want to update one   #
# In this case, entities refer to non-ground platforms or     #
# other floating objects you can stand on                     #
###############################################################

class collision_map():
	
	def __init__(self, map_file, entity_file, screen_width):	
	
		# Need screen width for later optimisatio
		self.screen_width = screen_width
		
		# Holding arrays for the collision map
		self.x_coord = []
		self.y_coord = []
		# Min/max IDs of the vectors currently on the screen
		self.map_range = [0,0]
		
		# Current location of the collision map
		self.location = [0,0]
		
		self.convert_map(map_file)
		#convert_entities(map_file)
		

	
	def convert_map(self, map_file):
		# Convert the collision map to an array of floats
		i = -1
		coord = ""
		for coord in map_file:
			i += 1
			# Coordinates stored as strings allows you to hold more info, max coordinate (99999,99999)
			self.x_coord.append(float(coord[:5]))
			self.y_coord.append(float(coord[5:]))
		# Reset size of the range
		self.x_coord.append(999999999)
		self.y_coord.append(999999999)
		self.map_range[0] = 0
		self.map_range[1] = i 
		
	#	self.calc_offset()
		
		
	def calc_offset(self):
		# Calculates the range of vectors that are currently displayed on the screen
		# You wanna run this every time the position of the player is updated
		
		# Left hand side
		# TODO - Correct conditions to not fuck up
		if self.x_coord[self.map_range[0] + 1] + self.location[0] < 0:
			self.map_range[0] += 1
			# itterates until everything is done
			self.calc_offset()
		elif self.x_coord[self.map_range[0] - 1] + self.location[0] > 0:
			self.map_range[0] -= 1
			self.calc_offset()
		
		# Right hand side
		if self.x_coord[self.map_range[1] - 1] + self.location > self.screen_width:
			self.map_range[1] += 1
			self.calc_offset()
		elif self.x_coord[self.map_range[1] + 1] + self.location < self.screen_width:
			self.map_range[1] -= 1
			self.calc_offset()
		
	
	def ground_collision(self, target):
		
		# basic counter for the loops
		i = -1
		
		# Location of the vector under the target in the above arrays
		array_ID = 0

		gradient = 0.0
		vector_y = 0.0
		dy = 0.0
		
		# Now to find the vector that the target is over
		i = self.map_range[0]	
		for i in range(self.map_range[0], self.map_range[1]):
			if target.rect[0] >= self.x_coord[i]:
				if target.rect[0] < self.x_coord[i+1]:
					print(i)
					array_ID = i

		# Calculate the gradient of the vector (dy/dx)
		gradient = (self.y_coord[array_ID+1] - self.y_coord[array_ID]) / (self.x_coord[array_ID + 1] - self.x_coord[array_ID])
		# Then use that to calculate the height of the vector where the target is
		vector_y = gradient * (target.rect[0]- self.x_coord[array_ID]) + self.y_coord[array_ID]
		# And finally  calculate the displacement, if any is needed
		if target.rect[1]> vector_y:
			dy = target.rect[1]- vector_y
		# This can be applied to the target to move them above the map
		target.rect[1]-= dy
