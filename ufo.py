import math
import random
import pygame

scrw = 800
scrh = 500
plstx = 370
plsty = 380
enstymin = 10
enstymax = 150
enspx = 4
enspy = 40
bultspy = 10
coldist = 27

pygame.init()
screen = pygame.display.set_mode((scrw, scrh))
pygame.display.set_caption("space invaders")

try:
    bg = pygame.image.load("background.png").convert()
except pygame.error:
    bg = pygame.Surface((scrw, scrh))
    bg.fill((10, 10, 25))

try:
    icon = pygame.image.load("ufo.png").convert_alpha()
except pygame.error:
    icon = pygame.Surface((32, 32), pygame.SRCALPHA)
    pygame.draw.circle(icon, (255, 255, 255), (16, 16), 16)
pygame.display.set_icon(icon)

try:
    pl = pygame.image.load("player.png").convert_alpha()
except pygame.error:
    pl = pygame.Surface((64, 20), pygame.SRCALPHA)
    pygame.draw.rect(pl, (0, 255, 0), (0, 0, 64, 20))

playerX = plstx
playerY = plsty
playerX_change = 0

enemy_images = []
enemy_x = []
enemy_y = []
enemy_xch = []
enemy_ych = []
ennum = 6
for i in range(ennum):
    try:
        enemy_img = pygame.image.load("enemy.png").convert_alpha()
    except pygame.error:
        enemy_img = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.polygon(enemy_img, (255, 0, 0), [(16, 0), (31, 31), (0, 31)])
    enemy_images.append(enemy_img)
    enemy_x.append(random.randint(0, scrw - enemy_img.get_width()))
    enemy_y.append(random.randint(enstymin, enstymax))
    enemy_xch.append(enspx)
    enemy_ych.append(enspy)

try:
    bullet_img = pygame.image.load("bullet.png").convert_alpha()
except pygame.error:
    bullet_img = pygame.Surface((8, 20), pygame.SRCALPHA)
    pygame.draw.rect(bullet_img, (255, 255, 0), (0, 0, 8, 20))

bultx = 0
bulty = playerY
bultsta = "ready"
score = 0

font = pygame.font.Font("freesansbold.ttf", 32)
texx = 10
texy = 10
ovrfon = pygame.font.Font("freesansbold.ttf", 64)

def shscr(x, y):
    score_text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def ovrtxt():
    game_over_text = ovrfon.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))


def pla(x, y):
    screen.blit(pl, (x, y))


def enm(x, y, i):
    screen.blit(enemy_images[i], (x, y))


def firebult(x, y):
    global bultsta, bultx, bulty
    bultsta = "fire"
    bultx = x
    bulty = y


def isCollision(enemy_x_pos, enemy_y_pos, bullet_x_pos, bullet_y_pos):
    dist = math.sqrt((enemy_x_pos - bullet_x_pos) ** 2 + (enemy_y_pos - bullet_y_pos) ** 2)
    return dist < coldist


running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bultsta == "ready":
                firebult(playerX + (pl.get_width() // 2), playerY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX, scrw - pl.get_width()))

    for i in range(ennum):
        if enemy_y[i] > 340:
            for j in range(ennum):
                enemy_y[j] = 2000
            ovrtxt()
            break

        enemy_x[i] += enemy_xch[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= scrw - enemy_images[i].get_width():
            enemy_xch[i] *= -1
            enemy_y[i] += enemy_ych[i]

        if isCollision(enemy_x[i], enemy_y[i], bultx, bulty):
            bulty = playerY
            bultsta = "ready"
            score += 1
            enemy_x[i] = random.randint(0, scrw - enemy_images[i].get_width())
            enemy_y[i] = random.randint(enstymin, enstymax)

        enm(enemy_x[i], enemy_y[i], i)

    if bultsta == "fire":
        bulty -= bultspy
        if bulty <= 0:
            bulty = playerY
            bultsta = "ready"
        else:
            screen.blit(bullet_img, (bultx, bulty))

    pla(playerX, playerY)
    shscr(texx, texy)
    pygame.display.update()
    clock.tick(60)

pygame.quit()