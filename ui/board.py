import pygame

LIGHT = (240, 217, 181) #pinkkkkk
DARK  = (200, 120, 140)

def draw_board(screen, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE):
    for row in range(8):
        for col in range(8):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            x = BOARD_LEFT_X + col * SQUARE_SIZE
            y = BOARD_TOP_Y + row * SQUARE_SIZE
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, board, PIECE_IMAGES, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece is not None:
                img = PIECE_IMAGES.get(piece)
                if img:
                    x = BOARD_LEFT_X + col * SQUARE_SIZE
                    y = BOARD_TOP_Y + row * SQUARE_SIZE
                    screen.blit(img, (x, y))