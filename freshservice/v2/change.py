from __future__ import annotations
from enum import Enum
from datetime import datetime
from freshservice.v2.models.ticket_model import TicketModel
from freshservice.v2.models.task import Task
from freshservice.v2.models.auth import Auth
from freshservice.v2.models.exceptions import FreshserviceResourceNotFound, FreshserviceTicketException

# TODO("Add compatibility to assets")
class Change(TicketModel):

    URL_PREFIX = "changes/{}"

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
      
    def __init__(self, id):

        # * Create the url
        self.url = self.URL_PREFIX.format(id)

        # * Try to get the ticket schema
        try:
            # * Create an auth object
            auth = Auth()

            # * Retrieve the ticket details
            schema = (auth.getx(url=self.url))['change']

        except FreshserviceResourceNotFound:
            raise FreshserviceResourceNotFound(f"The change {id} cannot be found.")
        except Exception as e:
            raise FreshserviceTicketException(f"Error occurred while getting change {id}: {e}")

        # * Unique class attributes
        self.risk = schema['risk']
        self.change_type = schema['change_type']
        self.approval_status = schema.get('approval_status', None)
        self.planned_start_date = schema.get('planned_start_date', None)
        self.planned_end_date = schema.get('planned_end_date', None)
        self.maintenance_window = schema.get('maintenance_window', None)
        self.blackout_window = schema.get('blackout_window', None)


        # * Pass values to the parent class
        super().__init__(
            auth=auth,
            id=schema['id'],
            requester_id=schema['requester_id'],
            responder_id=schema['responder_id'],
            description=schema['description'],
            description_text=schema['description_text'],
            group_id=schema['group_id'],
            department_id=schema['department_id'],
            priority=schema['priority'],
            status=schema['status'],
            impact=schema['impact'],
            custom_fields=schema['custom_fields'],
            subject=schema['subject'],
            created_at=schema['created_at'],
            updated_at=schema['updated_at'],
            category=schema['category'],
            sub_category=schema['sub_category'],
            item_category=schema['item_category']
        )

    @staticmethod
    def create(
        requester_email: str,
        subject: str,
        description: str,
        department_id, 
        group_id, 
        category,
        sub_category,
        item_category,
        custom_fields,
        planned_start_date: datetime,
        planned_end_date: datetime,
        priority: TicketModel.Priority = TicketModel.Priority.LOW,
        planning_fields = {}
    ) -> Change: 

        # * Set the URL prefix
        url_prefix = "/changes"

        # * Create an auth object
        auth = Auth()

        # * Get the requester id
        requesters = auth.getx(
            url=f"requesters?query=primary_email:'{requester_email}'"
        )['requesters']

        # * If no requesters are obtained, filter from agents
        if len(requesters) == 0:
            requesters = auth.getx(
                url=f"agents?query=email:'{requester_email}'"
            )['agents']
        
        print(requesters)

        # * Create the data object
        data = {
            "requester_id": requesters[0]['id'],
            "subject": subject,
            "description": description,
            "status": Change.Status.OPEN,
            "priority": priority.value,
            "department_id": department_id,
            "group_id": group_id,
            "category": category,
            "sub_category": sub_category,
            "item_category": item_category,
            "custom_fields": custom_fields,
            "priority": priority.value,
            "planned_start_date": planned_start_date,
            "planned_end_date": planned_end_date,
            "planning_fields": planning_fields 
        }

        # * Make the api call
        response = auth.postx(
            url=url_prefix,
            data=data
        )

        # * Return the ticket object
        return Change(id=response['change']['id'])

    def asdict(self) -> dict:

        # * Convert class attributes to dict
        the_dict = dict(vars(self))

        # * Remove unnecessary attributes
        the_dict.pop('id')
        the_dict.pop('url')
        the_dict.pop('created_at')
        the_dict.pop('updated_at')
        the_dict.pop('description_text')
        the_dict.pop('auth')

        # * Return the dict
        return the_dict
    
    def close(self) -> dict: 

        # * Create the dict attributes
        dict_attr = self.asdict()

        # * Change the status of the ticket to close
        dict_attr['status'] = self.Status.CLOSED.value

        # * Update the ticket
        return self.auth.putx(
            url = self.url,
            data=dict_attr
        )
    
    def update(self) -> dict: 

        # * Update the ticket
        return self.auth.putx(
            url = self.url,
            data=self.asdict()
        )
    
    def get_tasks(self) -> list[Task]: 
        
        # FIXME(All tasks need to be closed before closing a change)
        # * Create an extended url
        extended_url_prefix = self.url + "/tasks"

        # * Get all the tasks
        response =  self.auth.getx(
            url = extended_url_prefix
        )

        # * Return the tasks
        return [
            Task(
                url = extended_url_prefix,
                id=task['id'],
                agent_id=task["agent_id"],
                status=task['status'],
                due_date=task["due_date"],
                title=task["title"],
                description=task["description"],
                created_at=task["created_at"],
                updated_at=task["updated_at"],
                closed_at=task["closed_at"],
                group_id=task["group_id"]
            )
            for task in response['tasks']
        ]

    def add_note(self, note: str, is_private: bool) -> bool: 
        
        # * Create an extended url
        extended_url_prefix = self.url + "/notes"

        # * Create a data block
        data = { 
            "body": note, 
            "private": is_private 
        }

        # * Add the note to the ticket
        return self.auth.postx(
            url = extended_url_prefix,
            data=data
        )