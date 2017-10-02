"""
Author : Gautam Somappa

The program accepts user location as a pair of coordinates,
and returns a list of the five closest events,
along with the cheapest ticket
price for each event.
"""


import random
from event import Event


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

    def __init__(self, size, number_events):
        """ This is a generator function that generates
        random events and populates the world.

        Each event must be lying within the boundaries of the world
        and should have zero or more tickets.
        For simplicity, we have taken the maximum number of tickets to be 10
        """
        self.list_of_events = []
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
                print "ID is not unique, skipping : ", event.get_id()
                return 0
            if event.get_coordinates() == (Event.x, Event.y):
                print "Location is not unique, skipping : ", event.get_id()
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
                print "%05.2f" % ticket.get_price(),
            print "\n"

    def closest_events(self, x, y, nearest=5):
        """ Function calculates the nearest five events
        from user input. Events are sorted based on their
        distance from input and n-nearest neighbours
        are returned.
        """
        storeResult = []
        for event in self.list_of_events:
            event.distance_from_input(x, y)
        closeEvents = sorted(self.list_of_events,
                             key=lambda x: x.get_distance(), reverse=False)
        for j in closeEvents[:nearest]:
            minimum = j.minimum_price()
            storeResult.append((j.get_id(), minimum, j.get_distance()))
        return storeResult
