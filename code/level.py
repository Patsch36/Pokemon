import pygame 
from settings import *
from tile import Tile
from grass import Grass
from player import Player
from npc import NPC
from debug import debug

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		for row_index,row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					# Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
					#Grass((x,y),[self.visible_sprites], background=True)
					pass
				if col == 'p':
					self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
					#Grass((x,y),[self.visible_sprites], background=True)
				if col == ' ':
					#Grass((x,y),[self.visible_sprites])
					pass

		NPC((192, 64), 1, [self.visible_sprites,self.obstacle_sprites])	


	def run(self):
		# update and draw the game
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('Tiled/Route_1.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)


		# for sprite in self.sprites():
		sprites = sorted(self.sprites(),key = lambda sprite: sprite.rect.centery)
		for sprite in sorted(sprites,key = lambda sprite: sprite.image_layer):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
