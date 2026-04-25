import chess
from engine.board_converter import board_to_fen
from engine.evaluation import evaluate_board

def analyse_position(ui_board, turn):
    fen = board_to_fen(ui_board, turn)
    board = chess.Board(fen)

    best_move = None
    best_score = -9999 if turn == "w" else 9999

    for move in board.legal_moves:
        board.push(move)
        score = evaluate_board(board)
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