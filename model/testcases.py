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
random.seed(12345)
small_scenarios = [
    random_scenario((1,3),3,3),
    random_scenario((1,9),9,2),
    random_scenario((1,9),9,9),
    random_scenario((2,3),6,2),
    random_scenario((2,3),6,6),
    random_scenario((2,4),8,2),
                   ]