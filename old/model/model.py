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


@dataclass
class StateDescription:
    yard: ContainerYard
    future: list[Event]


class Agent:
    def step(self, event: Event, observation: StateDescription) -> list[MoveAction]:
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
        print(self.yard)
        for t in range(len(events)):
            self.process_event(t)
            print(self.yard)

    def process_event(self, event_index: int):
        event = self.scenario.events[event_index]

        observation = StateDescription(self.yard.copy(),
                                       self.scenario.events[event_index + 1:])

        done = False
        for move in self.agent.step(event, observation):
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
<<<<<<< Updated upstream


if __name__ == '__main__':
    events = [Event(Container(), type=EventType.ARRIVAL) for i in range(10)]
    scenario = Scenario(events, ContainerYard())
    model = Model(scenario, agent=Agent())
=======
>>>>>>> Stashed changes
