from . import material as m

import math
import random as r


class MapGen:
    def __init__(self, num_tunnels, max_length, max_depth, max_diag, min_width, max_width):
        self.num_tunnels = num_tunnels
        self.max_length = max_length
        self.max_depth = max_depth
        self.max_diag = max_diag
        self.min_width = min_width
        self.max_width = max_width

    @staticmethod
    def _backtracking(last_dir, rand_dir):
        if -rand_dir[0] == last_dir[0] and -rand_dir[1] == last_dir[1]:
            return True
        else:
            return False

    def _get_length(self, rand_dir):
        if rand_dir[0] != 0 and rand_dir[1] != 0:
            return math.ceil(r.random() * self.max_diag), False
        elif rand_dir[0] != 0 and rand_dir[1] == 0:
            return math.ceil(r.random() * self.max_depth), True
        else:
            return math.ceil(r.random() * self.max_length), False

    @staticmethod
    def _tunnel_width(rmap, cur_row, cur_col, vertical, width, prev_split, turn):
        split = prev_split + r.randint(-1, 1)
        split = math.floor(width / 2) if split > math.floor(width / 2) else split
        split = -math.floor(width / 2) if split < -math.floor(width / 2) else split

        if turn:
            for row in range(math.ceil(width / 2)):
                rmap.grid[(cur_row + split) % rmap.y][(cur_col - row) % rmap.x] = m.Material('None', 'white', 1)
                rmap.grid[(cur_row + split) % rmap.y][(cur_col + row) % rmap.x] = m.Material('None', 'white', 1)
                for col in range(row):
                    rmap.grid[(cur_row - math.floor(width / 2 - row) + split) % rmap.y] \
                        [(cur_col + col) % rmap.x] = m.Material('None', 'white', 1)
                    rmap.grid[(cur_row - math.floor(width / 2 - row) + split) % rmap.y] \
                        [(cur_col - col) % rmap.x] = m.Material('None', 'white', 1)
                    rmap.grid[(cur_row + math.floor(width / 2 - row) + split) % rmap.y] \
                        [(cur_col + col) % rmap.x] = m.Material('None', 'white', 1)
                    rmap.grid[(cur_row + math.floor(width / 2 - row) + split) % rmap.y] \
                        [(cur_col - col) % rmap.x] = m.Material('None', 'white', 1)
        if vertical:
            for index in range(math.ceil(width / 2)):
                rmap.grid[cur_row][(cur_col - index + split) % rmap.x] = m.Material('None', 'white', 1)
                rmap.grid[cur_row][(cur_col + index + split) % rmap.x] = m.Material('None', 'white', 1)
        else:
            for index in range(math.ceil(width / 2)):
                rmap.grid[(cur_row - index + split) % rmap.y][cur_col] = m.Material('None', 'white', 1)
                rmap.grid[(cur_row + index + split) % rmap.y][cur_col] = m.Material('None', 'white', 1)
        return split

    def _adjust_width(self, width):
        width += r.randint(-1, 1)
        width = width if width <= self.max_width else self.max_width
        width = width if width >= self.min_width else self.min_width

    def generate(self, rmap):
        # Starting row and column
        cur_row = math.floor(r.random() * rmap.x)
        cur_col = math.floor(r.random() * rmap.y)
        # Possible directions
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        last_dir = [0, 0]
        # Random width for tunnel
        width = r.randint(self.min_width, self.max_width)
        # Allows for asymmetric width around center of tunnel
        prev_split = r.randint(-math.floor(width / 2), math.floor(width / 2))

        # Create the max number of tunnels
        for tunnels in range(self.num_tunnels):
            rand_dir = dirs[r.randint(0, len(dirs) - 1)]
            # Make sure we are going in a different direction than last iteration
            while self._backtracking(last_dir, rand_dir):
                rand_dir = dirs[r.randint(0, len(dirs) - 1)]
            tun_len, vertical = self._get_length(rand_dir)
            for pixel in range(tun_len):
                # Take a step and account for wrapping
                cur_row = (cur_row + rand_dir[0]) % rmap.x
                cur_col = (cur_col + rand_dir[1]) % rmap.y
                # Set the middle pixel
                rmap.grid[cur_row][cur_col] = m.Material('None', 'white', 1)
                # Set bordering pixels to correct width
                if pixel == 0:
                    # Round out edges before a turn
                    prev_split = self._tunnel_width(rmap, cur_row, cur_col, vertical, width, prev_split, True)
                else:
                    prev_split = self._tunnel_width(rmap, cur_row, cur_col, vertical, width, prev_split, False)
                # Add minute variability to width
                self._adjust_width(width)
            # Update last direction
            last_dir = rand_dir
