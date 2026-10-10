import pygame
pygame.init()
pygame.display.set_mode((500,500))
pygame.display.set_caption("hello world")
backgroundimage=pygame.transform.scale(
    pygame.image.load("background.png").convert(),
    (500,500)
)
penguin=pygame.transform.scale(
    pygame.image.load("penguin.png").convert_alpha(200,200),

)
penguin