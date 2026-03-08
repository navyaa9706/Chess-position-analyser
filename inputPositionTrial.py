import pygame
import sys
import os


pygame.init()

WIDTH, HEIGHT = 600, 700
BOARD_TOP_Y = 100
BOARD_HEIGHT = 400  
SQUARE_SIZE = BOARD_HEIGHT//8
ROWS, COLS = 8, 8
PIECE_SIZE = 40
BUTTON_WIDTH, BUTTON_HEIGHT = 180, 50
FONT_LARGE = pygame.font.SysFont("Arial", 24, bold=True)
FONT = pygame.font.SysFont("Arial", 20)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
BUTTON_COLOR = (100, 100, 150)
BUTTON_HOVER = (130, 130, 180)
BG_COLOR = (240, 220, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Position Setup")

# Load PNGs
PIECE_IMAGES = {}
piece_files = {
    "wP": "wp.png", "wR": "wr.png", "wN": "wn.png", "wB": "wb.png", "wQ": "wq.png", "wK": "wk.png",
    "bP": "bp.png", "bR": "br.png", "bN": "bn.png", "bB": "bb.png", "bQ": "bq.png", "bK": "bk.png"
}

def load_images():
    for piece, filename in piece_files.items():
        if os.path.exists(filename):
            img = pygame.image.load(filename)
            PIECE_IMAGES[piece] = pygame.transform.scale(img, (PIECE_SIZE, PIECE_SIZE))

load_images()

# Infinite supply tracking
piece_count = {p: 0 for p in piece_files.keys()}
board = [[None for _ in range(COLS)] for _ in range(ROWS)]
pieces_below = []

def init_pieces_below():
    """ONE representative per piece type - infinite supply!"""
    pieces_below.clear()
    
    # White pieces - TOP ROW (fits screen)
    white_row_y = BOARD_TOP_Y + BOARD_HEIGHT + 30
    white_pieces = ["wK", "wQ", "wR", "wB", "wN", "wP"]
    start_x = (WIDTH - len(white_pieces) * (PIECE_SIZE + 15)) // 2
    for i, p in enumerate(white_pieces):
        x = start_x + i * (PIECE_SIZE + 15)
        rect = pygame.Rect(x-PIECE_SIZE//2, white_row_y-PIECE_SIZE//2, PIECE_SIZE, PIECE_SIZE)
        pieces_below.append((p, x, white_row_y, rect))
    
    black_row_y = BOARD_TOP_Y + BOARD_HEIGHT + 100
    black_pieces = ["bK", "bQ", "bR", "bB", "bN", "bP"]
    start_x = (WIDTH - len(black_pieces) * (PIECE_SIZE + 15)) // 2
    for i, p in enumerate(black_pieces):
        x = start_x + i * (PIECE_SIZE + 15)
        rect = pygame.Rect(x-PIECE_SIZE//2, black_row_y-PIECE_SIZE//2, PIECE_SIZE, PIECE_SIZE)
        pieces_below.append((p, x, black_row_y, rect))

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            y = BOARD_TOP_Y + row * SQUARE_SIZE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, y, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces_on_board():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece and piece in PIECE_IMAGES:
                img = PIECE_IMAGES[piece]
                x = col * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) // 2
                y = BOARD_TOP_Y + row * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) // 2
                screen.blit(img, (x, y))

def draw_pieces_below():
    """Show count next to each piece."""
    for i, (piece_str, x, y, rect) in enumerate(pieces_below):
        if piece_str in PIECE_IMAGES:
            screen.blit(PIECE_IMAGES[piece_str], (x - PIECE_SIZE//2, y - PIECE_SIZE//2))
        else:
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 3)
            text = FONT.render(piece_str, True, BLACK)
            screen.blit(text, text.get_rect(center=(x, y)))
        
        # Show usage count
        count = piece_count[piece_str]
        count_text = FONT.render(str(count), True, (100, 100, 100))
        screen.blit(count_text, (x + PIECE_SIZE//2 + 5, y))

def draw_analyse_button(hover=False):
    x = WIDTH - BUTTON_WIDTH - 20
    y = 20
    color = BUTTON_HOVER if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.draw.rect(screen, BLACK, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT), 3)
    label = FONT.render("Analyse Position", True, WHITE)
    screen.blit(label, label.get_rect(center=(x + BUTTON_WIDTH//2, y + BUTTON_HEIGHT//2)))
    return pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)

def coord_to_square(pos):
    x, y = pos
    if BOARD_TOP_Y <= y < BOARD_TOP_Y + BOARD_HEIGHT:
        row = (y - BOARD_TOP_Y) // SQUARE_SIZE
        col = x // SQUARE_SIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            return row, col
    return None

# Initialize
dragging_piece = None
init_pieces_below()
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_rect = pygame.Rect(WIDTH - BUTTON_WIDTH - 20, 20, BUTTON_WIDTH, BUTTON_HEIGHT)
            if button_rect.collidepoint(mouse_pos):
                print("=== ANALYSING ===")
                for row in board:
                    print(" ".join([".." if c is None else c for c in row]))
                print("Piece counts:", piece_count)
                continue

            for i, (p, px, py, rect) in enumerate(pieces_below):
                if rect.collidepoint(mouse_pos):
                    dragging_piece = p
                    piece_count[p] += 1
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_piece:
                square = coord_to_square(mouse_pos)
                if square:
                    row, col = square
                    board[row][col] = dragging_piece
                dragging_piece = None

    screen.fill(BG_COLOR)

    # Header
    title = FONT_LARGE.render("Chess Position Setup", True, BLACK)
    screen.blit(title, (20, 30))

    # Board frame + board
    pygame.draw.rect(screen, WHITE, (0, BOARD_TOP_Y - 5, WIDTH, BOARD_HEIGHT + 10), 0, 10)
    draw_board()
    draw_pieces_on_board()

    # PIECES SECTION - CLEARLY LABELED
    pieces_top_y = BOARD_TOP_Y + BOARD_HEIGHT + 10
    
    # White label + line
    white_label = FONT.render("WHITE PIECES", True, BLACK)
    screen.blit(white_label, (50, pieces_top_y))
    pygame.draw.line(screen, BLACK, (30, pieces_top_y + 25), (WIDTH-30, pieces_top_y + 25), 2)
    
    # Black label + line  
    black_label = FONT.render("BLACK PIECES", True, BLACK)
    screen.blit(black_label, (50, pieces_top_y + 80))
    pygame.draw.line(screen, BLACK, (30, pieces_top_y + 105), (WIDTH-30, pieces_top_y + 105), 2)
    
    draw_pieces_below()

    # Button
    button_rect = draw_analyse_button(
        mouse_pos[0] >= WIDTH - BUTTON_WIDTH - 20 and mouse_pos[1] <= 70
    )

    # Dragged piece
    if dragging_piece and dragging_piece in PIECE_IMAGES:
        mx, my = mouse_pos
        screen.blit(PIECE_IMAGES[dragging_piece], (mx - PIECE_SIZE//2, my - PIECE_SIZE//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
