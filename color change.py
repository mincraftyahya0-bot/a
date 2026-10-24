import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        colors = ["red", "blue", "green", "yellow", "purple"]
        self.image.fill(random.choice(colors))

sprite1 = Sprite(100, 150)
sprite2 = Sprite(400, 150)

sprites = pygame.sprite.Group(sprite1, sprite2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            for sprite in sprites:
                sprite.change_color()

    screen.fill("white")
    sprites.draw(screen)
    pygame.display.update()

pygame.quit()