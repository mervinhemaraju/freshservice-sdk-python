from abc import ABC, abstractmethod
from enum import Enum
from __future__ import annotations
from models.task import Task

class TicketModel(ABC):

    class Priority(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        URGENT = 4

    def __init__(
        self,
        id,
        requester_id,
        responder_id,
        description,
        description_text,
        group_id,
        department_id,
        priority,
        status,
        impact,
        custom_fields,
        subject,
        created_at,
        updated_at,
        category,
        sub_category,
        item_category,
    ):
        # TODO(Implement)
        return

    @abstractmethod
    def create() -> TicketModel: pass

    @abstractmethod
    def close() -> None: pass
    
    @abstractmethod
    def get() -> TicketModel: pass

    @abstractmethod
    def get_all() -> list[TicketModel]: pass
    
    @abstractmethod
    def filter() -> list[TicketModel]: pass

    @abstractmethod
    def update() -> TicketModel: pass

    @abstractmethod
    def create_task() -> Task: pass

    @abstractmethod
    def get_tasks() -> list[Task]: pass

    @abstractmethod
    def get_task() -> Task: pass
    