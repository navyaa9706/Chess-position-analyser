import pygame
from config import LIGHT_SQ, DARK_SQ, LABEL_COLOR


def draw_board(screen, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE):
    font = pygame.font.SysFont("Arial", 15)

    for row in range(8):
        for col in range(8):
            color = LIGHT_SQ if (row + col) % 2 == 0 else DARK_SQ

            x = BOARD_LEFT_X + col * SQUARE_SIZE
            y = BOARD_TOP_Y  + row * SQUARE_SIZE

            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            # rank numbers on left
            if col == 0:
                text = font.render(str(8 - row), True, LABEL_COLOR)
                screen.blit(text, (x - 22, y + SQUARE_SIZE // 2 - 8))

            # file letters below
            if row == 7:
                letter = chr(ord('a') + col)
                text = font.render(letter, True, LABEL_COLOR)
                screen.blit(text, (x + SQUARE_SIZE // 2 - 5, y + SQUARE_SIZE + 6))


def draw_pieces(screen, board, PIECE_IMAGES, BOARD_TOP_Y, BOARD_LEFT_X, SQUARE_SIZE):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                img = PIECE_IMAGES.get(piece)
                if img:
                    x = BOARD_LEFT_X + col * SQUARE_SIZE
                    y = BOARD_TOP_Y  + row * SQUARE_SIZE
                    screen.blit(img, (x, y))