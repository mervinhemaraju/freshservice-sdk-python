from enum import Enum
from __future__ import annotations

class Task:

    class STATUS(Enum):
        OPEN = 1
        IN_PROGRESS = 2
        COMPLETED = 3

    def __init__(
        self,
        ticket_id,
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