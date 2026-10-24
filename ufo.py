import math
import pygame
import random

scrw=800
scrh=500
plstx=370
plsty=380
enstymin=10
enstymax=150
enspx=4
enspy=40
buspy=10
coldist=27

pygame.init()
screen=pygame.display.set_mode((scrw,scrh))
bg=pygame.image.load("pixel-space-background-set.zip")
pygame.display.set_caption("space invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
pl=pygame.image.load("player.png")
plx=plstx
ply=plsty
plxch=0
en = []
enx = []
eny = []
enxch = []
enych = []
ennum = 6
for i in range(ennum):
    en.append(pygame.image.load('enemy.png'))
    enx.append(random.randint(0, scrw - 64))  # 64 is the size of the enemy
    eny.append(random.randint(enstymin, enstymax))
    enxch.append(enspx)
    enych.append(enspy)
