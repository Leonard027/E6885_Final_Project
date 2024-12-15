from game import Board
from tf_policy_value_net import PolicyValueNet
from mcts_alphaZero import MCTS
from pure_mcts import PureMCTS

def evaluate_alphazero_vs_pure(episodes=50, board_size=6):
    alphazero_wins, pure_wins, draws = 0, 0, 0
    policy_value_net = PolicyValueNet(board_size)
    pure_mcts = PureMCTS(board_size)

    for episode in range(episodes):
        board = Board(board_size)
        mcts_alphazero = MCTS(policy_value_net, board_size)

        while not board.is_full() and board.check_winner() == 0:
            if board.current_player == 1:
                # AlphaZero's move
                move = mcts_alphazero.search(board)
            else:
                # Pure MCTS's move
                move = pure_mcts.search(board)

            board.make_move(*move)

        winner = board.check_winner()
        if winner == 1:
            alphazero_wins += 1
        elif winner == 2:
            pure_wins += 1
        else:
            draws += 1

        print(f"Game {episode+1}/{episodes}: Winner - {'AlphaZero' if winner == 1 else 'Pure MCTS' if winner == 2 else 'Draw'}")

    print("\nEvaluation Results:")
    print(f"AlphaZero Wins: {alphazero_wins}")
    print(f"Pure MCTS Wins: {pure_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    evaluate_alphazero_vs_pure(episodes=50, board_size=6)