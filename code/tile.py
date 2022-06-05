import pygame 
from settings import *

class Tile(pygame.sprite.Sprite):
	"""Replaces a sprite tile in the game and draws it on the screen

	:param pos: position on the surface in n * settings.TILESIZE
	:type pos: int
	:param groups: sprite group of the tile
	:type groups: pygame.sprite.Group
	:param sprite_type: type of the sprite (legacy)
	:type sprite_type: String
	:param surface: surface on which the sprite should be drawn, defaults to pygame.Surface((TILESIZE,TILESIZE))
	:type surface: pygame.Surface, optional
	"""
	def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
		super().__init__(groups)
		self.sprite_type = sprite_type
		self.image = surface
		if sprite_type == 'object':
			self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE))
		else:
			self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)