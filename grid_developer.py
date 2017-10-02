"""
Author : Gautam Somappa

The program accepts user location as a pair of co-ordinates,
and returns a list of the five closest events,
along with the cheapest ticket
price for each event.
"""


import random


class World:
    """ The class World has all the events running on it.
    This is synonomous to a real world
    and each coordinate hosts an event. The events are
    generated through seeded random
    data and each event is stored in a list as an Event object.

    The class World has functions to display the data and
    calculate closest events to the user

    Variables:
    - List of events in world
    """
    list_of_events = []

    def __init__(self, size, number_events):
        """ This is a generator function that generates
        random events and populates the world.

        Each event must be lying within the boundaries of the world
        and should have zero or more tickets.
        For simplicity, we have taken the maximum number of tickets to be 10
        """
        for num in range(0, number_events):
            x = random.randint(-size, size)
            y = random.randint(-size, size)
            numberTickets = random.randint(0, 10)  # Tickets cannot exceed 10
            event = Event(num, x, y, numberTickets)  # Create Event
            self.add_event(event)  # Add event to your world

    def add_event(self, Event):
        """ This function adds events to a list after checking if the
        event ID and location is unique. If the location is not unique
        a zero is returned and the event is discarded.

        If the location is not unique, the event is discared like
        the previous example.
        """
        for event in self.list_of_events:
            if event.get_id() == Event.id:
                print "ID is not unique"
                return 0
            if event.get_coordinates() == (Event.x, Event.y):
                print "Location is not unique"
                return 0
        Event.set_ticket_price()
        self.list_of_events.append(Event)

    def display(self):
        """ Displays the following:
         - Event number
         - Location of event
         - Price of tickets (2 decimal places)
        """
        for event in self.list_of_events:
            print "Event Number: ", event.get_id()
            print "Location", event.get_coordinates()
            print "Ticket prices: ",
            ticket_prices = event.get_tickets()
            for ticket in ticket_prices:
                print "%.2f" % ticket.get_price(),
            print "\n"

    def closest_events(self, x, y, nearest=5):
        """ Function calculates the nearest five events
        from user input. Events are sorted based on their
        distance from input and n-nearest neighbours
        are returned.
        """
        for event in self.list_of_events:
            event.distance_from_input(x, y)
        closeEvents = sorted(self.list_of_events,
                             key=lambda x: x.get_distance(), reverse=False)
        for j in closeEvents[:nearest]:
            minimum = j.minimum_price()
            print "Event", "{0:0=3d}".format(j.get_id()), \
                  "-", "$%.2f," % minimum, "Distance", j.distance


class Event:
    """The class Event is unique to a location and has a unique identifier.
    Event holds the number of tickets available and the price of each ticket.
    Event also has functions to identify the cheapest ticket.

    Variables:
    - unique identifier
    - x coordinate
    - y coordinate
    - number of tickets
    - list containing the objects for class ticket
    - distance of event from input
    """
    numTickets = 0

    def __init__(self, id, x, y, numTickets):
        self.id = (id+1)
        self.x = x
        self.y = y
        self.numTickets = numTickets
        self.tickets = []

    def get_id(self):
        """ Returns the unique identifier for Event
        """
        return self.id

    def get_tickets(self):
        """ Returns the list containing tickets
        """
        return self.tickets

    def get_coordinates(self):
        """ Returns the coordiantes of the event
        """
        return self.x, self.y

    def get_distance(self):
        """ Returns the Manhattan distance of each event from Input
        """
        return self.distance

    def set_ticket_price(self):
        """ A generator function that randomly assigns ticket price to the event.
        Ticket prices are sampled from a range of 1 - 100.
        These values are added to an instance of class ticket
        """
        while self.numTickets > 0:
            price = random.uniform(1, 100)
            ticket = Ticket(price)
            self.tickets.append(ticket)
            self.numTickets -= 1

    def minimum_price(self):
        """ A function that calculates minimum price of tickets in a given event.
        The value of tickets are appended to a
        list and min of that list is calculated.
        """
        ticket_prices = []
        for j in self.tickets:
            ticket_prices.append(j.get_price())
        return min(ticket_prices)

    def distance_from_input(self, sx, sy):
        """ Function that calculates the Manhattan distance between two
        coordinated. The manhattan distance is calculates as:

        Manhattan Distance = absolute(destination_x - input_x) +
                             absolute(destination_y - input_y)
        """
        self.distance = abs(self.x - int(sx)) + abs(self.y - int(sy))


class Ticket:
    """The class Ticket holds the price of each ticket.
    Attributes to a ticket can be easily added here
    """
    def __init__(self, price):
        self.price = price

    def get_price(self):
        """Returns the price of a ticket
        """
        return self.price
