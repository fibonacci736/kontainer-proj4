import random

from feasible import feasible
from model.yard import Yard


#swap the containers between two coordinates of the yard
def swap(yard,p1, p2):
    x, y = p1
    x2, y2 = p2
    temp = yard[x][y]
    yard[x][y] = yard[x2][y2]
    yard[x2][y2] = temp

def feasible_neighbors(problem: list[int], solution: Yard):
    N = solution.N_bays
    M = solution[0].N_stacks
    original_solution = solution.copy()

    locs = list(solution.locations())
    for i in range(len(locs)):
        for j in range(i):
            l1, l2 = locs[i], locs[j]
            swap(solution,l1, l2)
            if solution != original_solution and feasible(problem, solution):
                yield solution.copy()
            swap(solution,l1, l2)  # restore original

def random_feasible_neighbor(problem,solution):
    solution = solution.copy()
    locs = list(solution.locations())
    N = len(locs)
    while True:
        i,j = random.sample(list(range(N)),2)
        swap(solution,locs[i],locs[j])
        if feasible(problem,solution):
            return solution
        swap(solution,locs[i],locs[j])
