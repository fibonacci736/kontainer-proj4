from local_search import random_feasible_solution
import random

from model.cost_function import cost_function
from model.feasible import feasible
from model.yard import Yard
from neighbors import random_feasible_neighbor

class GA:
    def __init__(self,scenario,pop_size = 10):
        self.scenario = scenario
        self.population = [random_feasible_solution(scenario.yard_dimensions,scenario.arrival_order)
                           for i in range(pop_size)]

    def step(self,n_children=6):
        children = [c for i in range(n_children) if (c := self.breed())]
        self.population = self.natural_selection(self.population + children)

    @property
    def best(self):
        return min(self.population,key=cost_function)
    def breed(self):
        p1,p2 = self.select_parents()
        child = self.crossover(p1,p2)
        if feasible(self.scenario.arrival_order,child):
            self.mutate(child)
            return child
        else:
            return None

    def select_parents(self):
        return random.sample(self.population,k=2)

    def crossover(self, p1: Yard, p2:Yard):
        order =self.scenario.arrival_order
        child = Yard(*self.scenario.yard_dimensions)
        for container in order:
            locs = list(child.locations())
            random.shuffle(locs)
            for x,y in locs:
                if p1[x][y] == container or p2[x][y] == container and child[x].is_accessible(y):
                    child[x][y] = container
                    break
            else:
                for x,y in locs:
                    if child[x].is_accessible(y):
                        child[x][y] = container
                        break
        return child
    def mutate(self, child,rate=0.1):
        if random.random() < rate:
            child = random_feasible_neighbor(self.scenario.arrival_order,child)
        return child


    def natural_selection(self, candidates : list, n_best = 4):
        candidates.sort(key=cost_function)
        n_target = len(self.population)
        return candidates[:n_best] + random.sample(candidates[n_best:],k=n_target-n_best)


def solve(scenario):
    search = GA(scenario)
    for i in range(10):
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