import pygame
import random

pygame.init()

bgcolors = [
    pygame.Color("red"),
    pygame.Color("blue"),
    pygame.Color("yellow")
]

playercolors = [
    pygame.Color("green"),
    pygame.Color("purple"),
    pygame.Color("orange")
]

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

spriteeve = pygame.USEREVENT + 1
bgeve = pygame.USEREVENT + 2
bg_color = random.choice(bgcolors)


class Player(pygame.sprite.Sprite):
    def __init__(self, color, h, w):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 450)
        self.rect.y = random.randint(0, 450)
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            pygame.event.post(pygame.event.Event(spriteeve))
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] = -self.velocity[1]
            pygame.event.post(pygame.event.Event(bgeve))

    def random_color(self):
        self.image.fill(random.choice(playercolors))


def random_bg_color():
    global bg_color
    bg_color = random.choice(bgcolors)


all_sprites_list = pygame.sprite.Group()
spr1 = Player("green", 50, 50)
all_sprites_list.add(spr1)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == spriteeve:
            spr1.random_color()
        elif event.type == bgeve:
            random_bg_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()

pygame.quit()