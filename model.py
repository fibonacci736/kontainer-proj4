from dataclasses import dataclass

from event import Event,EventType
from yard import ContainerYard, Container

@dataclass
class Scenario:
    events: list[Event]
    yard: ContainerYard

class Agent:
    def prepare_scenario(self,yard,events):
        self.yard = yard
        self.events = events

    def decide_where_to_put(self,container):
        pass

class Model:
    def run(self,scenario : Scenario, agent):
        time = 0
        yard = scenario.yard.copy()
        for event in scenario.events:
            if event.type == EventType.ARRIVAL:
                agent.



if __name__ == '__main__':
    yard = ContainerYard()
    for i in range(3):
        yard.put(Container(), i, 0)
    print(yard)
    for i in range(5):
        print(yard.can_pop(i, 0), yard.can_put(i, 0))
    for i in range(2, -1, -1):
        yard.pop(i, 0)
    print(yard)
