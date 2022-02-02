import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/test/rock_grassy.png').convert_alpha()		# Some IDE's need a ../ in path
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)

		# Add layer
		self.image_layer = 1