import pygame

MOVE_COLOR = (0, 255, 0, 100)
LAST_MOVE_COLOR = (255, 255, 0, 100)

def draw_highlight(screen, row, col, BOARD_TOP_Y, SQUARE_SIZE, color):
    s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
    s.fill(color)
    screen.blit(s, (col * SQUARE_SIZE, BOARD_TOP_Y + row * SQUARE_SIZE))


def highlight_moves(screen, moves, BOARD_TOP_Y, SQUARE_SIZE):
    for (r, c) in moves:
        draw_highlight(screen, r, c, BOARD_TOP_Y, SQUARE_SIZE, MOVE_COLOR)


def highlight_last_move(screen, move, BOARD_TOP_Y, SQUARE_SIZE):
    if move:
        (r1, c1), (r2, c2) = move
        draw_highlight(screen, r1, c1, BOARD_TOP_Y, SQUARE_SIZE, LAST_MOVE_COLOR)
        draw_highlight(screen, r2, c2, BOARD_TOP_Y, SQUARE_SIZE, LAST_MOVE_COLOR)