from game import Board
from tf_policy_value_net import PolicyValueNet
from mcts_alphaZero import MCTS

def human_vs_ai():
    board_size = 6
    board = Board(board_size)
    policy_value_net = PolicyValueNet(board_size)
    mcts = MCTS(policy_value_net, board_size)

    while not board.is_full() and board.check_winner() == 0:
        print(board.board)
        if board.current_player == 1:
            x, y = map(int, input("Enter your move (x y):").split())
        else:
            x, y = mcts.search(board)
        board.make_move(x, y)

    print("Game over! Winner:", board.check_winner())

human_vs_ai()