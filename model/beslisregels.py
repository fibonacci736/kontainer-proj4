import math

from model.cost_function import cost_function
from model.testcases import Scenario
from model.yard import Yard


#greedy algoritme: plaats de container op de plek die:
# 1. een container blokkeert die later vertrekt, maar zo kort mogelijk later
# 2. als dat niet kan, in een lege bay
# 3. als dat niet kan, naast een container met zo vergelijkbaar mogelijk vertrektijd


def get_available_places(yard: Yard):
    def get_neighbor(x, y):
        up_neighbor = yard[x][y-1] if y > 0 else 0
        down_neighbor = yard[x][y+1] if y+1 < len(yard[x]) else 0
        return up_neighbor if up_neighbor else down_neighbor
    for x,y in yard.locations():
        if yard[x].is_accessible(y) and yard[x].is_empty(y):
            yield (x,y), get_neighbor(x,y)

def place_container(yard, container):
    def order(param):
        _,neighbor = param
        diff = abs(neighbor-container)
        if neighbor == 0:
            return 0,0
        if neighbor >= container:
            return 1,-diff
        else:
            return -1,-diff
    best_place = max(get_available_places(yard),key=order)
    return best_place[0]


def solve(scenario : Scenario):
    containers = scenario.arrival_order
    yard = Yard(*scenario.yard_dimensions)
    for container in containers:
        x,y = place_container(yard,container)
        yard[x][y] = container
    return yard

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

