from engine.board_converter import board_to_fen
from engine.evaluation import evaluate_board
import chess

DEPTH = 3

def analyse_position(ui_board, turn):
    fen = board_to_fen(ui_board)
    board = chess.Board(fen)

    move_scores = []

    for move in board.legal_moves:
        board.push(move)

        score = minimax(
            board,
            DEPTH - 1,
            False if turn == "w" else True
        )

        board.pop()

        move_scores.append((move, score))

    reverse = True if turn == "w" else False
    move_scores.sort(key=lambda x: x[1], reverse=reverse)

    return [move.uci() for move, _ in move_scores[:3]], move_scores


def minimax(board, depth, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    moves = list(board.legal_moves)

    if not moves:
        return evaluate_board(board)

    if maximizing:
        max_eval = float("-inf")

        for move in moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()

            max_eval = max(max_eval, eval)

        return max_eval

    else:
        min_eval = float("inf")

        for move in moves:
            board.push(move)
            eval = minimax(board, depth - 1, True)
            board.pop()

            min_eval = min(min_eval, eval)

        return min_eval

