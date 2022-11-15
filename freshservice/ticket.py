from __future__ import annotations
from enum import Enum
from models.ticket_model import TicketModel
from models.exceptions import IllegalException
from models.task import Task

class Ticket(TicketModel):

    class Status(Enum):
        OPEN = 2
        PENDING = 3
        RESOLVED = 4
        CLOSED = 5
        
    def __init_subclass__(cls):
        if Ticket.__init__ is not cls.__init__:
            raise IllegalException(f'You are not allowed to override {cls}.__init__')
    
    def create() -> Ticket: 
        # TODO(Implement)
        pass

    def close() -> None: 
        # TODO(Implement)
        pass
    
    def get() -> Ticket: 
        # TODO(Implement)
        pass
    
    def get_all() -> list[Ticket]: 
        # TODO(Implement)
        pass
    
    def filter() -> list[Ticket]: 
        # TODO(Implement)
        pass
    
    def update() -> Ticket: 
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