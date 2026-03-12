from model import model
from model.event import Event
from model.model import MoveAction


class BeslisRegels(model.Agent):
    def step(self, event: Event) -> list[MoveAction]:
        pass


if __name__ == '__main__':
    model.Agent()
    #run some tests

