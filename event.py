"""
Author : Gautam Somappa

The program accepts user location as a pair of coordinates,
and returns a list of the five closest events,
along with the cheapest ticket
price for each event.
"""


from ticket import Ticket
import random


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
            price = round(random.uniform(1, 99), 2)
            ticket = Ticket(price)
            self.tickets.append(ticket)
            self.numTickets -= 1

    def minimum_price(self):
        """ A function that calculates minimum price of tickets in a given event.
        The value of tickets are appended to a list and min of that
        list is calculated.
        """
        ticket_prices = []
        if len(self.tickets) == 0:
            return 0
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
