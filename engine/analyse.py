from engine.board_converter import board_to_fen
from engine.evaluation import evaluate_board
from engine.alphabeta import alphabeta
import chess

DEPTH = 3

def analyse_position(ui_board, turn):
    fen = board_to_fen(ui_board, turn)
    board = chess.Board(fen)

    best_move = None
    best_score = float("-inf") if turn == "w" else float("inf")

    for move in board.legal_moves:
        board.push(move)

        score = alphabeta(
            board,
            DEPTH - 1,
            float("-inf"),
            float("inf"),
            False if turn == "w" else True
        )

        board.pop()

        if turn == "w":
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_move, best_score