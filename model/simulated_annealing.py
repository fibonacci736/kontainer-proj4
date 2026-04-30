import math
import random


def empty_yard(N_bays, N_stacks):
    return [[0 for j in range(N_stacks)] for i in range(N_bays)]
def random_feasible_solution(yard_dim, arrival_order):
    N_bays, N_stacks = yard_dim
    yard = empty_yard(N_bays,N_stacks)
    def get(i,j):
        try:
            return yard[i][j]
        except IndexError:
            return None
    def available_spots():
        for i in range(N_bays):
            is_empty_bay = not any(yard[i])
            for j in range(N_stacks):
                if yard[i][j]:
                    #already occupied
                    continue
                if is_empty_bay or get(i,j-1) == 0 or get(i,j+1) == 0:



def solve(yard_dim, arrival_order,seed=None):
    random.seed(seed)

    def accept(Z_old,Z_new, temp):
        p = math.exp(-abs(Z_old-Z_new)/temp)
        return random.random() < p or Z_new < Z_old

    #initialize with a random solution
    solution = random_feasible_solution(yard_dim, arrival_order)