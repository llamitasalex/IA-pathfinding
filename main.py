import pygame
from MapGeneration import Map
from States import State
from Search import *
from breath import breadth_search

pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))
bg = 25, 25, 25
screen.fill(bg)

map = Map()

map.draw_grid()  # Generate the grid
times = 1
while True:
    pygame.event.get()
    map.mouse()

    while times:
        origin = State(map, 25, 25)
        pathAux = search(
            solution=Solution(map, 25, 15),
            algorithm=breadth_search,
        )
        times = times - 1

    pygame.display.flip()

