import pygame
# from States import State
from breath import breadth_search
from Search import *
import MapGeneration as mg

pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))
bg = 25, 25, 25
screen.fill(bg)

map = mg.Map(width, height, screen)

map.draw_grid()  # Generate the grid
times = 1
while True:
    pygame.event.get()
    map.mouse()

    while times:
        origin = State(map, 25, 25)
        pathAux = search(
            solution=Solution(map, 25, 15),
            origin=origin,
            algorithm=breadth_search,
            map=map
        )
        times = times - 1

    pygame.display.flip()

