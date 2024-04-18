import os
import sys
import random

from game import TicTacToe


class TicTacToeGame:
    def __init__(self):
        self.num_players = 0
        self.player_names = []
        self.grid_size = 0
        self.game = None
        self.active_cell = (0, 0)
        self.current_player_index = 0

    def start_game(self):
        print("Welcome to Tic-Tac-Toe!")
        self.get_players_info()
        self.get_grid_size()
        self.game = TicTacToe(self.num_players, self.player_names, self.grid_size)
        self.play_game()

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        board = self.game.board
        cell_width = 5
        row_separator = "+".join(["-" * cell_width for _ in range(self.grid_size)])
        for i in range(self.grid_size):
            print("|", end="")
            for j in range(self.grid_size):
                cell_content = f"[{board[i][j]:^3}]" if (i, j) != self.active_cell else f"[*{board[i][j]}*]"
                print(cell_content, end="")
                if j != self.grid_size - 1:
                    print("|", end="")
            print("|")
            if i != self.grid_size - 1:
                print("+" + row_separator)
        print()
        print(f"It's {self.player_names[self.current_player_index]}'s turn.")

    def handle_arrow_input(self):
        while True:
            try:
                import msvcrt
                key = ord(msvcrt.getch())
                if key == 224:
                    arrow_key = ord(msvcrt.getch())
                    if arrow_key == 72:
                        self.active_cell = (max(self.active_cell[0] - 1, 0), self.active_cell[1])
                    elif arrow_key == 80:
                        self.active_cell = (min(self.active_cell[0] + 1, self.grid_size - 1), self.active_cell[1])
                    elif arrow_key == 75:
                        self.active_cell = (self.active_cell[0], max(self.active_cell[1] - 1, 0))
                    elif arrow_key == 77:
                        self.active_cell = (self.active_cell[0], min(self.active_cell[1] + 1, self.grid_size - 1))
                    self.display_board()
                elif key == 13:
                    return self.active_cell
            except ImportError:
                print("Arrow key input is not supported on this platform.")
                sys.exit(1)

    def get_players_info(self):
        while True:
            try:
                self.num_players = int(input("Enter the number of players (2 to 4): "))
                if 2 <= self.num_players <= 4:
                    break
                else:
                    print("Number of players must be between 2 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        for i in range(self.num_players):
            name = input(f"Enter name for player {i + 1}: ")
            self.player_names.append(name)

    def get_grid_size(self):
        while True:
            try:
                self.grid_size = int(input("Enter the size of the grid (5 to 25): "))
                if 5 <= self.grid_size <= 25:
                    break
                else:
                    print("Grid size must be between 5 and 25.")
            except ValueError:
                print("Please enter a valid number.")

    def play_game(self):
        while True:
            self.display_board()

            while True:
                try:
                    row, col = self.handle_arrow_input()
                    result, winner, _ = self.game.make_move(row, col)
                    break
                except ValueError:
                    print("Invalid move! Please enter row and column numbers separated by a space (e.g., 1 2).")

            if result == 'win':
                self.display_board()
                print(f"Congratulations! {winner} wins!")
                play_again = input("Play Again? (y/n): ")
                if play_again.lower() != 'y':
                    break
                else:
                    self.game.clear_board()
                    self.current_player_index = 0
                    self.active_cell = (0, 0)
            elif result == 'draw':
                print("It's a draw!")
                play_again = input("Play Again? (y/n): ")
                if play_again.lower() != 'y':
                    break
            elif result == 'success':
                self.current_player_index = (self.current_player_index + 1) % self.num_players


if __name__ == "__main__":
    game = TicTacToeGame()
    game.start_game()
