from engine.analyse import analyse_position

def handle_input(events, state):

    board = state["board"]
    palette = state["palette"]
    mouse_pos = state["mouse_pos"]
    coord_to_square = state["coord_to_square"]
    piece_count = state["piece_count"]
    piece_limits = state["piece_limits"]

    dragging_piece = state["dragging_piece"]
    old_r = state["old_r"]
    old_c = state["old_c"]

    turn = state["turn"]
    white_btn = state["white_btn"]
    black_btn = state["black_btn"]
    analyse_btn = state["analyse_btn"]

    for event in events:

        if event.type == 1025:  # MOUSE DOWN
            mx, my = mouse_pos

            # ===== TURN SELECT =====
            if white_btn and white_btn.collidepoint(mx, my):
                turn = "w"

            elif black_btn and black_btn.collidepoint(mx, my):
                turn = "b"

            # ===== ANALYSE =====
            elif analyse_btn and analyse_btn.collidepoint(mx, my):
                flat = [p for row in board for p in row]
                if "wK" in flat and "bK" in flat:
                    move, score = analyse_position(board, turn)
                    print("Best Move:", move, "Score:", score)
                else:
                    print("Invalid board")

            # ===== PALETTE PICK =====
            for p, rect in palette:
                if rect.collidepoint(mx, my):
                    if piece_count[p] < piece_limits[p]:
                        dragging_piece = p
                        old_r, old_c = None, None

            # ===== BOARD PICK =====
            square = coord_to_square(mouse_pos)
            if square:
                r, c = square
                if board[r][c] is not None:
                    dragging_piece = board[r][c]
                    old_r, old_c = r, c
                    board[r][c] = None

        elif event.type == 1026:  # MOUSE UP

            if dragging_piece:
                square = coord_to_square(mouse_pos)

                if square:
                    r, c = square

                    if board[r][c] is None:
                        board[r][c] = dragging_piece

                        if old_r is None:
                            piece_count[dragging_piece] += 1

                    else:
                        if old_r is not None:
                            board[old_r][old_c] = dragging_piece

                else:
                    if old_r is not None:
                        board[old_r][old_c] = dragging_piece

                dragging_piece = None
                old_r, old_c = None, None

    return dragging_piece, old_r, old_c, turn