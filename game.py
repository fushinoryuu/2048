import pygame
import sys
from pygame.locals import *
from interface import GameInterface

pygame.init()
game_interface = GameInterface()

def main():
    # Main game loop
    game_interface.start_setup()
    game_interface.print_board()

    while True:
        for event in pygame.event.get():
            game_interface.restart_button.active = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT:
                    print("Right")
                    game_interface.rules.move_right(game_interface.game_board)
                    game_interface.rules.addition_right(game_interface.game_board)
                    game_interface.rules.insert_number(game_interface.game_board)
                    game_interface.print_board()
                elif event.key == K_LEFT:
                    print("Left")
                    game_interface.rules.move_left(game_interface.game_board)
                    game_interface.rules.addition_left(game_interface.game_board)
                    game_interface.rules.insert_number(game_interface.game_board)
                    game_interface.print_board()
                elif event.key == K_UP:
                    print("Up")
                    game_interface.rules.move_up(game_interface.game_board)
                    game_interface.rules.addition_up(game_interface.game_board)
                    game_interface.rules.insert_number(game_interface.game_board)
                    game_interface.print_board()
                elif event.key == K_DOWN:
                    print("Down")
                    game_interface.rules.move_down(game_interface.game_board)
                    game_interface.rules.addition_down(game_interface.game_board)
                    game_interface.rules.insert_number(game_interface.game_board)
                    game_interface.print_board()
            if event.type == MOUSEBUTTONDOWN:
                mouse_xy = pygame.mouse.get_pos()
                if game_interface.restart_button.clicked(mouse_xy):
                    game_interface.restart_button.highlighted = True
                    print("Click Down")
            if event.type == MOUSEBUTTONUP:
                mouse_xy = pygame.mouse.get_pos()
                if game_interface.restart_button.clicked(mouse_xy):
                    print("Click UP")

        game_interface.display_interface()
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()