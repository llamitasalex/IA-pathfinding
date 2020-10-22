import pygame


class Map:
    blockSize = 20  # Set the size of the grid block
    strip = (230, 230, 230)
    colors = [[10, 10, 10], [90, 91, 92], [134, 239, 134], [0, 128, 0], [255, 0, 0]]
    #           floor:0        wall:1        checked:2       start:3        end:4
    map = []

    def __init__(self, width, height, screen):
        self.screen = screen
        self.w = width // self.blockSize
        self.h = height // self.blockSize
        self.map = [[0 for i in range(self.h)] for j in range(self.w)]

    def draw(self, x, y):
        rect = pygame.Rect(x * self.blockSize, y * self.blockSize,
                           self.blockSize, self.blockSize)
        pygame.draw.rect(self.screen, self.colors[self.map[x][y]], rect)
        pygame.draw.rect(self.screen, self.strip, rect, 1)
        # pygame.time.delay(500)
        pygame.display.update()

    def draw_grid(self):
        for x in range(self.w):
            for y in range(self.h):
                # pygame.time.delay(1000)
                rect = pygame.Rect(x * self.blockSize, y * self.blockSize,
                                   self.blockSize, self.blockSize)
                pygame.draw.rect(self.screen, self.colors[self.map[x][y]], rect)
                pygame.draw.rect(self.screen, self.strip, rect, 1)
                # pygame.display.update()

    def mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            x = mouse_pos[0] // self.blockSize
            y = mouse_pos[1] // self.blockSize
            self.map[x][y] = 1
            self.draw(x, y)
