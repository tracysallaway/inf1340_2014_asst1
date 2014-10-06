#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Tracy Sallaway, Sarah-Anne Schultheis'
__email__ = "tracy.armstrong@mail.utoronto.ca, sarah.schultheis@mail.utoronto.ca"

__copyright__ = "2014 Sarah-Anne Schultheis, Tracy Sallaway"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    gpa = 0.0

    if type(grade) is str:
        if grade == "A+":
            gpa = 4.0
        elif grade == "A":
            gpa = 4.0
        elif grade == "A-":
            gpa = 3.7
        elif grade == "B+":
            gpa = 3.3
        elif grade == "A-":
            gpa = 3.7
        elif grade == "B+":
            gpa = 3.3
        elif grade == "B":
            gpa = 3.0
        elif grade == "B-":
            gpa = 2.7
        elif grade == "FZ":
            gpa = 0.0
        else:
            raise ValueError('Please enter a valid grade')
        return gpa
    elif type(grade) is int:
        if grade >= 85 and grade <= 100:
            gpa = 4.0
        elif grade >= 80 and grade <= 84:
            gpa = 3.7
        elif grade >= 77 and grade <= 79:
            gpa = 3.3
        elif grade >= 73 and grade <= 76:
            gpa = 3.0
        elif grade >= 70 and grade <= 75:
            gpa = 2.7
        elif grade >= 0 and grade <= 69:
            gpa = 0.0
        else:
            raise ValueError('Please enter a valid integer grade between 0 and 100')
        return gpa
    else:
        raise TypeError('Please enter a valid letter or integer grade')

