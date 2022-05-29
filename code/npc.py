import pygame 
from settings import *
import random
from NPC_data import *
from debug import debug


class NPC(pygame.sprite.Sprite):
    def __init__(self, NPCID, npc_number, groups):
        super().__init__(groups)
        
        language = 'en'
        
        path = "code//npc_data.db"
        self.npc_data = NPC_data(path, language)
        pos = self.npc_data.get_position(NPCID) 

        image_str = 'graphics/test/NPCs/Teenager_' + str(npc_number) + '.png'
        self.image = pygame.image.load(image_str).convert_alpha()

        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = (self.rect.inflate(-20, -10))

        self.interaction = False

        self.textcounter = 0
        self.textsnippets = 3
        self.texts = []
        count = self.npc_data.get_dialog_length(NPCID)
        self.textsnippets = count
        i = 1
        for i in range(count):
            self.texts += self.npc_data.get_dialog(NPCID, (i+1)) 

        self.pos = pygame.Vector2()
        self.pos.x = pos[0]//TILESIZE
        self.pos.y = pos[1]//TILESIZE

        self.npc_data.close()
        
    def draw_speech_bubble(self, offset):

        screen = pygame.display.get_surface()
        pos = self.rect.midtop - offset
        if self.textcounter < self.textsnippets:
            text = self.texts[self.textcounter]
        
        size = 20

        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(midbottom=pos)

        # background
        bg_rect = text_rect.copy()
        bg_rect.inflate_ip(5, 5)

        # Frame
        frame_rect = bg_rect.copy()
        frame_rect.inflate_ip(2, 2)

        if self.interaction == True:
            pygame.draw.rect(screen, (0, 0, 0), frame_rect)
            pygame.draw.rect(screen, (255, 255, 255), bg_rect)
            screen.blit(text_surface, text_rect)

    def speak(self):
        if self.interaction == False:
            self.interaction = True
        elif self.textcounter < self.textsnippets - 1:
            self.textcounter += 1
        else:
            self.interaction = False
            self.textcounter = 0
    
    def position(self):
        return self.pos.x, self.pos.y