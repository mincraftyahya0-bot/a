#activity1
import pygame

pygame.init()
#screen=pygame.display.set_mode((400,500))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,60))
    pygame.display.flip()
#activity2
green=(0,255,0)
screen.fill((255,255,255))
pygame.draw.circle(screen,green,(300,300),50)
pygame.draw.circle(screen,green,(100,100),50,3)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
#activity3
def main():
    screenw, screenh = 500, 500
    screen = pygame.display.set_mode((screenw, screenh))
    pygame.display.set_caption("color changing sprite")

    color = {
        "red": pygame.Color("red"),
        "orange": pygame.Color("orange"),
        "yellow": pygame.Color("yellow"),
        "green": pygame.Color("green"),
        "white": pygame.Color("white")
    }

    curcolor = color["white"]
    x, y = 30, 30
    sprw, sprh = 60, 60
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3

        x = max(0, min(x, screenw - sprw))
        y = max(0, min(y, screenh - sprh))

        if x == 0:
            curcolor = color["green"]
        elif x == screenw - sprw:
            curcolor = color["orange"]
        elif y == 0:
            curcolor = color["red"]
        elif y == screenh - sprh:
            curcolor = color["yellow"]
        else:
            curcolor = color["white"]

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, curcolor, (x, y, sprw, sprh))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()