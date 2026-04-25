import pygame
import sys
import os
from engine.analyse import analyse_position

pygame.init()

# ================= CONFIG =================
WIDTH, HEIGHT = 600, 700
BOARD_TOP_Y = 100
BOARD_HEIGHT = 400
SQUARE_SIZE = BOARD_HEIGHT // 8
ROWS, COLS = 8, 8
PIECE_SIZE = 40
BUTTON_WIDTH, BUTTON_HEIGHT = 180, 50

turn = "w"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
BUTTON_COLOR = (100, 100, 150)
BG_COLOR = (240, 220, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Position Analyzer")

FONT = pygame.font.SysFont("Arial", 20)

# ================= LOAD IMAGES =================
PIECE_IMAGES = {}
piece_files = {
    "wP": "wp.png", "wR": "wr.png", "wN": "wn.png", "wB": "wb.png", "wQ": "wq.png", "wK": "wk.png",
    "bP": "bp.png", "bR": "br.png", "bN": "bn.png", "bB": "bb.png", "bQ": "bq.png", "bK": "bk.png"
}

def load_images():
    for piece, filename in piece_files.items():
        path = os.path.join("assets/images", filename)
        if os.path.exists(path):
            img = pygame.image.load(path)
            PIECE_IMAGES[piece] = pygame.transform.scale(img, (40, 40))
        else:
            print("Missing:", path)

load_images()

# ================= DATA =================
board = [[None for _ in range(COLS)] for _ in range(ROWS)]
dragging_piece = None
old_r, old_c = None, None

piece_limits = {
    "wK":1, "wQ":1, "wR":2, "wB":2, "wN":2, "wP":8,
    "bK":1, "bQ":1, "bR":2, "bB":2, "bN":2, "bP":8
}
piece_count = {k:0 for k in piece_limits}
palette = []

# ================= UI =================
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            y = BOARD_TOP_Y + row * SQUARE_SIZE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece in PIECE_IMAGES:
                x = col * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE)//2
                y = BOARD_TOP_Y + row * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE)//2
                screen.blit(PIECE_IMAGES[piece], (x, y))

def draw_button():
    x = WIDTH - BUTTON_WIDTH - 20
    y = 20
    pygame.draw.rect(screen, BUTTON_COLOR, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.draw.rect(screen, BLACK, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT), 2)
    text = FONT.render("Analyse", True, WHITE)
    screen.blit(text, (x + 40, y + 15))
    return pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)

def draw_palette():
    palette.clear()

    white_pieces = ["wK","wQ","wR","wB","wN","wP"]
    black_pieces = ["bK","bQ","bR","bB","bN","bP"]

    start_x = 40
    white_y = 520
    black_y = 580

    for i, p in enumerate(white_pieces):
        x = start_x + i*60
        rect = pygame.Rect(x, white_y, 40, 40)
        palette.append((p, rect))
        screen.blit(PIECE_IMAGES[p], (x, white_y))

    for i, p in enumerate(black_pieces):
        x = start_x + i*60
        rect = pygame.Rect(x, black_y, 40, 40)
        palette.append((p, rect))
        screen.blit(PIECE_IMAGES[p], (x, black_y))

def coord_to_square(pos):
    x, y = pos
    if BOARD_TOP_Y <= y < BOARD_TOP_Y + BOARD_HEIGHT:
        row = (y - BOARD_TOP_Y) // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col
    return None

# ================= LOOP =================
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(BG_COLOR)

    button_rect = draw_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # PALETTE PICK
            for p, rect in palette:
                if rect.collidepoint(mouse_pos):
                    if piece_count[p] < piece_limits[p]:
                        dragging_piece = p
                        old_r, old_c = None, None

            # ANALYSE
            if button_rect.collidepoint(mouse_pos):
                flat = sum(board, [])
                if "wK" not in flat or "bK" not in flat:
                    print("Invalid board")
                else:
                    move, score = analyse_position(board, turn)
                    print("Best Move:", move, "Score:", score)

            # BOARD PICK
            square = coord_to_square(mouse_pos)
            if square:
                r, c = square
                if board[r][c]:
                    dragging_piece = board[r][c]
                    old_r, old_c = r, c
                    board[r][c] = None

        elif event.type == pygame.MOUSEBUTTONUP:
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

    # DRAW
    draw_board()
    draw_pieces()
    draw_palette()

    # DRAG VISUAL
    if dragging_piece and dragging_piece in PIECE_IMAGES:
        mx, my = mouse_pos
        screen.blit(PIECE_IMAGES[dragging_piece], (mx - PIECE_SIZE//2, my - PIECE_SIZE//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()