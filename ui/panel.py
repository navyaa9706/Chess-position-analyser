import pygame


def draw_panel(screen, turn, PIECE_IMAGES, BOARD_LEFT_X, BOARD_TOP_Y, SQUARE_SIZE):

    BOARD_RIGHT = BOARD_LEFT_X + 8 * SQUARE_SIZE

    panel_x = BOARD_RIGHT + 28
    panel_y = BOARD_TOP_Y
    panel_w = 260
    panel_h = 8 * SQUARE_SIZE

    pygame.draw.rect(screen, (248, 236, 241),
                     (panel_x, panel_y, panel_w, panel_h), border_radius=10)
    pygame.draw.rect(screen, (190, 150, 165),
                     (panel_x, panel_y, panel_w, panel_h), 1, border_radius=10)

    font_title = pygame.font.SysFont("Georgia", 16, bold=True)
    font_label = pygame.font.SysFont("Arial",   13)
    font_btn   = pygame.font.SysFont("Arial",   14)

    pad = 20
    cy  = panel_y + 18

    t = font_title.render("ANALYSIS", True, (100, 65, 80))
    screen.blit(t, (panel_x + pad, cy))
    cy += t.get_height() + 14

    def divider():
        nonlocal cy
        pygame.draw.line(screen, (210, 180, 192),
                         (panel_x + pad, cy),
                         (panel_x + panel_w - pad, cy), 1)
        cy += 12

    screen.blit(font_label.render("Turn", True, (130, 90, 108)), (panel_x + pad, cy))
    cy += font_label.get_height() + 8

    btn_w, btn_h = 96, 36
    white_rect = pygame.Rect(panel_x + pad,             cy, btn_w, btn_h)
    black_rect = pygame.Rect(panel_x + pad + btn_w + 8, cy, btn_w, btn_h)

    for rect, label, is_active in [
        (white_rect, "White", turn == "w"),
        (black_rect, "Black", turn == "b"),
    ]:
        bg    = (255, 255, 255) if is_active else (238, 222, 228)
        bdr   = (120, 80, 100) if is_active else (200, 170, 182)
        bdr_w = 2 if is_active else 1
        pygame.draw.rect(screen, bg,  rect, border_radius=7)
        pygame.draw.rect(screen, bdr, rect, bdr_w, border_radius=7)
        lbl = font_btn.render(label, True,
                              (50, 30, 42) if is_active else (140, 100, 118))
        screen.blit(lbl, (rect.x + rect.w // 2 - lbl.get_width() // 2,
                          rect.y + rect.h // 2 - lbl.get_height() // 2))

    cy += btn_h + 16
    divider()

    # ── Piece palette ─────────────────────────────────────────────────────────
    ICON = 46
    GAP  = 8

    def crop_transparent(surf):
        r = surf.get_bounding_rect()
        cropped = pygame.Surface(r.size, pygame.SRCALPHA)
        cropped.blit(surf, (0, 0), r)
        return cropped

    def palette_row(pieces, start_y):
        row = []

        for i, p in enumerate(pieces):
            x    = panel_x + pad + i * (ICON + GAP)
            rect = pygame.Rect(x, start_y, ICON, ICON)
            print(f"{p}: rect={rect}")  
            pygame.draw.rect(screen, (242, 228, 234), rect, border_radius=8)
            pygame.draw.rect(screen, (200, 170, 182), rect, 1, border_radius=8)
            img = PIECE_IMAGES.get(p)
            if img:
                img = crop_transparent(img)
                orig_w, orig_h = img.get_size()
                target_h = ICON - 4
                target_w = int(orig_w * target_h / orig_h)
                target_w = min(target_w, ICON - 2)
                img_s = pygame.transform.smoothscale(img, (target_w, target_h))
                blit_x = x + (ICON - target_w) // 2
                blit_y = start_y + (ICON - target_h) // 2
                screen.blit(img_s, (blit_x, blit_y))
        return row

    palette = []

    screen.blit(font_label.render("White pieces", True, (130, 90, 108)),
                (panel_x + pad, cy))
    cy += font_label.get_height() + 6
    palette += palette_row(["wK", "wQ", "wR"], cy)
    cy += ICON + GAP
    palette += palette_row(["wB", "wN", "wP"], cy)
    cy += ICON + 14

    screen.blit(font_label.render("Black pieces", True, (130, 90, 108)),
                (panel_x + pad, cy))
    cy += font_label.get_height() + 6
    palette += palette_row(["bK", "bQ", "bR"], cy)
    cy += ICON + GAP
    palette += palette_row(["bB", "bN", "bP"], cy)
    cy += ICON + 16

    divider()

    # ── Analyse button ────────────────────────────────────────────────────────
    analyse_rect = pygame.Rect(panel_x + pad, cy, panel_w - 2 * pad, 44)
    pygame.draw.rect(screen, (255, 255, 255), analyse_rect, border_radius=8)
    pygame.draw.rect(screen, (150, 110, 130), analyse_rect, 1, border_radius=8)

    font_abtn = pygame.font.SysFont("Georgia", 15, bold=True)
    atxt = font_abtn.render("Analyse position", True, (70, 40, 55))
    screen.blit(atxt, (analyse_rect.x + analyse_rect.w // 2 - atxt.get_width() // 2,
                       analyse_rect.y + analyse_rect.h // 2 - atxt.get_height() // 2))
    cy += 44 + 14

    # ── Result box ────────────────────────────────────────────────────────────
    screen.blit(font_label.render("Result", True, (130, 90, 108)),
                (panel_x + pad, cy))
    cy += font_label.get_height() + 6

    result_h = panel_y + panel_h - cy - 14
    if result_h > 0:
        result_rect = pygame.Rect(panel_x + pad, cy, panel_w - 2 * pad, result_h)
        pygame.draw.rect(screen, (238, 222, 228), result_rect, border_radius=6)
        hint = font_label.render("Place pieces and press analyse",
                                 True, (160, 120, 138))
        screen.blit(hint, (result_rect.x + 8, result_rect.y + 8))

    return white_rect, black_rect, analyse_rect, palette