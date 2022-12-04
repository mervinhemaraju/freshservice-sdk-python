from __future__ import annotations
from enum import Enum
from freshservice.v2.models.ticket_model import TicketModel
from freshservice.v2.models.task import Task

class Problem(TicketModel):

    class Impact(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    class Status(Enum):
        OPEN = 1
        CHANGE_REQUESTED = 2
        CLOSED = 3
    
    @staticmethod
    def create() -> Problem:
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