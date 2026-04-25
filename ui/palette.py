import pygame

def draw_palette(screen, PIECE_IMAGES):
    white_pieces = ["wK","wQ","wR","wB","wN","wP"]
    black_pieces = ["bK","bQ","bR","bB","bN","bP"]

    start_x = (600 - 360) // 2  
    white_y = 550
    black_y = 620

    palette_rects = []

    for i, p in enumerate(white_pieces):
        x = start_x + i * 60
        rect = pygame.Rect(x, white_y, 40, 40)
        palette_rects.append((p, rect))
        screen.blit(PIECE_IMAGES[p], (x, white_y))

    for i, p in enumerate(black_pieces):
        x = start_x + i * 60
        rect = pygame.Rect(x, black_y, 40, 40)
        palette_rects.append((p, rect))
        screen.blit(PIECE_IMAGES[p], (x, black_y))

    return palette_rects