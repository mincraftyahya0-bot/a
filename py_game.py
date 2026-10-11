#activity1
import pygame
pygame.init()
pygame.display.set_mode((400,500))
pygame.APP_DIDENTERBACKGROUND.
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()