"""
Author : Gautam Somappa

The program accepts user location as a pair of coordinates,
and returns a list of the five closest events, along with the cheapest ticket
price for each event.
"""

import random
import argparse
from grid_developer import World
import sys

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
    number_of_events = 20  # Number of events in world
    world = World(size, number_of_events)
    if args.verbose:
        world.display()
    coordinates = raw_input("Please Input Coordinates:")
    print "\n"
    try:
        x, y = coordinates.split(',')
        if abs(int(x)) > size and abs(int(y)) > size:
            print "The coordinates you have entered" \
                  " is out of this world, try again!"
            sys.exit()
        print "Closest Events to (%s , %s): " % (x, y)
        print "\n"
    except ValueError:
        print "Invalid input, try again"
        exit()
    result = world.closest_events(x, y)
    for (id, minimum, distance) in result:
        print "Event", "{0:0=3d}".format(id), \
                  "-", "$%05.2f," % (minimum,), "Distance", distance
