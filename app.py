from game import TicTacToe

class TicTacToeGame:
    def __init__(self):
        self.num_players = 0
        self.player_names = []
        self.grid_size = 0
        self.game = None

    def start_game(self):
        print("Welcome to Tic-Tac-Toe!")

        self.get_players_info()
        self.get_grid_size()

        self.game = TicTacToe(self.num_players, self.player_names, self.grid_size)
        self.play_game()

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

            row, col = self.get_player_move()

            result, winner, _ = self.game.make_move(row, col)

            if result == 'win':
                print(f"Congratulations! {winner} wins!")
                break
            elif result == 'draw':
                print("It's a draw!")
                break

    def display_board(self):
        board = self.game.board
        for row in board:
            print("|".join(f" {cell} " if cell else "   " for cell in row))
            print("|".join(["---" for _ in range(self.grid_size)]))
        print()

    def get_player_move(self):
        while True:
            try:
                row = int(input("Enter row number (0 to grid size - 1): "))
                col = int(input("Enter column number (0 to grid size - 1): "))
                if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Please enter valid row and column numbers.")

        return row, col

if __name__ == "__main__":
    game = TicTacToeGame()
    game.start_game()
