import pygame

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    screen.fill("black")

    if not taged:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3

        if x < 0:
            x = 0
        if x > scrw - box_size:
            x = scrw - box_size
        if y < 0:
            y = 0
        if y > scrh - box_size:
            y = scrh - box_size

        if pressed[pygame.K_a]:
            x2 -= 3
        if pressed[pygame.K_d]:
            x2 += 3
        if pressed[pygame.K_w]:
            y2 -= 3
        if pressed[pygame.K_s]:
            y2 += 3

        if x2 < 0:
            x2 = 0
        if x2 > scrw - box_size:
            x2 = scrw - box_size
        if y2 < 0:
            y2 = 0
        if y2 > scrh - box_size:
            y2 = scrh - box_size

        tagger.x = x
        tagger.y = y
        runner.x = x2
        runner.y = y2

        if tagger.colliderect(runner):
            taged = True

    pygame.draw.rect(screen, "red", tagger)
    pygame.draw.rect(screen, "blue", runner)

    if taged:
        score_surface = font.render("TAGGER WINS!!1!", True, (255, 255, 255))
        screen.blit(score_surface, (110, 220))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False
        continue

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
