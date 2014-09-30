#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Tracy Sallaway, Sarah-Anne Schultheis'
__email__ = "tracy.armstrong@mail.utoronto.ca, sarah.schultheis@mail.utoronto.ca"

__copyright__ = "2014 Tracy Sallaway and Sarah-Anne Schultheis"

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
        ValueError if string is the wrong length (with error string stating how many digits are over or under)
    """

    # check type of input and raise TypeError if not string
    if len(upc) != 12:
        raise ValueError('UPC values must be exactly 12 characters')
    if type(upc) != str:
        raise TypeError('Input must be of type string')

    #input_type = type(upc)
    #if input_type != str:
        #print("TypeError: Input must be of type string")
    #else:
        #print("Type Correct")

    # check length of string and raise ValueError if not 12
    #input_length = len(upc)
    #if input_length != 12:
        #print("ValueError: Input must be 12 characters in length")
    #else:
        #print("Length Correct")

    # convert string to array
    list(upc)

    # generate checksum with first 11 digits provided
    # Note: odd positions denoted as even and vice versa due to Python index position 0
    odd_upc = ((int(upc[0]) + int(upc[2]) + int(upc[4]) + int(upc[6]) + int(upc[8]) + int(upc[10])) * 3)
    even_upc = odd_upc + (int(upc[1]) + int(upc[3]) + int(upc[5]) + int(upc[7]) + int(upc[9]))
    final_checksum = even_upc % 10

    # check against twelfth digit, return True if equal, False otherwise
    if final_checksum == 0:
        final_checksum = final_checksum
    else:
        final_checksum = 10 - (int(final_checksum))

    if int(final_checksum) == int(upc[11]):
        return True
    else:
        return False

