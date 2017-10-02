"""
Author : Gautam Somappa

The program accepts user location as a pair of co-ordinates,
and returns a list of the five closest events, along with the cheapest ticket
price for each event.
"""

import random
import argparse
from grid_developer import World

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="The program accepts"
                                                 " user location"
                                                 " as a pair of coordinates"
                                                 " and returns a list of"
                                                 " the five closest events,"
                                                 " along with the cheapest"
                                                 " ticket price for events.")
    parser.add_argument('--verbose', help='Display events and attributes',
                        required=False, action="store_true")
    args = parser.parse_args()
    size = 10  # Size of the world
    random.seed(34)
    number_of_events = 10  # Number of events in world
    world = World(size, number_of_events)
    if args.verbose:
        world.display()
    coordinates = raw_input("Please Input Coordinates:")
    print "\n"
    x, y = coordinates.split(',')
    print "Closest Events to (%s , %s): " % (x, y)
    print "\n"
    world.closest_events(x, y)
