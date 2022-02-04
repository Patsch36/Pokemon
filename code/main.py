import pygame, sys
from pygame.locals import *		# Needed for resizable window (Especially for Constant RESIZABLE and VIDEOSIZE)
from settings import *
from level import Level

class Game:
	def __init__(self):
		  
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH), RESIZABLE)
		pygame.display.set_caption('Game V1.1')
		self.clock = pygame.time.Clock()

		self.level = Level()
	
	def run(self):
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
		width, height = event.size
		if width < WIDTH:  
			width = WIDTH
		if height < HEIGTH: 
			height = HEIGTH
		screen = pygame.display.set_mode((width, height), RESIZABLE)


if __name__ == '__main__':
	game = Game()
	game.run()