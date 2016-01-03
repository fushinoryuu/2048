from random import randint

class GameRules:
    """This class describes the rules for the game."""
    def __init__(self):
        self.score = 0

    def random_location(self):
        rand_x = randint(0,3)
        rand_y = randint(0,3)

        return rand_x, rand_y

    def move(self, direction, matrix):
        """This function helps move the numbers in the matrix."""
        return

    def insert_number(self, matrix):
        """This function will allow us to insert a number into the game board."""
        temp_x, temp_y = self.random_location()
        if matrix[temp_x][temp_y] is not 0:
            self.insert_number(matrix)
        else:
            matrix[temp_x][temp_y] = 2