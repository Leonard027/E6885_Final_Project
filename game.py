import numpy as np

class Board:
    def __init__(self, size=6):
        self.size = size
        self.reset()
    
    def reset(self):
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.current_player = 1
    
    def make_move(self, x, y):
        if self.board[x, y] == 0:
            self.board[x, y] = self.current_player
            self.current_player = 3 - self.current_player
            return True
        return False
    
    def check_winner(self):
        for x in range(self.size):
            for y in range(self.size):
                if self._check_direction(x, y, 1, 0) or                    self._check_direction(x, y, 0, 1) or                    self._check_direction(x, y, 1, 1) or                    self._check_direction(x, y, 1, -1):
                    return self.board[x, y]
        return 0

    def _check_direction(self, x, y, dx, dy):
        player = self.board[x, y]
        if player == 0:
            return False
        for i in range(4):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= self.size or ny >= self.size or self.board[nx, ny] != player:
                return False
        return True
    
    def is_full(self):
        return np.all(self.board != 0)