import pygame

def draw_button(screen):
    rect = pygame.Rect(400, 20, 180, 50)
    pygame.draw.rect(screen, (100,100,150), rect)
    return rect