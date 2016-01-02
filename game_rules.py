class GameRules:
    """This class describes the rules for the game."""
    def __init__(self):
        self.matrix = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.score = 0

    def new_score(self, matrix):
        """This function will be called after every move to calculate the players score."""
        return

    def you_lose(self, matrix):
        """This function will be called after every turn to check if the player has lost."""
        return