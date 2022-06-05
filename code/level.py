"""
:author: Patrick Scheich
:name: level.py
:created: 3. Mai 2022
:description: Contains the level class

"""


from random import choice
from weather import *
import pygame
from pytmx.util_pygame import load_pygame
import json
from settings import *
from support import *
from tile import Tile
from player import Player
from npc import NPC
from debug import debug
from NPC_data import NPC_data
import logging
from Rain import Rain


class Level:
	"""Levelclass manages all level content and specific level data for the game such as graphical features or game content. Everything the player could do belongs in here

	:param player_position: Positin to place the player (mainly because managed from game_stats)
	:type player_position: tuple of (int, int)

	Attributes:
		level_name: String : Name of the level

		__player_position: tuple(int, int) : Intial Position of player, only needed for creating the player lateron

		display_surface: pygame.display : Game window for graphical manipulation

		tmx_data:file Object: data of tmx- File of od level, currently not used because of buggx version of library, not fixed yet

		raingroup: pygame.sprite.Group : all the rain effects that should only displayed on the rain condition

		NPCs[]: list<NPPC> : Contains all NPCs the player should can talk to, is checked on space_key_pressed

		weatherapp: Weather : object for getting all the weather specific data

		weathercode: String : Weather code saveed for only making the request once not every tick

		is_snowy: Bool : Contains value wether winter specific objects should be shown (Like snowmen)

    """

	def __init__(self, player_position):

		self.level_name = "MainLevel"
		self.player_position = player_position

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		self.tmx_data = load_pygame('./Tiled/Maps/Route_1.tmx')

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()
		self.sprite_group = pygame.sprite.Group()
		self.raingroup = pygame.sprite.Group()
		
		# NPC- Group
		self.NPCs = []
		
		# Get translation table for images (because in bigger sprite sheets, Tiled uses other names than in you in your graphics folder)
		with open('./graphics/translationtable.json', 'r') as f:
			self.translation_table = json.load(f)


		self.weatherapp = Weather()
		# Test rain through manipulating weather code (for example 1180)
		self.weathercode = self.weatherapp.get_weather_code()
		# Test snowing thorugh manipulating this (setting true)
		self.is_snowy = self.weatherapp.getSnow()
		for weather_amount in range(15):
			self.raingroup.add(Rain())
		
		logging.debug("Weather Code:" + str(self.weathercode))
		logging.debug("Is snowy:" + str(self.is_snowy))

		# sprite setup
		self.create_map()
  


	def create_map(self):
		"""Build map from extern files through reading the csv- files and building up the graphic tiles.
		
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
							drawTile = True
							# if col == 332 && season == winter, then draw snowman, otherwise skip
							if col == '332' and not(self.is_snowy):
								drawTile = False
							# If it's winter, you can add to the translated image-number + 2 if the original col was 333 or 334 (winter and summer version of image available)
							adder = 0
							logging.debug("self.weatherapp.getSnow" + str(self.weatherapp.getSnow()))
							if (col == '333' and self.weatherapp.getSnow()) or (col == '334' and self.weatherapp.getSnow()):
									adder =  2

							if drawTile:
								surf = graphics['decoration'][self.translation_table['decoration'][col] + adder]
								logging.debug("Current Wetter- Image- Code: " + str(self.translation_table['decoration'][col] + adder))
								Tile((x,y + TILESIZE),[self.visible_sprites,self.obstacle_sprites],'object',surf)

		# Building with pytmx (buggy)
		# for layer in self.tmx_data.visible_layers:
		# 	if hasattr(layer, 'data'):
		# 		for x, y, surf in layer.tiles():
		# 			pos = (x * TILESIZE, y * TILESIZE)
		# 			Tile(pos = pos, surf = surf, groups = self.sprite_group)

		
		logging.info("Created Map")

		self.player = Player(self.player_position,[self.visible_sprites],self.obstacle_sprites)

		# Creating NPCs T
		NPC_number = NPC_COUNTER
		sprites = [self.visible_sprites,self.obstacle_sprites]
		for i in range(NPC_number):
			self.NPCs.insert(i, NPC((i+1), 1, sprites))
		self.player.NPCs = self.NPCs

		logging.info('Created Player and NPCs')


	def run(self):
		"""Updates Sprites and draw new frames for each game tick
		
		"""
		# update and draw the game
		self.visible_sprites.custom_draw(self.player, self.NPCs)
		self.visible_sprites.update()
		if self.weathercode in [1180, 1183, 1186, 1189, 1192, 1195, 1198, 1201]:
			self.raingroup.update()
			self.raingroup.draw(pygame.display.get_surface())


class YSortCameraGroup(pygame.sprite.Group):
	"""New Camera Rendering

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
		"""Custom draw method for noting Y- Positions for realitic 3D Graphic.

		:param player: Player of the Game
		:type player: class:`player`
		:param NPCs: List of all NPCS
		:type NPCs: class:`pygame.sprite.Group()`
		"""
		
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

