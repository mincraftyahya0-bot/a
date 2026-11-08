import pygame
import time
import random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500, 500))
running = True
x = 30
y = 225
x2 = 420
y2 = 225
scrw = 500
scrh = 500
taged = False
box_size = 50
font = pygame.font.Font(None, 48)
tagger = pygame.Rect(x, y, box_size, box_size)
runner = pygame.Rect(x2, y2, box_size, box_size)
clock = pygame.time.Clock()
start_time = time.time()

obstacles = []

for i in range(8):
    for attempt in range(100):
        width = random.randint(20, 80)
        height = random.randint(20, 80)
        ox = random.randint(0, scrw - width)
        oy = random.randint(0, scrh - height)

        wall = pygame.Rect(ox, oy, width, height)

        if not wall.colliderect(tagger) and not wall.colliderect(runner):
            if not any(wall.colliderect(other) for other in obstacles):
                obstacles.append(wall)
                break

def move_player(player, dx, dy, obstacles):
    player.x += dx

    for wall in obstacles:
        if player.colliderect(wall):
            if dx > 0:
                player.right = wall.left
            elif dx < 0:
                player.left = wall.right

    player.y += dy

    for wall in obstacles:
        if player.colliderect(wall):
            if dy > 0:
                player.bottom = wall.top
            elif dy < 0:
                player.top = wall.bottom

    player.clamp_ip(screen.get_rect())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        break

    screen.fill("black")

    for wall in obstacles:
        pygame.draw.rect(screen, "orange", wall)

    if not taged:
        pressed = pygame.key.get_pressed()

        dx = 0
        dy = 0
        dx2 = 0
        dy2 = 0

        if pressed[pygame.K_LEFT]:
            dx -= 3
        if pressed[pygame.K_RIGHT]:
            dx += 3
        if pressed[pygame.K_UP]:
            dy -= 3
        if pressed[pygame.K_DOWN]:
            dy += 3

        if pressed[pygame.K_a]:
            dx2 -= 3
        if pressed[pygame.K_d]:
            dx2 += 3
        if pressed[pygame.K_w]:
            dy2 -= 3
        if pressed[pygame.K_s]:
            dy2 += 3

        move_player(tagger, dx, dy, obstacles)
        move_player(runner, dx2, dy2, obstacles)

        x, y = tagger.x, tagger.y
        x2, y2 = runner.x, runner.y

        if tagger.colliderect(runner):
            taged = True

        seconds_passed = int(time.time() - start_time)
        time_left = max(0, 60 - seconds_passed)

    pygame.draw.rect(screen, "red", tagger)
    pygame.draw.rect(screen, "blue", runner)

    if taged:
        score_surface = font.render("TAGGER WINS!!!!", True, (255, 255, 255))
        screen.blit(score_surface, (110, 220))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
        continue

    time_surface = font.render("Time: " + str(time_left), True, (255, 255, 255))
    screen.blit(time_surface, (scrw - 300, 10))

    if time_left == 0:
        score_surface = font.render("RUNNER WINS!!!!", True, (255, 255, 255))
        screen.blit(score_surface, (110, 220))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
        continue

    pygame.display.flip()
    clock.tick(90)

pygame.quit()