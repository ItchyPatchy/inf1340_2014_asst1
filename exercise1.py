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

    # states letter_grade as blank value
    letter_grade = ""

    # states gpa as blank value
    gpa = ()

    if type(grade) is str:
        # check that the grade is one of the accepted values
        if type(grade) == "A+":
            assert type(grade) == letter_grade
        if type(grade) == "A":
            assert type(grade) == letter_grade
        if type(grade) == "A-":
            assert type(grade) == letter_grade
        if type(grade) == "B+":
            assert type(grade) == letter_grade
        if type(grade) == "B":
            assert type(grade) == letter_grade
        if type(grade) == "B-":
            assert type(grade) == letter_grade
        if type(grade) == "FZ":
            assert type(grade) == letter_grade

    elif type(grade) is int:
        # rounds input to whole number
        round(type(grade), 0)
        # checks if value is in expected range
        if 100 > type(grade):
            raise ValueError
        if 0 < type(grade):
            raise ValueError
        # convert the numeric grade to a letter grade
        if type(grade) is range(85, 100):
            assert "A+" == letter_grade
        if type(grade) is range(80, 84):
            assert "A-" == letter_grade
        if type(grade) is range(77, 79):
            assert "B+" == letter_grade
        if type(grade) is range(73, 76):
            assert "B" == letter_grade
        if type(grade) is range(70, 72):
            assert "B-" == letter_grade
        if type(grade) is range(0, 69):
            assert "FZ" == letter_grade

    # assign the gpa value to letter_grade
    if letter_grade == "A+":
        assert 4.0 == gpa
    if letter_grade == "A":
        assert 4.0 == gpa
    if letter_grade == "A-":
        assert 3.7 == gpa
    if letter_grade == "B+":
        assert 3.3 == gpa
    if letter_grade == "B":
        assert 3.0 == gpa
    if letter_grade == "B-":
        assert 2.7 == gpa
    if letter_grade == "FZ":
        assert 0.0 == gpa

    else:
        # raise a TypeError exception
        print("error")
        raise TypeError("Invalid type passed as parameter")

    return gpa