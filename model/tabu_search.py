import random

from local_search import random_feasible_solution
from cost_function import cost_function
import neighbors
from model.testcases import Scenario
from yard import Yard


class TabuSearch:
    def __init__(self,max_tabu,scenario : Scenario):
        self.n_tabu = max_tabu
        self.tabu = []
        self.container_order = scenario.arrival_order
        self.solution = random_feasible_solution(scenario.yard_dimensions,scenario.arrival_order)
        self.Z = cost_function(self.solution)
        self.best = self.solution.copy()
        self.bestZ = self.Z
    def is_tabu(self,p1,p2):
        return p1 in self.tabu or p2 in self.tabu
    def move(self,p1,p2):
        neighbors.swap(self.solution,p1,p2)
        self.tabu.extend((p1,p2))
        while len(self.tabu) > self.n_tabu:
            self.tabu.pop(0)
    def evaluate_swap(self,p1,p2):
        neighbors.swap(self.solution,p1,p2)
        Z_new = cost_function(self.solution)
        neighbors.swap(self.solution, p1, p2)
        return Z_new
    def step(self):
        p1,p2 = neighbors.random_feasible_swap(self.container_order,self.solution)
        Z_new = self.evaluate_swap(p1,p2)
        if Z_new < self.Z or not self.is_tabu(p1,p2):
            self.move(p1,p2)
            if Z_new < self.bestZ:
                self.bestZ = Z_new
                self.best = self.solution.copy()
            self.Z = Z_new

def solve(scenario):
    search = TabuSearch(5,scenario)
    for i in range(1000):
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

