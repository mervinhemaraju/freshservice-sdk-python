from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from freshservice.models.auth import Auth
from freshservice.models.task import Task

class TicketModel(ABC):
    
    class Priority(Enum):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        URGENT = 4

    def __init__(
        self,
        auth: Auth,
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
        
        # * Create an auth object
        self.auth = auth

        # * Assign ticket attributes
        self.id = id
        self.requester_id = requester_id
        self.responder_id = responder_id
        self.description = description
        self.description_text = description_text
        self.group_id = group_id
        self.department_id = department_id
        self.priority = priority
        self.status = status
        self.impact = impact
        self.custom_fields = custom_fields
        self.subject = subject
        self.created_at = created_at
        self.updated_at = updated_at
        self.category = category
        self.sub_category = sub_category
        self.item_category = item_category

    @abstractmethod
    def create() -> TicketModel: pass

    @abstractmethod
    def close() -> None: pass

    @abstractmethod
    def update() -> dict: pass

    @abstractmethod
    def get_tasks() -> list[Task]: pass

    @abstractmethod
    def add_note() -> bool: pass
    