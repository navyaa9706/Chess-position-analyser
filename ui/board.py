import pygame

LIGHT = (240, 217, 181)
DARK  = (200, 120, 140)

# ================= BOARD =================
def draw_board(screen, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE):
    font = pygame.font.SysFont("Arial", 16)

    for row in range(8):
        for col in range(8):
            color = LIGHT if (row + col) % 2 == 0 else DARK

            x = BOARD_LEFT_X + col * SQUARE_SIZE
            y = BOARD_TOP_Y + row * SQUARE_SIZE

            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            # numbers (1–8)
            if col == 0:
                text = font.render(str(8-row), True, (0,0,0))
                screen.blit(text, (x - 20, y + 5))

            # letters (a–h)
            if row == 7:
                letter = chr(ord('a') + col)
                text = font.render(letter, True, (0,0,0))
                screen.blit(text, (x + SQUARE_SIZE//2 - 5, y + SQUARE_SIZE + 5))


# ================= PIECES =================
def draw_pieces(screen, board, PIECE_IMAGES, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                img = PIECE_IMAGES.get(piece)
                if img:
                    x = BOARD_LEFT_X + col * SQUARE_SIZE
                    y = BOARD_TOP_Y + row * SQUARE_SIZE
                    screen.blit(img, (x, y))


# ================= PALETTE =================
def draw_palette(screen, PIECE_IMAGES, WIDTH):
    palette = []

    white_pieces = ["wK","wQ","wR","wB","wN","wP"]
    black_pieces = ["bK","bQ","bR","bB","bN","bP"]

    start_x = (WIDTH - 360) // 2
    white_y = 550
    black_y = 620

    for i, p in enumerate(white_pieces):
        x = start_x + i * 60
        rect = pygame.Rect(x, white_y, 40, 40)
        palette.append((p, rect))
        screen.blit(PIECE_IMAGES[p], (x, white_y))

    for i, p in enumerate(black_pieces):
        x = start_x + i * 60
        rect = pygame.Rect(x, black_y, 40, 40)
        palette.append((p, rect))
        screen.blit(PIECE_IMAGES[p], (x, black_y))

    return palette