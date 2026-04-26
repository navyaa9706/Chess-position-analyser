import pygame
import os

def load_images():
    piece_files = {
        "wP": "wp.png", "wR": "wr.png", "wN": "wn.png", "wB": "wb.png", "wQ": "wq.png", "wK": "wk.png",
        "bP": "bp.png", "bR": "br.png", "bN": "bn.png", "bB": "bb.png", "bQ": "bq.png", "bK": "bk.png"
    }

    images = {}

    for piece, filename in piece_files.items():
        path = os.path.join("assets/images", filename)
        if os.path.exists(path):
            img = pygame.image.load(path)
            images[piece] = pygame.transform.scale(img, (40, 40))

    return images