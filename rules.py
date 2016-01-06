import random
import sys

class GameRules:
    """This class describes the rules for the game."""
    def __init__(self):
        self.score = 0

    def random_location(self):
        rand_x = random.randint(0,3)
        rand_y = random.randint(0,3)

        return rand_x, rand_y

    def move_up(self, matrix):
        i = 0
        for j in range(0,4):
            if matrix[i][j] != 0 or matrix[i + 1][j] != 0 or matrix[i + 2][j] != 0 or matrix[i + 3][j] != 0:
                if matrix[i][j] == 0:
                    while matrix[i][j] == 0:
                        matrix[i][j] = matrix[i + 1][j]
                        matrix[i + 1][j] = matrix[i + 2][j]
                        matrix[i + 2][j] = matrix[i + 3][j]
                        matrix[i + 3][j] = 0

                if matrix[i + 1][j] == 0 and (matrix[i + 2][j] != 0 or matrix[i + 3][j] != 0):
                    while matrix[i + 1][j]==0:
                        matrix[i + 1][j] = matrix[i + 2][j]
                        matrix[i + 2][j] = matrix[i + 3][j]
                        matrix[i + 3][j] = 0
                if matrix[i + 2][j] == 0 and matrix[i + 3][j] != 0:
                    while matrix[i + 2] == 0:
                        matrix[i + 2] = matrix[i + 3]
                        matrix[i + 3][j] = 0

    def addition_up(self, matrix):
        i = 0
        for j in range(0,4):
            if matrix[i][j] == matrix[i + 1][j]:
                matrix[i][j] = matrix[i][j] + matrix[i + 1][j]
                matrix[i + 1][j] = matrix[i + 2][j]
                matrix[i + 2][j] = matrix[i + 3][j]
                matrix[i + 3][j] = 0

            if matrix[i + 1][j] == matrix[i + 2][j]:
                matrix[i + 1][j] = matrix[i + 1][j] + matrix[i + 2][j]
                matrix[i + 2][j] = matrix[i + 3][j]
                matrix[i + 3][j] = 0

            if matrix[i + 2][j] == matrix[i + 3][j]:
                matrix[i + 2][j] = matrix[i + 2][j] + matrix[i + 3][j]
                matrix[i + 3][j] = 0

    def move_down(self, matrix):
        i = 0
        for j in range(0,4):
            if matrix[i][j] != 0 or matrix[i + 1][j] != 0 or matrix[i + 2][j] != 0 or matrix[i + 3][j] != 0:
                if matrix[i + 3][j] == 0:
                    while matrix[i + 3][j] == 0:
                        matrix[i + 3][j] = matrix[i + 2][j]
                        matrix[i + 2][j] = matrix[i + 1][j]
                        matrix[i + 1][j] = matrix[i][j]
                        matrix[i][j] = 0

                if matrix[i + 2][j] == 0 and (matrix[i + 1][j] != 0 or matrix[i][j] != 0):
                    while matrix[i + 2][j] == 0:
                        matrix[i + 2][j] = matrix[i + 1][j]
                        matrix[i + 1][j] = matrix[i][j]
                        matrix[i][j] = 0

                if matrix[i + 1][j] == 0 and matrix[i][j] != 0:
                    while matrix[i + 1][j] == 0:
                        matrix[i + 1][j] = matrix[i][j]
                        matrix[i][j] = 0

    def addition_down(self, matrix):
        i = 0
        for j in range(0,4):
            if matrix[i + 3][j] == matrix[i + 2][j]:
                matrix[i + 3][j] = matrix[i + 3][j] + matrix[i + 2][j]
                matrix[i + 2][j] = matrix[i + 1][j]
                matrix[i + 1][j] = matrix[i][j]
                matrix[i][j] = 0

            if matrix[i + 2][j] == matrix[i + 1][j]:
                matrix[i + 2][j] = matrix[i + 2][j] + matrix[i + 1][j]
                matrix[i + 1][j] = matrix[i][j]
                matrix[i][j] = 0

            if matrix[i + 1][j] == matrix[i][j]:
                matrix[i + 1][j] = matrix[i + 1][j] + matrix[i][j]
                matrix[i][j] = 0

    def move_left(self, matrix):
        j = 0
        for i in range(0,4):
            if matrix[i][j] != 0 or matrix[i][j + 1] != 0 or matrix[i][j + 2] != 0 or matrix[i][j + 3] != 0:
                if matrix[i][j] == 0:
                    while matrix[i][j] == 0:
                        matrix[i][j] = matrix[i][j + 1]
                        matrix[i][j + 1] = matrix[i][j + 2]
                        matrix[i][j + 2] = matrix[i][j + 3]
                        matrix[i][j + 3] = 0

                if matrix[i][j + 1] == 0 and (matrix[i][j + 2] != 0 or matrix[i][j + 3] != 0):
                    while matrix[i][j + 1] == 0:
                        matrix[i][j + 1] = matrix[i][j + 2]
                        matrix[i][j + 2] = matrix[i][j + 3]
                        matrix[i][j + 3] = 0

                if matrix[i][j + 2] == 0 and (matrix[i][j + 3] != 0):
                    while matrix[i][j + 2] == 0:
                        matrix[i][j + 2] = matrix[i][j + 3]
                        matrix[i][j + 3] = 0

    def addition_left(self, matrix):
        j = 0
        for i in range(0,4):
            if matrix[i][j] == matrix[i][j + 1]:
                matrix[i][j] = matrix[i][j] + matrix[i][j + 1]
                matrix[i][j + 1] = matrix[i][j + 2]
                matrix[i][j + 2] = matrix[i][j + 3]
                matrix[i][j + 3] = 0

            if matrix[i][j + 1] == matrix[i][j + 2]:
                matrix[i][j + 1] = matrix[i][j + 1] + matrix[i][j + 2]
                matrix[i][j + 2] = matrix[i][j + 3]
                matrix[i][j + 3] = 0

            if matrix[i][j + 2] == matrix[i][j + 3]:
                matrix[i][j + 2] = matrix[i][j + 2] + matrix[i][j + 3]
                matrix[i][j + 3] = 0

    def move_right(self, matrix):
        j = 0
        for i in range(0,4):
            if matrix[i][j] != 0 or matrix[i][j + 1] != 0 or matrix[i][j + 2] != 0 or matrix[i][j + 3] != 0:
                if matrix[i][j + 3] == 0:
                    while matrix[i][j + 3] == 0:
                        matrix[i][j + 3] = matrix[i][j + 2]
                        matrix[i][j + 2] = matrix[i][j + 1]
                        matrix[i][j + 1] = matrix[i][j]
                        matrix[i][j] = 0

                if matrix[i][j + 2] == 0 and (matrix[i][j + 1] != 0 or matrix[i][j] != 0):
                    while matrix[i][j + 2] == 0:
                        matrix[i][j + 2] = matrix[i][j + 1]
                        matrix[i][j + 1] = matrix[i][j]
                        matrix[i][j] = 0

                if matrix[i][j + 1] == 0 and matrix[i][j] != 0:
                    while matrix[i][j + 1] == 0:
                        matrix[i][j + 1] = matrix[i][j]
                        matrix[i][j] = 0
    def addition_right(self, matrix):
        j=0
        for i in range(0,4):
            if matrix[i][j + 3] == matrix[i][j + 2]:
                matrix[i][j + 3] = matrix[i][j + 3] + matrix[i][j + 2]
                matrix[i][j + 2] = matrix[i][j + 1]
                matrix[i][j + 1] = matrix[i][j]
                matrix[i][j] = 0

            if matrix[i][j + 2] == matrix[i][j + 1]:
                matrix[i][j + 2] = matrix[i][j + 2] + matrix[i][j + 1]
                matrix[i][j + 1] = matrix[i][j]
                matrix[i][j] = 0

            if matrix[i][j + 1] == matrix[i][j]:
                matrix[i][j + 1] = matrix[i][j + 1] + matrix[i][j]
                matrix[i][j] = 0

    def insert_number(self, matrix):
        """This function will allow us to insert a number into the game board."""
        temp_column, temp_row = self.random_location()
        if matrix[temp_column][temp_row] is not 0:
            try:
                self.insert_number(matrix)
            except "RuntimeError: maximum recursion depth exceeded while calling a Python object":
                print("You lose!")
                sys.exit()
        else:
            matrix[temp_column][temp_row] = 2