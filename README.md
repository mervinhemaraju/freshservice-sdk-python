# freshservice-sdk-python

This sdk is an unofficial freshservice API v2 SDK written in Python.

The library is based on the official Freshservice api found [here](https://api.freshservice.com/)

It currently supports the manipulation of resources listed below:

* Tickets
* Changes
* Problems
* Tasks (tickets, changes and problems)
* Many more to come!

## Getting Started

To install the SDK in your project:

```
pip install freshservice-sdk-python
```

You'll also need

* A Freshservice domain name, `your_company.freshservice.com`
* An [API key](https://support.freshservice.com/en/support/solutions/articles/50000000306-where-do-i-find-my-api-key-)

You will need to pre set these two values in your deployment's environment variables before using the library. You can either set it in a bash script or pre code it so that you have it in your environment variable on runtime:

```
os.environ['FRESHSERVICE_API_KEY'] = "XXXXXX"

os.environ['FRESHSERVICE_DOMAIN'] = "your_company.freshservice.com"
```

## Tickets

You can manipulate tickets using the `Ticket` model from the sdk. The `Ticket` model will handle [this](https://api.freshservice.com/#tickets) part of the api in freshservice.

You can import the model as shown below:

```
from freshservice.v2 import Ticket
```

### Creating a ticket

```
from freshservice.v2 import Ticket

ticket = Ticket.create(
	requester_email, 
        subject, 
        description, 
        status: Status, 
        priority: TicketModel.Priority, 
        department_id = None,
        group_id = None,
        category = None,
        sub_category = None,
        item_category = None,
        custom_fields: dict = {}
)
```

### Fetching a ticket

You can fetch a ticket by providing the ticket id when initializing the ticket object as shown below.

This will go and fetch the ticket details.

```
from freshservice.v2 import Ticket

ticket = Ticket(
	id=your_ticket_id
)

```

### Updating a ticket

To update a ticket, you can just update the ticket's attribute and then hit the `update()` on the ticket's object to update it.

```
from freshservice import Ticket

ticket.subject = "new subject"
ticket.description = "new description"
ticket.update()

```

### Closing a ticket

Closing a ticket works similarly to updating it. You can set all the required attributes of the ticket to match the ticket closure rules and then hit the `close()` function

```
from freshservice.v2 import Ticket

ticket.category = "Other"
ticket.close()
```

## Changes

```
Coming soon
```

## Problems

```
Coming soon
```

## Building the SDK

In most cases, you won't need to build the SDK from source. If you want to build it yourself, you'll need these preequisites:

* Clone the repo
* Run `python setup.py build` from the root of the project (assuming Python is installed)

## Contributing

We're happy to accept contributions and PRs!

[](https://pypi.org/project/freshservice-sdk-python/#modal-close "Close")###

|          |   |   |
| -------- | - | - |
| -------- |   |   |
|          |   |   |
| -        | - | - |
|          |   |   |
|          |   |   |

[](https://pypi.org/project/freshservice-sdk-python/#modal-close

This sdk is an unofficial freshservice API v2 SDK written in Python.

The library is based on the official Freshservice api found [here](https://api.freshservice.com/)

It currently supports the manipulation of resources listed below:

* Tickets
* Changes
* Problems
* Tasks (tickets, changes and problems)

```
Under construction
```
