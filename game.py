import pygame
import sys
import random
from pygame.locals import *
from interface import GameInterface

pygame.init()
game_interface = GameInterface()

def new_game():
    return

def main():
    game_interface.startSetUp()

    #Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    game_interface.display_interface()
    pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()