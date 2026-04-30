from feasible import feasible
from model.yard import Yard


def feasible_neighbors(problem: list[int], solution: Yard):
    N = solution.N_bays
    M = solution[0].N_stacks

    def swap(p1, p2):
        x, y = p1
        x2, y2 = p2
        temp = solution[x][y]
        solution[x][y] = solution[x2][y2]
        solution[x2][y2] = temp

    def copy(s):
        return [list(row) for row in s]

    original_solution = copy(solution)

    locs = list(solution.locations())
    for i in range(len(locs)):
        for j in range(i):
            l1, l2 = locs[i], locs[j]
            swap(l1, l2)
            if solution != original_solution and feasible(problem, solution):
                yield copy(solution)
            swap(l1, l2)  # restore original


from testcases import tc1

if __name__ == '__main__':
    for n in feasible_neighbors(*tc1):
        print(n)
