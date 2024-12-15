from game import Board
from tf_policy_value_net import PolicyValueNet
from mcts_alphaZero import MCTS

def train():
    board_size = 6
    episodes = 50
    policy_value_net = PolicyValueNet(board_size)

    for episode in range(episodes):
        board = Board(board_size)
        mcts = MCTS(policy_value_net, board_size)
        states, policies, values = [], [], []

        while not board.is_full() and board.check_winner() == 0:
            move = mcts.search(board)
            x, y = move
            states.append(board.board.copy())
            board.make_move(x, y)

        print(f"Episode {episode+1}: Winner {'Draw' if board.check_winner() == 0 else board.check_winner()}")
train()