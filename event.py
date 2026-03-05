from dataclasses import dataclass
from enum import Enum

from yard import Container

class EventType(Enum):
    ARRIVAL=0
    DEPARTURE=1
@dataclass
class Event:
    subject: Container
    type : EventType


