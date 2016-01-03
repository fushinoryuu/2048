import pygame
from pygame.locals import *
from button_class import SimpleButton
from tile import Tile
from rules import GameRules

pygame.init()

class GameInterface:
    """This class represents the interface for the game's menu."""
    def __init__(self):
        self.display_width = 600
        self.display_height = 800

        self.display_surface = pygame.display.set_mode((self.display_width,
                                                        self.display_height), 0, 32)
        pygame.display.set_caption('2048')

        #This matrix represent that game board.
        self.game_board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        #RGB colors for later use
        self.background_color = (49, 36, 25)
        self.text_color = (255, 255, 255)
        self.alt_text_color = (189, 178, 172)
        self.board_color = (132, 121, 115)
        self.empty_cell = (148, 138, 124)
        self.button_color = (250, 0, 0)
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
        self.button_x = self.display_width/8
        self.button_y = self.display_height/3
        self.button_position = (self.button_x, self.button_y)

        #Button
        self.restart_button = SimpleButton(self.button_width, self.button_height, self.button_color,
                                           self.text_color, "Restart", self.display_surface,
                                           self.button_position)
        self.button_list = [self.restart_button]

        self.rules = GameRules()

    def display_buttons(self):
        for x in self.button_list:
            x.display_button()

    def display_board(self):
        """This function will draw the game board."""
        x = self.display_width/8
        y = self.display_height/2.5

        #Game board
        pygame.draw.rect(self.display_surface, self.board_color, Rect((x, y), (450, 450)))

        #First row of empty cells
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 10, y + 10), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 120, y + 10), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 230, y + 10), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 340, y + 10), (100, 100)))

        #Second row of empty cells
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 10, y + 120), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 120, y + 120), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 230, y + 120), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 340, y + 120), (100, 100)))

        #Third row of empty cells
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 10, y + 230), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 120, y + 230), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 230, y + 230), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 340, y + 230), (100, 100)))

        #Fourth row of empty cells
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 10, y + 340), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 120, y + 340), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 230, y + 340), (100, 100)))
        pygame.draw.rect(self.display_surface, self.empty_cell, Rect((x + 340, y + 340), (100, 100)))

    def start_setup(self):
        """This function starts the set u for the game setting up the buttons and the game board."""
        self.restart_button.active = True
        self.rules.insert_number(self.game_board)

    def print_board(self):
        print(self.game_board)

    def display_interface(self):
        self.display_buttons()
        self.display_board()

    def reset_game(self):
        """Resets everything for a new game."""
        return