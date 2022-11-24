from __future__ import annotations
from enum import Enum
from freshservice.models.ticket_model import TicketModel
from freshservice.models.task import Task

class Change(TicketModel):

    class Impact(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    class Status(Enum):
        OPEN = 1
        PLANNING = 2
        APPROVAL = 3
        PENDING_RELEASE = 4
        PENDING_REVIEW = 5
        CLOSED = 6

    class Type(Enum):
        MINOR = 1
        STANDARD = 2
        MAJOR = 3
        EMERGENCY = 4

    class Risk(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        VERY_HIGH = 4
    
    @staticmethod
    def create() -> Change: 
        # TODO(Implement)
        pass

    def close() -> None: 
        # TODO(Implement)
        pass
    
    def update() -> dict: 
        # TODO(Implement)
        pass
    
    def get_tasks() -> list[Task]: 
        # TODO(Implement)
        pass

    def add_note() -> bool: 
        # TODO(Implement)
        pass