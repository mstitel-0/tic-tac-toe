import random


import random

class TicTacToe:
    def __init__(self, num_players, player_names, grid_size, player_symbols=None):
        if num_players < 2:
            raise ValueError("Number of players must be at least 2.")
        if num_players > 4:
            raise ValueError("Number of players cannot exceed 4.")
        if grid_size < 5:
            raise ValueError("Grid size must be at least 5.")
        if grid_size > 25:
            raise ValueError("Grid size cannot exceed 25.")

        self.num_players = num_players
        self.player_names = player_names
        self.grid_size = grid_size
        self.current_player_index = 0
        self.current_player = player_names[self.current_player_index]
        self.board = [['' for _ in range(grid_size)] for _ in range(grid_size)]
        self.symbols = ['#', '$', '%', '&']  # Define default symbols for players
        if player_symbols is None:
            random.shuffle(self.symbols)  # Shuffle symbols to assign randomly to players if not provided
            self.player_symbols = {player: symbol for player, symbol in zip(player_names, self.symbols)}  # Map player names to symbols
        else:
            self.player_symbols = player_symbols
        self.moves_left = grid_size * grid_size




    # Remaining methods (make_move, check_victory, get_winning_cells) remain unchanged
    def make_move(self, row, col):
        if self.board[row][col] != '':
            return 'occupied', None, []

        self.board[row][col] = self.player_symbols[self.current_player]  # Use player symbol for the current player
        self.moves_left -= 1

        # Check for victory
        if self.check_victory(row, col):
            winning_cells = self.get_winning_cells(row, col)
            return 'win', self.current_player, winning_cells

        # Check for draw
        if self.moves_left == 0:
            return 'draw', None, []

        # Switch to the next player
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        self.current_player = self.player_names[self.current_player_index]
        return 'success', None, []

    # Remaining methods (check_victory, get_winning_cells) remain unchanged


    def check_victory(self, row, col):
        symbol = self.board[row][col]
        min_symbols_for_victory = (self.grid_size + 1) // 2

        # Check horizontal
        count = 1
        for c in range(col + 1, self.grid_size):
            if self.board[row][c] == symbol:
                count += 1
            else:
                break
        for c in range(col - 1, -1, -1):
            if self.board[row][c] == symbol:
                count += 1
            else:
                break
        if count >= min_symbols_for_victory:
            return True

        # Check vertical
        count = 1
        for r in range(row + 1, self.grid_size):
            if self.board[r][col] == symbol:
                count += 1
            else:
                break
        for r in range(row - 1, -1, -1):
            if self.board[r][col] == symbol:
                count += 1
            else:
                break
        if count >= min_symbols_for_victory:
            return True

        # Check diagonal (top-left to bottom-right)
        count = 1
        for i in range(1, min(row, col) + 1):
            if self.board[row - i][col - i] == symbol:
                count += 1
            else:
                break
        for i in range(1, min(self.grid_size - row, self.grid_size - col)):
            if self.board[row + i][col + i] == symbol:
                count += 1
            else:
                break
        if count >= min_symbols_for_victory:
            return True

        # Check diagonal (top-right to bottom-left)
        count = 1
        for i in range(1, min(row, self.grid_size - col - 1) + 1):
            if self.board[row - i][col + i] == symbol:
                count += 1
            else:
                break
        for i in range(1, min(self.grid_size - row, col + 1)):
            if self.board[row + i][col - i] == symbol:
                count += 1
            else:
                break
        if count >= min_symbols_for_victory:
            return True

        return False

    def get_winning_cells(self, row, col):
        symbol = self.board[row][col]
        winning_cells = [[row, col]]

        # Check horizontal
        count = 1
        for c in range(col + 1, self.grid_size):
            if self.board[row][c] == symbol:
                count += 1
                winning_cells.append([row, c])
            else:
                break
        for c in range(col - 1, -1, -1):
            if self.board[row][c] == symbol:
                count += 1
                winning_cells.append([row, c])
            else:
                break
        if count >= self.grid_size // 2:
            return winning_cells

        # Check vertical
        count = 1
        for r in range(row + 1, self.grid_size):
            if self.board[r][col] == symbol:
                count += 1
                winning_cells.append([r, col])
            else:
                break
        for r in range(row - 1, -1, -1):
            if self.board[r][col] == symbol:
                count += 1
                winning_cells.append([r, col])
            else:
                break
        if count >= self.grid_size // 2:
            return winning_cells

        # Check diagonal (top-left to bottom-right)
        count = 1
        for i in range(1, min(row, col) + 1):
            if self.board[row - i][col - i] == symbol:
                count += 1
                winning_cells.append([row - i, col - i])
            else:
                break
        for i in range(1, min(self.grid_size - row, self.grid_size - col)):
            if self.board[row + i][col + i] == symbol:
                count += 1
                winning_cells.append([row + i, col + i])
            else:
                break
        if count >= self.grid_size // 2:
            return winning_cells

        # Check diagonal (top-right to bottom-left)
        count = 1
        for i in range(1, min(row, self.grid_size - col - 1) + 1):
            if self.board[row - i][col + i] == symbol:
                count += 1
                winning_cells.append([row - i, col + i])
            else:
                break
        for i in range(1, min(self.grid_size - row, col + 1)):
            if self.board[row + i][col - i] == symbol:
                count += 1
                winning_cells.append([row + i, col - i])
            else:
                break
        if count >= self.grid_size // 2:
            return winning_cells

        return []