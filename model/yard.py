from copy import deepcopy
from dataclasses import dataclass

from .graph_things import DFSearch

@dataclass
class Container:
    pass
class ContainerYard:
    EXTERNAL = (-1, -1)
    def __init__(self, N=6, M=5, H=1):
        self.dim = (N, M, H)
        self.grid = [[[] for j in range(M)] for i in range(N)]
        self.connectedness = DFSearch(self._neighbors)
        self._update_reachable()

    def valid_coords(self, i, j):
        coords = i, j
        hdim = self.dim[:-1]  # ignore the vertical direction
        return all(0 <= c < cmax for c, cmax in zip(coords, hdim))

    def stack_height(self, i, j):
        return len(self.grid[i][j])

    def put(self, container, i, j):
        assert (self.can_put(i, j))
        self.grid[i][j].append(container)
        self._update_reachable()

    def pop(self, i, j) -> Container:
        assert (self.can_pop(i, j))
        res = self.grid[i][j].pop()
        self._update_reachable()
        return res

    def _can_lift(self, i, j):
        return self.reachable(i - 1, j) or self.reachable(i + 1, j)

    def can_put(self, i, j):
        return self.stack_height(i, j) < self.dim[2] and self._can_lift(i, j)

    def can_pop(self, i, j):
        return not self.is_empty(i, j) and self._can_lift(i, j)

    def is_empty(self, i, j):
        return self.stack_height(i, j) == 0

    def _neighbors(self, c):
        i, j = c
        adjacent = []
        for direction in [0, 1]:
            for delta in [-1, 1]:
                p = [i, j]
                p[direction] += delta
                adjacent.append(tuple(p))
        return [p for p in adjacent
                if self.valid_coords(*p) and
                self.is_empty(*p)
                ]

    def _update_reachable(self):
        self.connectedness.reset()

        N, M, _ = self.dim
        boundary = [(0, j) for j in range(M)] + \
                   [(N - 1, j) for j in range(M)] + \
                   [(i, 0) for i in range(N)] + \
                   [(i, M - 1) for i in range(M)]
        for p in boundary:
            if self.is_empty(*p):
                self.connectedness.explore(p)

    def reachable(self, i, j):
        return self.connectedness.reachable((i, j))

    def __str__(self):
        out = ""
        for row in self.grid:
            out += '|'
            for stack in row:
                out += '==|' if stack else '  |'
            out += '\n'
        return out

    def copy(self):
        new = ContainerYard(*self.dim)
        new.grid = deepcopy(self.grid)

