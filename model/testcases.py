import random
from dataclasses import dataclass

from model.yard import Yard


@dataclass
class Scenario:
    yard_dimensions : tuple[int,int]
    arrival_order : list[int]

def random_scenario(yard_dim,N_containers,N_destinations):
    destinations = [i+1 for i in range(N_destinations)]
    containers = random.choices(destinations,k=N_containers)
    return Scenario(yard_dim,containers)
small_scenarios = [
    Scenario((1,9),[1,2,3,4,5,6,7,8,9]),
    Scenario((2,9),[1,2,3,4,5,6,7,8,9]),
    random_scenario((4,4),16,9)
]