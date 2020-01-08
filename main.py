import sys
import pygame
import random
pygame.init()

white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0

print('Sorting algorithm')
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sorting Algorithm")
clock = pygame.time.Clock()


class Pillar:
    def __init__(self, area, color):
        self.area = area
        self.color = color


j = 0
pillar_list = []
for i in range(0, 32):
    height = random.randint(1, 200)
    pillar_list.append(Pillar((0 + j, 240 - height, 10, height), red))  # [x, y, width, height]
    pygame.draw.rect(screen, pillar_list[i].color, pygame.Rect(pillar_list[i].area))
    j = j + 10


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    clock.tick(30)
