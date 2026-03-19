from dataclasses import dataclass

from .event import Event, EventType
from .yard import ContainerYard, Container



@dataclass
class Scenario:
    events: list[Event]
    yard: ContainerYard


@dataclass
class MoveAction:
    source: (int, int)
    target: (int, int)


class Agent:
    def start(self, yard, events):
        self.yard = yard
        self.events = events

    def step(self, event: Event) -> list[MoveAction]:
        raise NotImplementedError


class Model:

    def __init__(self, scenario, agent: Agent):
        self.scenario = scenario
        self.agent = agent
        self.yard: ContainerYard

    def run(self):
        self.yard: ContainerYard = self.scenario.yard.copy()
        events = self.scenario.events
        self.move_log = []

        self.agent.start(self.yard, events)
        for event in events:
            self.process_event(event)

    def process_event(self, event: Event):
        done = False

        for move in self.agent.step(event):
            self.move_log.append(move)
            if move.source == ContainerYard.EXTERNAL:
                assert event.type == EventType.ARRIVAL, 'there is no new container to be placed'
                self.yard.put(event.subject, *move.target)
                done = True
            elif move.target == ContainerYard.EXTERNAL:
                assert event.type == EventType.DEPARTURE, 'container shouldnt leave'
                leaving_container = self.yard.pop(*move.source)
                assert leaving_container == event.subject
                done = True
            else:
                moving_container = self.yard.pop(*move.source)
                self.yard.put(moving_container, *move.target)

        assert done, "failed to place or remove container"


if __name__ == '__main__':
    events = [Event(Container(), type=EventType.ARRIVAL) for i in range(10)]
    scenario = Scenario(events, ContainerYard())
    model = Model(scenario, agent=Agent())
