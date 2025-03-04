from abc import ABC, abstractmethod
class Ticket:
    def __init__(self, ticket_id, ticket_type, ticket_price):
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price    

    @property
    def ticket_id(self):
        return self.__ticket_id
    
    @ticket_id.setter
    def ticket_id(self, value):
        if len(value) == 8 and value[:3].isalpha() and value[:3].isupper() and value[3:].isdigit():
            self.__ticket_id = value
        else:
            raise ValueError("Invalid ticket ID format")

    def __str__(self):
        return f"{self.ticket_id} - {self.ticket_type} - {self.ticket_price}"

    def valid(self):
        if len(self.__ticket_id) == 8 and self.__ticket_id[:3].isalpha() and self.__ticket_id[:3].isupper() and self.__ticket_id[3:].isdigit():
            return True
        return False


class Event(ABC):
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.__tickets = {}

    def add_ticket(self, ticket):
        if len(self.__tickets) < self.max_capacity:
            self.__tickets[ticket.ticket_id] = ticket
        else:
            raise ValueError("Event is full")
    def remove_ticket(self, ticket_id):
        if ticket_id in self.__tickets:
            del self.__tickets[ticket_id]
        else:
            raise ValueError("Ticket not found")
    @abstractmethod
    def generate_event_summary(self):
        pass


class Concert(Event):
    def __init__(self, name, max_capacity, artist):
        super().__init__(name,max_capacity)
        self.artist = artist

    def generate_event_summary(self):
        return f"{"Name: {self.name}\n Total tickets: {len(self.__tickets)}\n Artist: {self.artist}"}"


class PrivateEvent(Event):
    def __init__(self, name, artist ):
        super().__init__(name, 50)
        self.artist = artist
    
    def generate_event_summary(self):
        return f"Name: {self.name}\n Total tickets: {len(self.__tickets)}\n Artist: {self.artist}"
    
    admiral_freebee = PrivateEvent("Admiral Live", "Admiral Freebee")
    print(admiral_freebee)