import pygame
import random
pygame.init()
bgcolors=[pygame.Color("red"),
          pygame.Color("blue"),
          pygame.Color("yellow")]
playercolors=[
    pygame.Color("green"),
    pygame.Color("purple"),
    pygame.Color("orange")
]
def playerrancol():
    return random.choice(playercolors)
def bgrancol():
    return random.choice(bgcolors)
x=0
y=0
pygame.display.set_mode((500, 500))
b=True
class player(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        self.image.fill(playercolors)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    