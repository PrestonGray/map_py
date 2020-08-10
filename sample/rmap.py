from . import constants

import numpy as np
import random as r


class RMap:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = []
        self.centers = set()
        for row in range(y):
            temp = []
            for col in range(x):
                if r.random() < 0.01:
                    temp.append(np.random.choice(constants.materials, 1,
                                                 p=[mat.rarity for mat in constants.materials])[0])
                    self.centers.add((row, col))
                else:
                    temp.append(constants.materials[0])
            self.grid.append(temp)

    def get_colors(self):
        int_map = np.zeros((self.y, self.x), dtype=int)
        for row in range(self.y):
            for col in range(self.x):
                int_map[row][col] = constants.colors[self.grid[row][col].color]
        return int_map
