dragging = False
dragged_piece = None
start_square = None

def start_drag(board, row, col):
    global dragging, dragged_piece, start_square

    piece = board[row][col]
    if piece is not None:
        dragging = True
        dragged_piece = piece
        start_square = (row, col)
        board[row][col] = None


def end_drag(board, row, col):
    global dragging, dragged_piece, start_square

    if dragging:
        if board[row][col] is None:
            board[row][col] = dragged_piece
        else:
            # revert
            r, c = start_square
            board[r][c] = dragged_piece

        move = (start_square, (row, col))

        dragging = False
        dragged_piece = None
        return move

    return None