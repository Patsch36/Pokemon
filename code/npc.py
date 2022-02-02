import pygame 
from settings import *
import random

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, npc_number, groups):
        super().__init__(groups)
        grass_block = random.randint(0, 4)

        image_str = 'graphics/test/NPCs/Teenager_' + str(npc_number) + '.png'
        self.image = pygame.image.load(image_str).convert_alpha()

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = (self.rect.inflate(-20, -10))
        
        # Add layer
        self.image_layer = 1