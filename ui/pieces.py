import pygame
import os

def load_images(piece_files, size):
    images = {}
    for p, file in piece_files.items():
        path = os.path.join("assets/images", file)
        if os.path.exists(path):
            img = pygame.image.load(path)
            images[p] = pygame.transform.scale(img, (size, size))
    return images