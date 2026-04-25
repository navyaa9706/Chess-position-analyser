import pygame

def draw_button(screen, WIDTH):
    rect = pygame.Rect(WIDTH//2 - 90, 30, 180, 50)

    shadow = rect.copy()
    shadow.y += 4
    pygame.draw.rect(screen, (50,50,80), shadow, border_radius=12)

    pygame.draw.rect(screen, (90, 90, 160), rect, border_radius=12)

    #hover ka effect
    if rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (120, 120, 200), rect, border_radius=12)

    font = pygame.font.SysFont("Arial", 22, bold=True)
    text = font.render("Analyse", True, (255,255,255))

    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

    return rect