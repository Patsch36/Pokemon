"""
:author: Patrick Scheich
:name: debug.py
:created: 2. Mai 2022
:description: Contains helper function for debugging
"""

import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10):
	"""Shows a debug message at the top left of the window for faster debugging on quick changing data

	:param info: Text that should be displayed as debug message
	:type info: string
	:param y: y position of text to display at, defaults to 10
	:type y: int, optional
	:param x: x position of text to display at, defaults to 10
	:type x: int, optional
	"""
	display_surface = pygame.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)
