#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Paul Fisher'
__email__ = "ptg.fisher@gmail.com"

__copyright__ = "2014 Paul Fisher"
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

    # defines variable input
    type(grade)
    # sets letter_grade as blank string
    letter_grade = ""

    if grade is str:
        # check that the grade is one of the accepted values
        if grade is 'A+''A-''B+''B''B-''FZ':
            assert grade == letter_grade

    elif grade is int:
        round(grade, 0)
        # checks if value is in expected range
        if int < 100:
            raise ValueError
        if int > 0:
            raise ValueError
        # convert the numeric grade to a letter grade
        if int is range(85, 100):
            assert letter_grade == "A+,A"
        if int is range(80, 84):
            assert letter_grade == "A-"
        if int is range(77, 79):
            assert letter_grade == "B+"
        if int is range(73, 76):
            assert letter_grade == "B"
        if int is range(70, 72):
            assert letter_grade == "B-"
        if int is range(0, 69):
            assert letter_grade == "FZ"

    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")


    # assign the value to letter_grade
    if letter_grade == "A+""A":
        gpa = 4.0
    if letter_grade == "A-":
        gpa = 3.7
    if letter_grade == "B+":
        gpa = 3.3
    if letter_grade == "B":
        gpa = 3.0
    if letter_grade == "B-":
        gpa = 2.7
    if letter_grade == "FZ":
        gpa = 0.0

    return gpa