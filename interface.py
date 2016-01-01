import pygame
from pygame.locals import *
from button_class import SimpleButton

pygame.init()

class GameInterface:
    """This class represents the interface for the game's menu."""
    def __init__(self):
        self.display_width = 720
        self.display_height = 1280

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

        self.display_surface.fill(self.background_color)

        #Attributes for buttons in the game
        self.button_width = self.display_width//5
        self.button_height = self.button_width//4
        self.button_x = self.display_width//2 - self.button_width//2
        self.button_y = self.display_height//2 - self.button_height//2 + 150
        self.button_position = (self.button_x, self.button_y)

        #Button
        self.restart_button = SimpleButton(self.button_width, self.button_height, self.tile_2, self.text_color, "Restart",
                                         self.display_surface, self.button_position)
        self.button_list = [self.restart_button]

        gameFont = pygame.font.SysFont("Sans Serif", 72)
        self.title_text_surface = gameFont.render("2048", True, self.text_color, None)

    def display_buttons(self):
        for x in self.button_list:
            x.display_button()

    def display_interface(self):
        self.display_buttons()