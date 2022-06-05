"""
:author: Patrick Scheich
:name: Level.py
:created: 3. Mai 2022
:description: Contains the Game class representing the basic game as also the main function which is starting the application
"""

import pygame
import sys
# Needed for resizable window (Especially for Constant RESIZABLE and VIDEOSIZE)
from pygame.locals import *
import logging

from settings import *
from level import Level
from support import test_modules_installed, modules_to_install
from game_stats import game_stats


class Game:
    """
    This class represents the game itself
    It instantiates class:`Level`.
    It contains basic Game mechanics and data management for the game

    Attributes:
            screen: Pygame Screen (Window Screen)

            clock: Pygame clock for Framerate

            level: Current, playable level
    """

    def __init__(self):
        with open('./code/game.log', 'r+') as f:
            f.truncate(0)
        # logging.basicConfig(filename='./code/game.log', level=logging.DEBUG,
        #                     format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y:%H:%M:%S')
            logging.basicConfig(filename='./code/game.log', level=logging.INFO,
                             format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y:%H:%M:%S')


        # test_modules_installed(modules_to_install)
        game_stats.create_gamedata()

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH), RESIZABLE)
        pygame.display.set_caption('Game V1.1')
        self.clock = pygame.time.Clock()

        self.level = Level((game_stats.game_data["player_position"]["player_position_x"] * TILESIZE, game_stats.game_data["player_position"]["player_position_y"] * TILESIZE))

        logging.debug("Player status: (" + str(self.level.player.rect.topleft[0] / TILESIZE) + ", " + str(self.level.player.rect.topleft[1] / TILESIZE) + ")")

        logging.info("Initialized Game")

    def run(self):
        """Mainloop with standard event-handling of window events.
                Configuration ogf Game settings.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    game_stats.add_played_time()
                    game_stats.set_player_position(self.level)
                    game_stats.save_stats()

                    pygame.quit()
                    sys.exit()

            if event.type == VIDEORESIZE:
                self.resize_window(event)

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(120)

    def resize_window(self, event):
        """Sets new window size on resize event.

        :param event: Pygame resie event, has new windo size on x and y coordinate
        :type event: pygame.event
        """
        width, height = event.size
        if width < WIDTH:
            width = WIDTH
        if height < HEIGTH:
            height = HEIGTH
        screen = pygame.display.set_mode((width, height), RESIZABLE)

if __name__ == '__main__':
    game = Game()
    game.run()
