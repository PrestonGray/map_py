import math
import random as r


class Diffuser:
    def __init__(self, num_centers, max_radius):
        self.max_radius = max_radius
        self.num_centers = num_centers
        self.centers = set()

    def _get_radius(self, rarity, constant):
        return math.ceil(self.max_radius * rarity) + constant

    @staticmethod
    def _check_color(color):
        return color != 'white' and color != 'brown'

    @staticmethod
    def _conditions(random, color):
        return random <= 0.1 and color != 'white'

    @staticmethod
    def _get_index(index, modifier, bound):
        return (index + modifier) % bound

    def generate(self, rmap):
        self.centers = r.sample(rmap.centers, self.num_centers)
        for center in self.centers:
            row, col = center[0], center[1]
            color = rmap.grid[row][col].color
            radius = self._get_radius(rmap.grid[row][col].rarity, 5)
            if self._check_color(color):
                for height in list(range(-radius, radius)):
                    for width in list(range(-height, height)):
                        row1 = self._get_index(row, -radius + height, rmap.y)
                        row2 = self._get_index(row, radius - height, rmap.y)
                        column = self._get_index(col, width, rmap.x)
                        color1 = rmap.grid[row1][column].color
                        color2 = rmap.grid[row2][column].color
                        if self._conditions(r.random(), color1):
                            rmap.grid[row1][column] = rmap.grid[row][col]
                        if self._conditions(r.random(), color2):
                            rmap.grid[row2][column] = rmap.grid[row][col]
