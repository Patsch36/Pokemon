import pygame 
from settings import *
import random

class Grass(pygame.sprite.Sprite):
    def __init__(self, pos, groups, background = False):
        super().__init__(groups)
        grass_block = random.randint(0, 4)

        if not background:
            if grass_block < 3:
                self.image = pygame.image.load('graphics/test/grass_1.png').convert_alpha()		# Some IDE's need a ../ in path
            elif grass_block == 3:
                self.image = pygame.image.load('graphics/test/flower_1.png').convert_alpha()		# Some IDE's need a ../ in path
            elif grass_block == 4:
                self.image = pygame.image.load('graphics/test/flower_1_1.png').convert_alpha()		# Some IDE's need a ../ in path
        else:
            self.image = pygame.image.load('graphics/test/grass_1.png').convert_alpha()		# Some IDE's need a ../ in path

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = (self.rect.inflate(-64, -64))
        
        # Add layer
        self.image_layer = 0