import pygame

def draw_board(screen, BOARD_TOP_Y, SQUARE_SIZE):
    LIGHT = (240,217,181)
    DARK = (181,136,99)

    for row in range(8):
        for col in range(8):
            color = LIGHT if (row+col)%2==0 else DARK
            y = BOARD_TOP_Y + row*SQUARE_SIZE
            pygame.draw.rect(screen, color, (col*SQUARE_SIZE, y, SQUARE_SIZE, SQUARE_SIZE))

# ===== PIECE PALETTE =====
white_pieces = ["wK","wQ","wR","wB","wN","wP"]
black_pieces = ["bK","bQ","bR","bB","bN","bP"]

start_x = 50
white_y = 550
black_y = 620

palette_rects = []

for i, p in enumerate(white_pieces):
    x = start_x + i * 60
    rect = pygame.Rect(x, white_y, 40, 40)
    palette_rects.append((p, rect))
    if p in PIECE_IMAGES:
        screen.blit(PIECE_IMAGES[p], (x, white_y))

for i, p in enumerate(black_pieces):
    x = start_x + i * 60
    rect = pygame.Rect(x, black_y, 40, 40)
    palette_rects.append((p, rect))
    if p in PIECE_IMAGES:
        screen.blit(PIECE_IMAGES[p], (x, black_y))