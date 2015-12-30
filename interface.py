import pygame
from pygame.locals import *
from button_class import SimpleButton

pygame.init()

class GameInterface:
    """This class represents the interface for the game's menu."""
    def __init__(self):
        self.display_width = 1080
        self.display_height = 1920

        self.display_surface = pygame.display.set_mode((self.display_width, self.display_height), 0, 32)
        pygame.display.set_caption('2048')

        #RGB colors for later use
        self.background_color = (49, 36, 25)
        self.text_color = (255, 255, 255)
        self.alt_text_color = (189, 178, 172)
        self.board_color = (132, 121, 115)
        self.empty_cell = (148, 138, 124)
        self.tile_2 = (239, 231, 222)
        self.tile_4 = (231, 223, 198)
        self.tile_8 = (247, 178, 123)
        self.tile_16 = (247, 150, 99)
        self.tile_32 = (246, 124, 95)
        self.tile_64 = (234, 89, 55)
        self.tile_128 = (230, 206, 115)
        self.tile_256 = (241, 208, 75)
        self.tile_512 = (231, 198, 74)
        self.tile_1024 = (239, 198, 66)
        self.tile_2048 = (234, 192, 44)

        #Attributes for buttons in the game
        self.button_width = self.display_width//5
        self.button_height = self.button_width//4
        self.button_x = self.display_width//2 - self.button_width//2
        self.button_y = self.display_height//2 - self.button_height//2 + 150
        self.button_position = (self.button_x, self.button_y)

        #Button
        self.start_button = SimpleButton(self.button_width, self.button_height, self.tile_2, self.text_color, "Restart",
                                         self.display_surface, self.button_position)

        self.game_font = pygame.font.SysFont("Clear Sans", 100)

        self.score = 0

    def reset_game(self):
        """This function resets the game"""
        return