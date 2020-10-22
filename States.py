

class State:

    def __init__(self, m, x, y):
        self.map = m
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def successors(self):
        successors = []
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in neighbours:
            x = self.x + i[0]
            y = self.y + i[1]
            if self.valid(x, y):
                successors.append(State(self.map, x, y))
        return successors

    def valid(self, x, y):
        valid = 0 <= y < self.map.h and 0 <= x < self.map.w  # Check x,y doesnt get out the grid
        if valid:
            return valid and self.map.map[x][y] != 1  # Check x,y is not a wall
        else:
            return False

    def __str__(self):
        return f'({self.x}, {self.y})'
