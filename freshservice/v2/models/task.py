from __future__ import annotations
from enum import Enum
from freshservice.v2.models.auth import Auth

class Task:

    class Status(Enum):
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
        group_id,
        notify_before
    ):
        self.url = url + f"/{id}"
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
        self.notify_before = notify_before

    def asdict(self):

        # * Convert class attributes to dict
        the_dict = dict(vars(self))

        # * Remove unnecessary attributes
        the_dict.pop('id')
        the_dict.pop('created_at')
        the_dict.pop('updated_at')
        the_dict.pop('closed_at')
        the_dict.pop('url')

        # * Return the dict
        return the_dict
    
    @staticmethod
    def create(
        url,
        ticket_id,
        agent_id,
        title,
        description,
        group_id,
        notify_before = 0,
        status = Status.OPEN,
        due_date = None,
    ) -> Task:
        
        # * Create the URL
        url = url + f"/{ticket_id}/tasks"

        # * Create an auth object
        auth = Auth()

        # * Construct the data
        data = {
            "agent_id": agent_id,
            "title": title,
            "description": description,
            "group_id": group_id,
            "notify_before": notify_before,
            "status": status.value,
            "due_date": due_date
        }

        # * Make the api call
        return auth.postx(
            url=url,
            data=data
        )

    def update(self, auth: Auth) -> dict:
        
        # * Create the dict attributes
        dict_attr = self.asdict()

        # * Update the task
        return auth.putx(
            url = self.url,
            data=dict_attr
        )

    def close(self, auth: Auth) -> dict: 

        # * Create the dict attributes
        dict_attr = self.asdict()

        # * Change the status of the task to completed
        dict_attr['status'] = self.Status.COMPLETED.value

        # * Update the task
        return auth.putx(
            url = self.url,
            data=dict_attr
        )

    def delete(self, auth: Auth) -> dict: 

        # * Delete the task
        return auth.deletex(
            url = self.url
        )