import pygame
import sys

from engine.analyse import analyse_position

from ui.board import draw_board, draw_pieces, draw_palette
from ui.panel import draw_panel
from ui.input_handler import handle_input

from ui.utils import coord_to_square 
from ui.assets_loader import load_images

from config import *

pygame.init()

# ================= SETUP =================
turn = "w"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Position Analyzer")

BG_COLOR = (245, 220, 225)# ================= LOAD =================
PIECE_IMAGES = load_images()

board = [[None for _ in range(COLS)] for _ in range(ROWS)]

dragging_piece = None
old_r, old_c = None, None

piece_limits = {
    "wK":1, "wQ":1, "wR":2, "wB":2, "wN":2, "wP":8,
    "bK":1, "bQ":1, "bR":2, "bB":2, "bN":2, "bP":8
}
piece_count = {k:0 for k in piece_limits}
palette = []

# ================= LOOP =================
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BG_COLOR)
    # ===== TITLE =====
    title_font = pygame.font.SysFont("Arial", 28, bold=True)
    title = title_font.render("Chess Position Analyzer", True, (0,0,0))
    screen.blit(title, (WIDTH//2 - 180, 30))
    
    mouse_pos = pygame.mouse.get_pos()
    events = pygame.event.get()

    # ===== QUIT =====
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # ===== PANEL =====
    white_btn, black_btn, analyse_btn = draw_panel(screen, turn, BOARD_LEFT_X, SQUARE_SIZE)

    # ===== STATE =====
    state = {
        "board": board,
        "palette": palette,
        "mouse_pos": mouse_pos,
        "coord_to_square": lambda pos: coord_to_square(
            pos, BOARD_TOP_Y, BOARD_LEFT_X, BOARD_HEIGHT, SQUARE_SIZE
        ),
        "piece_count": piece_count,
        "piece_limits": piece_limits,
        "turn": turn,
        "white_btn": white_btn,
        "black_btn": black_btn,
        "analyse_btn": analyse_btn,
        "dragging_piece": dragging_piece,
        "old_r": old_r,
        "old_c": old_c
    }

    # ===== INPUT =====
    dragging_piece, old_r, old_c, turn = handle_input(events, state)

    # ===== DRAW =====
    draw_board(screen, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE)
    draw_pieces(screen, board, PIECE_IMAGES, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE)
    palette = draw_palette(screen, PIECE_IMAGES, WIDTH)

    # ===== DRAG VISUAL =====
    if dragging_piece and dragging_piece in PIECE_IMAGES:
        mx, my = mouse_pos
        screen.blit(
            PIECE_IMAGES[dragging_piece],
            (mx - SQUARE_SIZE//2, my - SQUARE_SIZE//2)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()