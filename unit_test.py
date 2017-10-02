import unittest
from grid_developer import World
from event import Event
from ticket import Ticket
import random
 
 
class GridDeveloper(unittest.TestCase):
    """Class that runs unit tests. Each testing case
    is contained in a seperate function"""

    def test_instance_world(self):
        """Unit test to check if an instance of part of the class World"""
        size = 10
        number_of_events = 20
        worldObj = World(size, number_of_events)
        self.assertIsInstance(worldObj, World)
        print "Test for world object passed"

    def test_instance_event(self):
        """Unit test to check if an instance of part of the class Event"""
        eventObj = Event(1, 5, -5, 3)
        self.assertIsInstance(eventObj, Event)
        print "Test for event object passed"

    def test_instance_ticket(self):
        """Unit test to check if an instance of part of the class Event"""
        ticketObj = Ticket(20)
        self.assertIsInstance(ticketObj, Ticket)
        print "Test for ticket object passed"

    def test_output1(self):
        event1 = Event(1, 0, 0, 10)
        event2 = Event(2, 0, 1, 5)
        event1.distance_from_input(1,1)
        event2.distance_from_input(1,1)
        distance_event1 = event1.get_distance()
        distance_event2 = event2.get_distance()
        self.assertEqual(2, distance_event1)
        self.assertEqual(1, distance_event2)
        print "Test for Manhattan distance passed"


if __name__ == '__main__':
    unittest.main()