import math
import random

from model.cost_function import cost_function
from model.local_search import random_feasible_solution
from model.neighbors import random_feasible_neighbor
from model.yard import Yard
from testcases import Scenario
import itertools





#simulated annealing
def solve(scenario : Scenario, seed=None,n_iter = 100, cooling_factor = 10):
    arrival_order = scenario.arrival_order
    yard_dim = scenario.yard_dimensions

    random.seed(seed)

    def accept(Z_old, Z_new, temp):
        p = math.exp(-abs(Z_old - Z_new) / temp)
        return random.random() < p or Z_new < Z_old

    # initialize with a random solution
    solution = random_feasible_solution(yard_dim, arrival_order)
    # print('initial solution:')
    # print(solution)

    #initialize the temperature to a reasonable value
    initial_temperature = 1 + cost_function(solution) * 1.0

    best = solution
    Z_best = cost_function(best)

    for i in range(n_iter):
        temperature = initial_temperature * (1/cooling_factor)**(i/n_iter)
        while True:
            neighbor = random_feasible_neighbor(arrival_order,solution)
            Z_old = cost_function(solution)
            Z_new = cost_function(neighbor)
            if accept(Z_old,Z_new,temperature):
                solution = neighbor
                # print(f'new solution (score = {Z_new}):')
                # print(solution)
                if Z_new < Z_best:
                    Z_best = Z_new
                    best = solution
                    if Z_best == 0:
                        return best
                break
    return best



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