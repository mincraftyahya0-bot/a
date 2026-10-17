#activity1
import pygame
pygame.init()
screen=pygame.display.set_mode((400,500))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,60))
    font = pygame.font.SysFont("Arial", 30)
    text = font.render("text", True, (255, 255, 255))
    screen.blit(text, (0, 0))
    pygame.display.flip()