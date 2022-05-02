import pygame 
from settings import *
from support import import_folder
from debug import debug
from npc import *

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/test/player.png').convert_alpha()		# Some IDEs need a ../ in path
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-26)


		# screen data
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.Vector2()



		# graphics setup
		self.import_player_assets()
		self.status = 'down'
		self.frame_index = 0
		self.animation_speed = 0.07

		self.direction = pygame.math.Vector2()
		self.speed = 2
		self.obstacle_sprites = obstacle_sprites

		# list of all npcs to interact with
		self.NPCs = []
		self.speak = False

		# flags for pressed keys
		self.space_pressed = False


	def import_player_assets(self):
		character_path = 'graphics/red/'
		self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		keys = pygame.key.get_pressed()

		# movement input
		if not self.speak:
			if keys[pygame.K_UP]:
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_DOWN]:
				self.direction.y = 1
				self.status = 'down'
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT]:
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_LEFT]:
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0

		if keys[pygame.K_SPACE]:
			if self.space_pressed == False:
				self.space_pressed = True
				pos = self.rect.topleft
				posx= pos[0] // TILESIZE
				posy = pos[1]// TILESIZE
				pos = [posx, posy]
				for npc in self.NPCs:
					# Always check 2 position: because if player stands 1px to far away from tile, it looks like he stands in front of npc but technically he's on another tile
					if (self.status == 'up' or self.status == 'up_idle') and ((npc.pos + (0, 1)) == pos or (npc.pos + (-1, 1)) == pos):
						npc.speak()
						self.speak = npc.interaction
					# For some reason, npc is 2 tiles beneath the player when talking from above (not when talking from beneath, lol)
					elif (self.status == 'down' or self.status == 'down_idle')  and ((npc.pos - (0, 2)) == pos or (npc.pos - (1, 2)) == pos):
						npc.speak()
						self.speak = npc.interaction
					# For some reason, npc is 2 tiles right the player when talking from left (not when talking from right, lol)
					elif (self.status == 'right' or self.status == 'right_idle') and (npc.pos - (2, 0) == pos):
						npc.speak()
						self.speak = npc.interaction
						npc.draw_speech_bubble(self.offset)
					# standing right, but looking left so left_idle (reverse thinking other than above, brainfuck and half an hour debug lol)
					elif (self.status == 'left' or self.status == 'left_idle')  and (npc.pos + (1, 0) == pos):
						npc.speak()
						self.speak = npc.interaction
					break
		else:
			self.space_pressed = False


	def get_status(self):

		# idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status:
				self.status = self.status + '_idle'

	def move(self,speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center
		

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def animate(self):
		animation = self.animations[self.status]

		# loop over the frame index 
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# set the image
		if self.frame_index <= len(animation):
			self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

	def update(self):
		self.input()
		self.get_status()
		self.animate()
		self.move(self.speed)
