import numpy as np

class MCTS:
    def __init__(self, policy_value_net, board_size, dirichlet_alpha=0.3, c_puct=1.5):
        self.policy_value_net = policy_value_net
        self.board_size = board_size
        self.dirichlet_alpha = dirichlet_alpha
        self.c_puct = c_puct

    def search(self, board):
        state = np.stack([(board.board == 1).astype(int), (board.board == 2).astype(int)], axis=-1)
        state = state.reshape((1, self.board_size, self.board_size, 2))
        policy, _ = self.policy_value_net.predict(state)
        noise = np.random.dirichlet([self.dirichlet_alpha] * len(policy[0]))
        policy = 0.75 * policy[0] + 0.25 * noise

        valid_moves = np.argwhere(board.board == 0)
        move_probs = {tuple(move): policy[move[0] * self.board_size + move[1]] for move in valid_moves}
        return max(move_probs, key=move_probs.get)