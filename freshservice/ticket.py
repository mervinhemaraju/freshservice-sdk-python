from __future__ import annotations
from enum import Enum
from freshservice.models.exceptions import FreshserviceResourceNotFound, FreshserviceTicketException
from freshservice.models.ticket_model import TicketModel
from freshservice.models.task import Task
from freshservice.models.auth import Auth

class Ticket(TicketModel):

    URL_PREFIX = "tickets/{}"

    class Status(Enum):
        OPEN = 2
        PENDING = 3
        RESOLVED = 4
        CLOSED = 5
            
    def __init__(self, id):

        # * Try to get the ticket schema
        try:
            # * Create an auth object
            auth = Auth()

            # * Create the url
            url = self.URL_PREFIX.format(id)

            # * Retrieve the ticket details
            schema = (auth.getx(url=url))['ticket']

        except FreshserviceResourceNotFound:
            raise FreshserviceResourceNotFound(f"The ticket {id} cannot be found.")
        except Exception as e:
            raise FreshserviceTicketException(f"Error occurred while getting {id}: {e}")

        # * Unique class attributes
        self.attachments = schema.get('attachments', None)
        self.email = schema.get('email', None)
        self.name = schema.get('name', None)
        self.tags = schema.get('tags', None)
        self.type = schema.get('type', None)

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

    def asdict(self):

        # * Convert class attributes to dict
        the_dict = dict(vars(self))

        # * Remove unnecessary attributes
        the_dict.pop('id')
        the_dict.pop('created_at')
        the_dict.pop('updated_at')
        the_dict.pop('description_text')
        the_dict.pop('auth')
        the_dict.pop('attachments')

        # * Return the dict
        return the_dict

    @staticmethod
    def create() -> Ticket: 
        # TODO(Implement)
        pass

    def close(self) -> None: 

        # * Create the url
        url = self.URL_PREFIX.format(self.id)

        # * Create the dict attributes
        dict_attr = self.asdict()

        # * Change the status of the ticket to close
        dict_attr['status'] = self.Status.CLOSED.value

        # * Update the ticket
        return self.auth.putx(
            url = url,
            data=dict_attr
        )
         
    def update(self) -> dict: 

        # * Create the url
        url = self.URL_PREFIX.format(self.id)

        # * Update the ticket
        return self.auth.putx(
            url = url,
            data=self.asdict()
        )
    
    def create_task() -> Task: 
        # TODO(Implement)
        pass
    
    def get_tasks() -> list[Task]: 
        # TODO(Implement)
        pass
    
    def get_task() -> Task: 
        # TODO(Implement)
        pass

    def add_note() -> bool: 
        # TODO(Implement)
        pass