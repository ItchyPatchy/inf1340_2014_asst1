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

    # states letter_grade and gpa as blank value

    letter_grade = ""
    gpa = 0.0
    valid_letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]

    if type(grade) == str:
        print("letter")
        # check that the grade is one of the accepted values
        if grade in valid_letter_grades:
            print("Valid Letter Grade")
            if grade == "A+":
                gpa = 4.0
            if grade == "A":
                gpa = 4.0
            if grade == "A-":
                gpa = 3.7
            if grade == "B+":
                gpa = 3.3
            if grade == "B":
                gpa = 3.0
            if grade == "B-":
                gpa = 2.7
            if grade == "FZ":
                gpa = 0.0
        else:
            print("Wrong Letter Grade!")
            raise ValueError

    elif type(grade) is int:
        print("number")
        # check that grade is in the accepted range
        if grade in range(1, 100):
            print("Ok Number Range")
        # convert the numeric grade to a letter grade
        # assign the value to letter_grade
        # hint: letter_grade = mark_to_letter(grade)

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    elif letter_grade == "A":
        gpa = 4.0

    else:
        # raise a TypeError exception
        print("error")
        raise TypeError("Invalid type passed as parameter")

    return gpa