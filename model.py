from dataclasses import dataclass
from enum import Enum

from event import Event,EventType
from yard import ContainerYard, Container

@dataclass
class Scenario:
    events: list[Event]
    yard: ContainerYard

@dataclass
class MoveAction:
    source : (int, int)
    target : (int, int)

class Agent:
    def start(self,yard,events):
        self.yard = yard
        self.events = events

    def notify(self,event: Event):
        pass
    def actions(self) -> list[MoveAction]:
        return []

class CoroAgent(Agent):
    def coroutine(self):
        pass
    def notify(self,event: Event):
        pass
    def actions(self) -> list[MoveAction]:
        pass


class Model:
    EXTERNAL = (-1,-1)

    def __init__(self,scenario,agent : Agent):
        self.scenario = scenario
        self.agent = agent
        self.yard : ContainerYard = None

    def run(self):
        time = 0
        self.yard : ContainerYard = self.scenario.yard.copy()
        events = self.scenario.events
        self.agent.start(self.yard,events)
        for event in events:
            self.process_event(event)

    def process_event(self,event:Event):
        self.agent.notify(event)
        done = False

        for move in self.agent.actions():
            if move.source == Model.EXTERNAL:
                assert event.type == EventType.ARRIVAL,'there is no new container to be placed'
                self.yard.put(event.subject, *move.target)
                done = True
            elif move.target == Model.EXTERNAL:
                assert event.type == EventType.DEPARTURE, 'container shouldnt leave'
                leaving_container = self.yard.pop(*move.source)
                assert leaving_container == event.subject
                done = True
            else:
                moving_container = self.yard.pop(*move.source)
                self.yard.put(moving_container,*move.target)

        assert done, "failed to place or remove container"








if __name__ == '__main__':
    scenario = Scenario()
