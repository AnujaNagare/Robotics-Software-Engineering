# Write a python function for the following declarations:

import re
import math


# all locations are tuples, which represent an x-y
# coordinate pair.

# do not alter the printLocation function
def printLocation(location):
    print("Location = (%i, %i)" % (location[0], location[1]))


def moveForwardX(distance, startLocation):
    # TODO: Calculate the distance along the
    # X (horizontal) axis.
    # Return the new location as a tuple of
    # coordinates x and y
    x = startLocation[0] + distance
    y = startLocation[1]
    new = (x, y)
    return new


def moveForwardY(distance, startLocation):
    # TODO: Calculate the distance along the
    # Y (vertical) axis.
    # Return the new location as a tuple of
    # coordinates x and y
    x = startLocation[0]
    y = startLocation[1] + distance
    new = (x, y)
    return new


def calcDistance(distanceX, distanceY):
    # TODO: Return the straight line distance
    # From the start location to the end location
    # Recall: x*x*x = x**3 in python
    return math.sqrt((distanceX ** 2) + (distanceY ** 2))


def robotVelocity(distance, time):
    # TODO: Return velocity using the straight line
    # distance and the given time
    return distance / time
