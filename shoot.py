import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

square = pygame.Rect(250, 250, 50, 50)
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if square.collidepoint(event.pos):
                score += 1
                square.x = random.randint(0, 450)
                square.y = random.randint(0, 450)

    mouse_pos = pygame.mouse.get_pos()
    if square.collidepoint(mouse_pos):
        color = "green"
    else:
        color = "red"

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, square)

    text = font.render(f"Score: {score}", True, "white")
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()