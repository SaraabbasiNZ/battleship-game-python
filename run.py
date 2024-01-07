import random


class Board:
    def __init__(self):
        # Initialize the game board with default settings and parameters
        self.board_size = 5
        self.ship_size = 3
        self.player_board = [
            [" " for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        self.computer_board = [
            [" " for _ in range(self.board_size)] for _ in range(self.board_size)
        ]
        self.player_turns = 20
        self.computer_turns = 20
        self.ships = 3

    def display_board(self, board, is_player=True):
        # Display the game board, including player's and computer's boards
        print("   0 1 2 3 4")
        for i, row in enumerate(board):
            print(f"{i} |{'|'.join(row)}|")
