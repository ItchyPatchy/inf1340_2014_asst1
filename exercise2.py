#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """
    # creates blank list to store output of string append (short variable to avoid congestion in equations)
    k = []
    # generate a checksum from first 11 digits

    # check type of input
    if type(upc) is str:
        print("That's a string, buddy.")
        # check length of string
        if len(upc) == 12:
            print("And that's 12 digeridoos!")
            # convert string to array
            for digit in upc:
                k.append(int(digit))
            print(k)
        # raise ValueError if not 12
        else:
            print("You sure that is 12 digits?")
            raise ValueError

    # raise TypeError if not string
    else:
        print("Not a string value")
        raise TypeError
    # check against the the twelfth digit

    # return True if they are equal, False otherwise

    return False

