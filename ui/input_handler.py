from engine.analyse import analyse_position

def handle_input(events, state):
    board = state["board"]
    palette = state["palette"]
    mouse_pos = state["mouse_pos"]
    coord_to_square = state["coord_to_square"]
    piece_count = state["piece_count"]
    piece_limits = state["piece_limits"]
    turn = state["turn"]
    button_rect = state["button_rect"]

    dragging_piece = state["dragging_piece"]
    old_r = state["old_r"]
    old_c = state["old_c"]

    for event in events:

        #mouse down
        if event.type == 1025:

            #pick piece from palette
            for p, rect in palette:
                if rect.collidepoint(mouse_pos):
                    if piece_count[p] < piece_limits[p]:
                        dragging_piece = p
                        old_r, old_c = None, None

            #button work
            if button_rect.collidepoint(mouse_pos):
                flat = [piece for row in board for piece in row]
                if "wK" in flat and "bK" in flat:
                    move, score = analyse_position(board, turn)
                    print("Best Move:", move, "Score:", score)
                else:
                    print("Invalid board")

            #pick from board
            square = coord_to_square(mouse_pos)
            if square:
                r, c = square
                if board[r][c] is not None:
                    dragging_piece = board[r][c]
                    old_r, old_c = r, c
                    board[r][c] = None

        #mouse up
        elif event.type == 1026:

            if dragging_piece:
                square = coord_to_square(mouse_pos)

                if square:
                    r, c = square

                    if board[r][c] is None:
                        #place piece
                        board[r][c] = dragging_piece

                        # from palette
                        if old_r is None:
                            piece_count[dragging_piece] += 1

                    else:
                        #if occupied-->revert
                        if old_r is not None:
                            board[old_r][old_c] = dragging_piece

                else:
                    #dropped outside-->revert
                    if old_r is not None:
                        board[old_r][old_c] = dragging_piece

                dragging_piece = None
                old_r, old_c = None, None

    return dragging_piece, old_r, old_c