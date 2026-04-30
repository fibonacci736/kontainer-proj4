import random

from model import Scenario,Container,ContainerYard,EventType,Event

def get_basic_scenario():
    yard = ContainerYard(4,4)
    K = 10
    containers = [Container() for i in range(K)]

    arrivals = [Event(containers[i],EventType.ARRIVAL) for i in range(K)]
    random.shuffle(containers)
    departures = [Event(containers[i],EventType.DEPARTURE) for i in range(K)]

    return Scenario(arrivals + departures, yard)

