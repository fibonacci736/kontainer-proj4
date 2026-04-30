import random

import model
from model import Event, MoveAction, ContainerYard, EventType
from model.model import StateDescription

def move(yard,a,b) -> MoveAction:
    yard.put(yard.pop(a),b)
    return MoveAction(a,b)

def make_reachable(location, yard: ContainerYard) -> list[MoveAction]:
    actions = []
    i,j = location
    while not yard.reachable(*location):
        for k in range(yard.dim[0],i,-1):
            lremove = k,j
            if yard.is_empty(*lremove):
                continue
            empty = random.choice(list(put_locations(yard)))

            actions.append( move(yard,lremove,empty) )
            break
    return actions



def put_locations(yard: ContainerYard):
    for i, j in yard.coords():
        if yard.can_put(i, j) and yard.reachable(i, j):
            yield i, j


def retrieveContainer(container, yard: ContainerYard) -> list[MoveAction]:
    *location, _ = yard.find(container)
    actions = make_reachable(location, yard)
    return actions + [MoveAction((location), ContainerYard.EXTERNAL)]


class BasicAgent(model.Agent):

    def step(self, event: Event, observation: StateDescription) -> list[MoveAction]:
        if event.type == EventType.DEPARTURE:
            return retrieveContainer(event.subject, observation.yard)
        if event.type == EventType.ARRIVAL:
            location = random.choice(list(put_locations(observation.yard)))
            print( observation.yard.can_put(*location))
            return [MoveAction(ContainerYard.EXTERNAL, location)]
