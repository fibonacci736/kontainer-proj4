import re
def parse_scenario(description_file):
    dim,order = description_file.readline().strip().split(';')
    N,M = map(int, dim[1:-1].split(',') )
    arrival_order = list(map(int,order[1:-1].split(',')))

def parse_solution(file):
    yard = []
    while line := file.readline().strip():
        bay = list(map(int,line.split(',')))
        yard.append(bay)

    return yard

