from __future__ import annotations
from enum import Enum

class Task:

    class STATUS(Enum):
        OPEN = 1
        IN_PROGRESS = 2
        COMPLETED = 3

    def __init__(
        self,
        url,
        id,
        agent_id,
        status,
        due_date,
        title,
        description,
        created_at,
        updated_at,
        closed_at,
        group_id
    ):
        self.url = url
        self.id = id
        self.agent_id = agent_id
        self.status = status
        self.due_date = due_date
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.closed_at = closed_at
        self.group_id = group_id

    
    @staticmethod
    def create() -> Task:
        # TODO(Implement)
        pass

    def update() -> Task:
        # TODO(Implement)
        pass

    def close() -> None: 
        # TODO(Implement)
        pass

    def delete() -> bool: 
        # TODO(Implement)
        pass