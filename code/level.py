from random import choice
import pygame
from pytmx.util_pygame import load_pygame
import json
from settings import *
from support import *
from tile import Tile
from player import Player
from npc import NPC
from debug import debug


class Level:
	"""This class represents an level of a game build by the included Game Engine
    """
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		self.tmx_data = load_pygame('./Tiled/Maps/Route_1.tmx')

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.sprite_group = pygame.sprite.Group()
		
		# NPC- Group
		self.NPCs = []
		
		# Get translation table for images (because in bigger sprite sheets, Tiled uses other names than in you in your graphics folder)
		with open('./graphics/translationtable.json', 'r') as f:
			self.translation_table = json.load(f)

		# sprite setup
		self.create_map()


	def create_map(self):
		"""_summary_
			Build map from extern files
		"""

		# Creating details from map
		layouts = {
			'flowers': import_csv_layout('./map/Route_1_Flowers.csv'),
			'trees': import_csv_layout('./map/Route_1_Trees.csv'),
			'stones': import_csv_layout('./map/Route_1_Stones.csv'),
			'decoration': import_csv_layout('./map/Route_1_Decoration.csv'),
		}
		graphics = {
			'flowers': import_folder('./graphics/flowers'),
			'trees': import_folder('./graphics/trees'),
			'stones': import_folder('./graphics/stones'),
			'decoration': import_folder('./graphics/decoration')
		}

		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'flowers':
							surf = graphics['flowers'][self.translation_table['flowers'][col]]
							Tile((x,y),[self.visible_sprites],'visible', surf)
						if style == 'trees':
							surf = graphics['trees'][self.translation_table['trees'][col]]
							Tile((x,y + TILESIZE),[self.visible_sprites,self.obstacle_sprites],'object',surf)
						if style == 'stones':
							surf = graphics['stones'][self.translation_table['stones'][col]]
							Tile((x,y + TILESIZE),[self.visible_sprites,self.obstacle_sprites],'object',surf)
						if style == 'decoration':
							# if col == 332 && season == winter, then draw snowman, otherwise skip
							# If it's winter, you can add to the translated image-number + 2 if the original col was 333 or 334 (winter and summer version of image available)
							surf = graphics['decoration'][self.translation_table['decoration'][col]]
							Tile((x,y + TILESIZE),[self.visible_sprites,self.obstacle_sprites],'object',surf)

		# Building with pytmx (buggy)
		# for layer in self.tmx_data.visible_layers:
		# 	if hasattr(layer, 'data'):
		# 		for x, y, surf in layer.tiles():
		# 			pos = (x * TILESIZE, y * TILESIZE)
		# 			Tile(pos = pos, surf = surf, groups = self.sprite_group)

		
		self.player = Player((250,100),[self.visible_sprites],self.obstacle_sprites)

		# Creating NPCs
		self.NPCs.insert(0, NPC((192, 64), 1, [self.visible_sprites,self.obstacle_sprites]))
		self.player.NPCs = self.NPCs


	def run(self):
		"""_summary_
			Updates Sprites and draw new frames for each game tick
		"""
		# update and draw the game
		self.visible_sprites.custom_draw(self.player, self.NPCs)
		self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
	"""_summary_

	:param pygame: Model of Pygames Sprite Groupes
	:type pygame: _pygame.sprite.Group
	"""
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('Tiled/Route_1.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self, player, NPCs):
		# Getting Data from current display (right data even after resize event)
		

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

		for npc in NPCs:      
			npc.draw_speech_bubble(self.offset)

