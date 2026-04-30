from model.yard import Yard


def feasible(problem: list[int], solution: Yard):
    N_bays = solution.N_bays
    N_stacks = solution[0].N_stacks

    def find(container, yard):
        for i, j in yard.locations():
            if yard[i][j] == container:
                yield i, j

    def can_place(location, yard: Yard):
        i, j = location
        return yard[i].is_accessible(j) and yard[i].is_empty(j)

    current_yard = Yard(N_bays, N_stacks)
    p_index = 0
    lookup = {}

    def solve():
        nonlocal p_index

        key = hash(current_yard)
        if key in lookup:
            return lookup[key]

        if p_index == len(problem):
            lookup[key] = True
            return True

        container = problem[p_index]
        potential_locations = [loc for loc in current_yard.locations()
                               if (can_place(loc, current_yard) or sum(current_yard[loc[0]]) == 0)
                               and solution[loc[0]][loc[1]] == container
                               ]
        for loc in potential_locations:
            i, j = loc

            current_yard[i][j] = container
            p_index += 1
            cando = solve()
            current_yard[i][j] = 0
            p_index -= 1

            if cando:
                lookup[key] = True
                return True
        lookup[key] = False
        return False

    return solve()


if __name__ == '__main__':
    problem = [1, 1, 2, 2, 1, 1]
    solution = [[1, 2, 1],
                [1, 2, 1]]
    print(feasible(problem, solution))
