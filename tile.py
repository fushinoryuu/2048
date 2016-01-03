import pygame
from pygame.locals import *
from random import randint

class Tile:
    """class that displays a graphical representation of a 6 sided die"""
    def __init__(self, surface, position, value, size):
        """This function defines some values of the die and where things should display."""
        self.surface = surface
        self.position = position
        self.value = value
        self.size = size

    def draw_tile(self):
        return

    def set_value(self, value):
        """This function helps us set a new value to the object."""
        self.value = value

    def draw_value(self, value):
        self.draw_tile()

    def display_tile(self):
        self.draw_value()