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

    def place_ships(self, board):
        # Randomly place ships on the board, ensuring no overlap
        for _ in range(self.ships):
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            while board[row][col] == "@":
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
            board[row][col] = "@"

    def validate_input(self, row, col):
        # Check if the input coordinates are within the valid range
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def make_shot(self, board, row, col):
        # Process player's or computer's shot on the board & update accordingly
        if board[row][col] == '@':
            print("Hit!")
            board[row][col] = 'X'
            return True
        else:
            print("Miss!")
            board[row][col] = 'O'
            return False

    def display_instructions(self):
        # Display comprehensive game instructions and information
        print("\nBattleship Game\n")
        print("How to play:")
        print("1. The game consists of two boards, one for each player.")
        print("2. The boards marked with the numbers 0 - 4.")
        print("3. You have a total of 20 turns to sink 3 hidden ships.")
        print("4. Guess a row and a column between 0 and 4.")
        print("5. If you HIT a ship, you will see 'X'.")
        print("6. If you MISS a ship, you will see 'O'.")
        print("7. Your ships is displayed as '@'.")
        print("8. Type 'exit' to quit the game at any time.")
        print("\nLet the battle begin!\n")
