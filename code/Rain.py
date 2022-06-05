"""
:author: Patrick Scheich
:name: level.py
:created: 3. Juni 2022
:description: Contains the graphical feature of rain for displaying weather data
"""

import pygame
import random
import logging

class Rain(pygame.sprite.Sprite):
    """Class of a single raindrop dripping down the window
    """
    def __init__(self):
        self. wn_width = 1600
        self.wn_height = 980
        pygame.sprite.Sprite.__init__(self)
        self.image = rain_img = pygame.image.load('./graphics/weather/rain.png')
        self.rect = self.image.get_rect()
        self.speedx = 3
        self.speedy = random.randint(5,25)
        self.rect.x = random.randint(-100,self.wn_width)
        self.rect.y = random.randint(-self.wn_height,-5)
        logging.debug("Created Rain")
        

    def update(self):
        """Calculating new raindposition for every tick (called in :meth:`level.Level.run`)
        """
        
        if self.rect.bottom > self.wn_height:
            self.speedx = 3
            self.speedy = random.randint(5,25)
            self.rect.x = random.randint(-self.wn_width,self.wn_width)
            self.rect.y = random.randint(-self.wn_height,-5)
            
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy   