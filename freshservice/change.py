from __future__ import annotations
from enum import Enum
from models.ticket_model import TicketModel
from models.exceptions import IllegalException
from models.task import Task

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

    def __init_subclass__(cls):
        if Change.__init__ is not cls.__init__:
            raise IllegalException(f'You are not allowed to override {cls}.__init__')
    
    def create() -> Change: 
        # TODO(Implement)
        pass

    def close() -> None: 
        # TODO(Implement)
        pass
    
    def get() -> Change: 
        # TODO(Implement)
        pass
    
    def get_all() -> list[Change]: 
        # TODO(Implement)
        pass
    
    def filter() -> list[Change]: 
        # TODO(Implement)
        pass
    
    def update() -> Change: 
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