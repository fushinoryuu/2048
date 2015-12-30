import pygame
from pygame.locals import *
from random import randint

class Tile:
    """class that displays a graphical representation of a 6 sided die"""
    def __init__(self, size, surface, position):
        """This function defines some values of the die and where things should display."""
        self.SURF = surface
        self.POS = position
        self.VALUE = 1
        self.SIZE = size

        self.TILESURF = pygame.Surface((size, size), flags=SRCALPHA, depth=32)
        self.TILESURF.fill((0, 0, 0, 0))