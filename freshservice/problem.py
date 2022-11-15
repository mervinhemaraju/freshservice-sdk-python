from __future__ import annotations
from enum import Enum
from models.ticket_model import TicketModel
from models.exceptions import IllegalException
from models.task import Task

class Problem(TicketModel):

    class Impact(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    class Status(Enum):
        OPEN = 1
        CHANGE_REQUESTED = 2
        CLOSED = 3

    def __init_subclass__(cls):
        if Problem.__init__ is not cls.__init__:
            raise IllegalException(f'You are not allowed to override {cls}.__init__')
    
    def create() -> Problem:
        # TODO(Implement)
        pass

    def close() -> None: 
        # TODO(Implement)
        pass
    
    def get() -> Problem:
        # TODO(Implement)
        pass
    
    def get_all() -> list[Problem]: 
        # TODO(Implement)
        pass
    
    def filter() -> list[Problem]: 
        # TODO(Implement)
        pass
    
    def update() -> Problem:
        # TODO(Implement)
        pass
    
    def create_task() -> Task: 
        # TODO(Implement)
        pass
    
    def get_tasks() -> list[Task]: 
        # TODO(Implement)
        pass
    
    def get_task() -> Task: 
        # TODO(Implement)
        pass