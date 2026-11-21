import random
import sys
import pygame

GRID = 4
CELL = 110
GAP = 10
CODE_LEN = 6
WIDTH, HEIGHT = 520, 720
GRID_W = GRID * CELL + (GRID - 1) * GAP
GRID_X = (WIDTH - GRID_W) // 2
GRID_Y = 220

BG = (24, 26, 38)
CELL_COLOR = (52, 58, 82)
CELL_HOVER = (70, 78, 108)
LIT = (255, 210, 70)
GOOD = (80, 200, 120)
BAD = (230, 80, 80)
TEXT = (235, 235, 245)
DIM = (150, 155, 180)

MOVES = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
ARROWS = {"U": "^", "D": "v", "L": "<", "R": ">"}


def generate_round():
    while True:
        start = (random.randrange(GRID), random.randrange(GRID))
        pos = start
        code, path = [], [start]
        for _ in range(CODE_LEN):
            options = []
            for letter, (dr, dc) in MOVES.items():
                nr, nc = pos[0] + dr, pos[1] + dc
                if 0 <= nr < GRID and 0 <= nc < GRID:
                    options.append((letter, (nr, nc)))
            letter, pos = random.choice(options)
            code.append(letter)
            path.append(pos)
        if pos != start:
            return start, code, path


def cell_rect(r, c):
    x = GRID_X + c * (CELL + GAP)
    y = GRID_Y + r * (CELL + GAP)
    return pygame.Rect(x, y, CELL, CELL)


def cell_at(pos):
    for r in range(GRID):
        for c in range(GRID):
            if cell_rect(r, c).collidepoint(pos):
                return (r, c)
    return None


def draw_text(surf, font, text, color, center):
    img = font.render(text, True, color)
    surf.blit(img, img.get_rect(center=center))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Direction Code Grid")
    clock = pygame.time.Clock()

    title_font = pygame.font.SysFont("arial", 34, bold=True)
    code_font = pygame.font.SysFont("consolas,couriernew,monospace", 46, bold=True)
    font = pygame.font.SysFont("arial", 22)
    small = pygame.font.SysFont("arial", 18)

    score = 0
    streak = 0
    best = 0

    start, code, path = generate_round()
    state = "playing"
    clicked = None
    show_hint = False

    while True:
        mouse = pygame.mouse.get_pos()
        target = path[-1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_h and state == "playing":
                    show_hint = not show_hint
                if event.key in (pygame.K_SPACE, pygame.K_RETURN) and state != "playing":
                    start, code, path = generate_round()
                    state, clicked, show_hint = "playing", None, False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == "playing":
                    cell = cell_at(event.pos)
                    if cell is not None:
                        clicked = cell
                        if cell == target:
                            state = "correct"
                            streak += 1
                            best = max(best, streak)
                            score += 1 if not show_hint else 0
                        else:
                            state = "wrong"
                            streak = 0
                else:
                    start, code, path = generate_round()
                    state, clicked, show_hint = "playing", None, False

        screen.fill(BG)
        draw_text(screen, title_font, "DIRECTION CODE", TEXT, (WIDTH // 2, 40))

        total_w = CODE_LEN * 56
        x0 = WIDTH // 2 - total_w // 2 + 28
        for i, letter in enumerate(code):
            draw_text(screen, code_font, letter, LIT, (x0 + i * 56, 105))
            if show_hint and state == "playing":
                draw_text(screen, small, ARROWS[letter], DIM, (x0 + i * 56, 140))

        draw_text(screen, small, "U = up   D = down   L = left   R = right", DIM,
                  (WIDTH // 2, 170))
        draw_text(screen, small, "Start at the lit square, follow the code, click where you land.",
                  DIM, (WIDTH // 2, 195))

        for r in range(GRID):
            for c in range(GRID):
                rect = cell_rect(r, c)
                color = CELL_COLOR
                if state == "playing" and rect.collidepoint(mouse):
                    color = CELL_HOVER
                if (r, c) == start:
                    color = LIT
                if state != "playing":
                    if (r, c) == target:
                        color = GOOD
                    elif (r, c) == clicked:
                        color = BAD
                pygame.draw.rect(screen, color, rect, border_radius=14)

                if (r, c) == start:
                    draw_text(screen, font, "START", (40, 30, 0), rect.center)

        if (show_hint and state == "playing") or state != "playing":
            pts = [cell_rect(*p).center for p in path]
            pygame.draw.lines(screen, (255, 255, 255), False, pts, 3)
            for p in pts:
                pygame.draw.circle(screen, (255, 255, 255), p, 6)

        status_y = GRID_Y + GRID_W + 40
        if state == "playing":
            msg = "Hint ON (no point this round)" if show_hint else "Press H for a hint"
            draw_text(screen, small, msg, DIM, (WIDTH // 2, status_y))
        elif state == "correct":
            draw_text(screen, font, "Correct! Click or press SPACE for next", GOOD,
                      (WIDTH // 2, status_y))
        else:
            draw_text(screen, font, "Wrong! Green was the answer. Click for next", BAD,
                      (WIDTH // 2, status_y))

        draw_text(screen, font,
                  f"Score: {score}    Streak: {streak}    Best: {best}", TEXT,
                  (WIDTH // 2, status_y + 40))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()