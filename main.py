import pygame
import sys
import os
from engine.analyse import analyse_position

from ui.board import draw_board, draw_pieces
from ui.palette import draw_palette
from ui.button import draw_button
from ui.input_handler import handle_input

pygame.init()

#coordinates configuration
WIDTH, HEIGHT = 600, 700
BOARD_TOP_Y = 120
BOARD_HEIGHT = 400
SQUARE_SIZE = BOARD_HEIGHT // 8
ROWS, COLS = 8, 8
PIECE_SIZE = 40
BOARD_LEFT_X = (WIDTH - BOARD_HEIGHT) // 2

turn = "w"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Position Analyzer")

BG_COLOR = (230, 200, 210)

#load piece images 
PIECE_IMAGES = {}
piece_files = {
    "wP": "wp.png", "wR": "wr.png", "wN": "wn.png", "wB": "wb.png", "wQ": "wq.png", "wK": "wk.png",
    "bP": "bp.png", "bR": "br.png", "bN": "bn.png", "bB": "bb.png", "bQ": "bq.png", "bK": "bk.png"
}

for piece, filename in piece_files.items():
    path = os.path.join("assets/images", filename)
    if os.path.exists(path):
        img = pygame.image.load(path)
        PIECE_IMAGES[piece] = pygame.transform.scale(img, (40, 40))

#data
board = [[None for _ in range(COLS)] for _ in range(ROWS)]

dragging_piece = False
old_r, old_c = None, None

piece_limits = {
    "wK":1, "wQ":1, "wR":2, "wB":2, "wN":2, "wP":8,
    "bK":1, "bQ":1, "bR":2, "bB":2, "bN":2, "bP":8
}
piece_count = {k:0 for k in piece_limits}
palette = []

#helper
def coord_to_square(pos):
    x, y = pos
    if BOARD_TOP_Y <= y < BOARD_TOP_Y + BOARD_HEIGHT and BOARD_LEFT_X <= x < BOARD_LEFT_X + BOARD_HEIGHT:
        row = (y - BOARD_TOP_Y) // SQUARE_SIZE
        col = (x - BOARD_LEFT_X) // SQUARE_SIZE
        return row, col
    return None

#game loop?
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG_COLOR)
    mouse_pos = pygame.mouse.get_pos()
    events = pygame.event.get()

    #quit
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    
    button_rect = draw_button(screen, WIDTH)

    #state passed to input handler
    state = {
        "board": board,
        "palette": palette,
        "mouse_pos": mouse_pos,
        "coord_to_square": coord_to_square,
        "piece_count": piece_count,
        "piece_limits": piece_limits,
        "turn": turn,
        "button_rect": button_rect,
        "dragging_piece": dragging_piece,
        "old_r": old_r,
        "old_c": old_c
    }

    
    dragging_piece, old_r, old_c = handle_input(events, state)

    #draw everything
    draw_board(screen, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE)
    draw_pieces(screen, board, PIECE_IMAGES, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE)
    palette = draw_palette(screen, PIECE_IMAGES)
    
    if dragging_piece:
        mx, my = mouse_pos

    #if dragging from palette or board
        piece = dragging_piece if isinstance(dragging_piece, str) else None

        if piece and piece in PIECE_IMAGES:
            screen.blit(
                PIECE_IMAGES[piece],
                (mx - SQUARE_SIZE//2, my - SQUARE_SIZE//2)
         )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()