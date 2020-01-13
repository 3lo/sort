import sys
import pygame
import random
pygame.init()

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
        self.height = area[3]

    @classmethod
    def bubbleSort(cls, arr):  # Method to update class attributes
        n = len(arr)
        for i in range(n):  # Traverse through all array elements
            for j in range(0, n - i - 1):  # Last i elements are already in place
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j].height > arr[j + 1].height:
                    arr[j].height, arr[j + 1].height = arr[j + 1].height, arr[j].height
            pygame.draw.rect(screen, black, pygame.Rect(arr[j].area[0], arr[j].area[1], 10, 240))  # clear line
            pygame.display.update()
            pygame.time.wait(500)
            x, y = arr[j].area[0], 240 - arr[j + 1].height
            pygame.draw.rect(screen, red, pygame.Rect(x, y, 10, arr[j + 1].height))  # draw new line


def background():
    j = 0
    pillar_list = []
    for i in range(0, 32):
        height = random.randint(1, 200)
        pillar_list.append(Pillar((0 + j, 240 - height, 10, height), red))  # [x, y, width, height]
        pygame.draw.rect(screen, pillar_list[i].color, pygame.Rect(pillar_list[i].area))
        j = j + 10
    pygame.display.update()
    pygame.time.wait(1500)
    Pillar.bubbleSort(pillar_list)


background()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    clock.tick(30)
