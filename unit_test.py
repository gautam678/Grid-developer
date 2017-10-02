import unittest
from grid_developer import World, Event, Ticket
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
        random.seed(34)
        worldObj = World(10, 20)
        result = worldObj.closest_events(4, 5)
        expected_output = [(5, 12.47, 3),
                           (14, 69.99, 3),
                           (3, 21.19, 4),
                           (15, 15.22, 4),
                           (4, 25.35, 5)]
        self.assertEqual(expected_output, result)
        print "Test for Correct output passed"

    def test_output2(self):
        random.seed(34)
        worldObj = World(10, 20)
        result = worldObj.closest_events(4, 5,1)
        expected_output = [(5, 12.47, 3)]
        self.assertEqual(expected_output, result)
        print "Test for Correct output passed"


if __name__ == '__main__':
    unittest.main()
