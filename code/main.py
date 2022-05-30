import pygame
import sys
# Needed for resizable window (Especially for Constant RESIZABLE and VIDEOSIZE)
from pygame.locals import *
from settings import *
from level import Level
import logging
from support import initLogger, getLogger


class Game:
    """
    This class represents the game itself
    It instantiates class:`Level`

    Attributes:
            screen: Pygame Screen (Window Screen)

            clock: Pygame clock for Framerate

            level: Current, playable level
    """

    def __init__(self):
        logging.basicConfig(filename='./code/game.log', level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y:%H:%M:%S')

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH), RESIZABLE)
        pygame.display.set_caption('Game V1.1')
        self.clock = pygame.time.Clock()

        self.level = Level()

        logging.info("Initialized Game")

    def run(self):
        """Mainloop with standard event-handling of window events.
                Configuration ogf Game settings.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
