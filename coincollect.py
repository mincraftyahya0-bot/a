import pygame
import random
import time
pygame.init()
coin_sound = pygame.mixer.Sound("coin.wav")

scrw = 500
scrh = 500
screen = pygame.display.set_mode((scrw, scrh))
pygame.display.set_caption("coin collector")

box_size = 50
x = (scrw - box_size) // 2
y = (scrh - box_size) // 2

coin_size = 30
x2 = random.randint(0, scrw - coin_size)
y2 = random.randint(0, scrh - coin_size)

score = 0
font = pygame.font.SysFont("Arial", 30)

start_time = time.time()

running = True
clock = pygame.Clock()

while running:
    clock.tick(120) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        x -= 3
    if pressed[pygame.K_d]:
        x += 3
    if pressed[pygame.K_w]:
        y -= 3
    if pressed[pygame.K_s]:
        y += 3

    if x < 0:
        x = 0
    if x > scrw - box_size:
        x = scrw - box_size
    if y < 0:
        y = 0
    if y > scrh - box_size:
        y = scrh - box_size

    player_rect = pygame.Rect(x, y, box_size, box_size)
    coin_rect = pygame.Rect(x2, y2, coin_size, coin_size)

    if player_rect.colliderect(coin_rect):
        score += 1
        x2 = random.randint(0, scrw - coin_size)
        y2 = random.randint(0, scrh - coin_size)
        coin_sound.play()

    seconds_passed = int(time.time() - start_time)
    time_left = max(0, 60 - seconds_passed)

    if time_left == 0:
        running = False

    screen.fill((0, 0, 0))
    
    score_surface = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

    time_surface = font.render("Time: " + str(time_left), True, (255, 255, 255))
    screen.blit(time_surface, (scrw - 120, 10))

    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    pygame.draw.rect(screen, (255, 255, 0), coin_rect)
    pygame.display.flip()

pygame.quit()