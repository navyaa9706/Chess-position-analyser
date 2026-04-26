import pygame
import pygame

def draw_panel(screen, turn, BOARD_LEFT_X, SQUARE_SIZE):
    # ===== POSITION (relative to board) =====
    panel_x = BOARD_LEFT_X + 8 * SQUARE_SIZE + 40
    panel_y = 120
    panel_w = 240
    panel_h = 400

    # ===== PANEL BOX =====
    pygame.draw.rect(screen, (245, 230, 240), (panel_x, panel_y, panel_w, panel_h))
    pygame.draw.rect(screen, (0,0,0), (panel_x, panel_y, panel_w, panel_h), 2)

    # ===== FONTS =====
    font = pygame.font.SysFont("Arial", 20, bold=True)
    small_font = pygame.font.SysFont("Arial", 18)

    # ===== TITLE =====
    title = font.render("Analysis Panel", True, (0,0,0))
    screen.blit(title, (panel_x + 30, panel_y + 10))

    # ===== TURN LABEL =====
    turn_text = small_font.render("Turn:", True, (0,0,0))
    screen.blit(turn_text, (panel_x + 10, panel_y + 60))

    # ===== TURN BUTTONS =====
    white_rect = pygame.Rect(panel_x + 20, panel_y + 90, 80, 40)
    black_rect = pygame.Rect(panel_x + 120, panel_y + 90, 80, 40)

    white_color = (180,180,255) if turn == "w" else (220,220,220)
    black_color = (180,180,255) if turn == "b" else (220,220,220)

    pygame.draw.rect(screen, white_color, white_rect)
    pygame.draw.rect(screen, black_color, black_rect)

    pygame.draw.rect(screen, (0,0,0), white_rect, 2)
    pygame.draw.rect(screen, (0,0,0), black_rect, 2)

    # ===== BUTTON TEXT =====
    screen.blit(small_font.render("White", True, (0,0,0)),
                (white_rect.x + 10, white_rect.y + 10))
    screen.blit(small_font.render("Black", True, (0,0,0)),
                (black_rect.x + 10, black_rect.y + 10))

    # ===== ANALYSE BUTTON =====
    analyse_rect = pygame.Rect(panel_x + 50, panel_y + 180, 140, 50)

    pygame.draw.rect(screen, (120,120,200), analyse_rect)
    pygame.draw.rect(screen, (0,0,0), analyse_rect, 2)

    screen.blit(small_font.render("Analyse", True, (255,255,255)),
                (analyse_rect.x + 30, analyse_rect.y + 12))

    # ===== RETURN CLICKABLE AREAS =====
    return white_rect, black_rect, analyse_rect