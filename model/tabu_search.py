import random

from local_search import random_feasible_solution
from cost_function import cost_function
import neighbors
from model.feasible import feasible
from model.testcases import Scenario
from yard import Yard


class TabuSearch:
    def __init__(self,max_tabu,scenario : Scenario):
        self.n_steps = 0
        self.n_tabu = max_tabu
        self.tabu = []
        self.container_order = scenario.arrival_order
        self.solution = random_feasible_solution(scenario.yard_dimensions,scenario.arrival_order)
        self.Z = cost_function(self.solution)
        self.best = self.solution.copy()
        self.bestZ = self.Z
        self.worsening_moves = 0
        self.stuck = False
    def is_tabu(self,p1,p2):
        return p1 in self.tabu and p2 in self.tabu
    def move(self,p1,p2, Z_new):
        neighbors.swap(self.solution,p1,p2)

        self.tabu.extend((p1,p2))
        while len(self.tabu) > self.n_tabu:
            self.tabu.pop(0)

        if Z_new >= self.Z:
            self.worsening_moves += 1

        if Z_new < self.bestZ:
            self.bestZ = Z_new
            self.best = self.solution.copy()
        self.Z = Z_new

    def feasible_swaps(self):
        for p1 in self.solution.locations():
            for p2 in self.solution.locations():
                neighbors.swap(self.solution,p1,p2)
                Z_new = cost_function(self.solution)
                is_feasible = feasible(self.container_order,self.solution)
                neighbors.swap(self.solution, p1, p2)
                if is_feasible:
                    yield Z_new,p1,p2
    def step(self):
        self.n_steps += 1
        swaps = sorted(list(self.feasible_swaps()))
        for Z_new,p1,p2 in swaps:
            if Z_new < self.bestZ or not self.is_tabu(p1,p2):
                self.move(p1, p2, Z_new)
                break
        else:
            self.stuck = True

def solve(scenario):
    search = TabuSearch(4, scenario)
    while (not search.stuck
           and search.worsening_moves < 10
           and search.n_steps < 100):
        search.step()
    return search.best

import testcases
if __name__ == '__main__':
    for scenario in testcases.small_scenarios:
        print('problem:')
        print(scenario.yard_dimensions)
        print(scenario.arrival_order)
        print('solution:')
        s =  solve(scenario)
        print(s)
        print(f'cost = {cost_function(s)}')

