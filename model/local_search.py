from model.neighbors import feasible_neighbors
from model.testcases import Scenario
from model.yard import Yard
import random

def random_feasible_solution(yard_dim, arrival_order):
    N_bays, N_stacks = yard_dim
    yard = Yard(N_bays, N_stacks)

    def available_spots():
        for i, j in yard.locations():
            bay = yard[i]
            if bay.is_accessible(j) and bay.is_empty(j):
                yield i, j

    for container in arrival_order:
        spots = list(available_spots())
        i, j = random.choice(spots)
        yard[i][j] = container
    return yard
from cost_function import cost_function
def solve(scenario : Scenario):
    yard_dim =scenario.yard_dimensions
    containers = scenario.arrival_order
    solution = random_feasible_solution(scenario.yard_dimensions,containers)
    while True:
        Z_old = cost_function(solution)
        for neighbor in feasible_neighbors(containers,solution):
            Z_new = cost_function(neighbor)
            if Z_new < Z_old:
                solution = neighbor
                break
        else:
            return solution

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