import random
import numpy as np
from game import Board

class PureMCTS:
    def __init__(self, board_size, simulations=100):
        self.board_size = board_size
        self.simulations = simulations

    def search(self, board):
        valid_moves = list(zip(*np.where(board.board == 0)))  # All legal moves
        best_move = None
        max_wins = -1

        for move in valid_moves:
            wins = 0
            for _ in range(self.simulations):
                wins += self._simulate(board, move)
            if wins > max_wins:
                max_wins = wins
                best_move = move

        return best_move

    def _simulate(self, board, move):
        temp_board = Board(self.board_size)
        temp_board.board = board.board.copy()
        temp_board.make_move(move[0], move[1])
        player = temp_board.current_player

        while not temp_board.is_full() and temp_board.check_winner() == 0:
            valid_moves = list(zip(*np.where(temp_board.board == 0)))
            random_move = random.choice(valid_moves)
            temp_board.make_move(random_move[0], random_move[1])

        winner = temp_board.check_winner()
        return 1 if winner == player else 0