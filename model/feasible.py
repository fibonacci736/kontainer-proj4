

def feasible(problem : list[int],solution:list[list[int]]):

    N = len(solution)
    M = len(solution[0])
    def locations():
        for i in range(N):
            for j in range(M):
                yield (i,j)

    def find(container,yard):
        for i,j in locations():
            if yard[i][j] == container:
                yield i,j

    def can_place(location,yard):
        i,j = location
        if yard[i][j] != 0:
            return False
        if j == 0 or j == M-1:
            return True
        #check that it is next to the previous container
        return bool(yard[i][j-1]) + bool(yard[i][j+1]) == 1


    yard = [[0 for j in range(M)] for i in range(N)]
    p_index = 0
    lookup = {}
    def solve():
        nonlocal p_index

        key = tuple(tuple(yard[i]) for i in range(N))
        if key in lookup:
            return lookup[key]

        if p_index == len(problem):
            lookup[key] = True
            return True

        container = problem[p_index]
        potential_locations = [loc for loc in locations()
                               if ( can_place(loc,yard) or sum(yard[loc[0]])==0 )
                               and solution[loc[0]][loc[1]] == container
                               ]
        for loc in potential_locations:
            i,j = loc


            yard[i][j] = container
            p_index += 1
            cando = solve()
            yard[i][j] = 0
            p_index -= 1

            if cando:
                lookup[key] = True
                return True
        lookup[key] = False
        return False
    return solve()

if __name__ == '__main__':
    problem = [1,1,2,2,1,1]
    solution = [[1,2,1],
                [1,2,1]]
    print(feasible(problem,solution))

