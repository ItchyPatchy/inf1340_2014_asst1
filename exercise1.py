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
    # defines valid letter grades
    valid_letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]
    if type(grade) == str:
        # check that the grade is one of the accepted values
        if grade in valid_letter_grades:
            print("Valid Letter Grade")
            letter_grade = grade
        else:
            print("Invalid Letter Grade!")
            raise ValueError
    elif type(grade) is int:
        # check that grade is in the accepted range
        if (grade <= 100) and (grade >= 0):
            print("Valid Number Range")
            # assign the value to letter_grade
            letter_grade = mark_to_letter(grade)
        else:
            print("Invalid Number Range!")
            raise ValueError
    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.0
    else:
        # raise a TypeError exception
        print("error")
        raise TypeError("Invalid type passed as parameter")
    return gpa


# convert the numeric grade to a letter grade
def mark_to_letter(grade_input):
    if (grade_input <= 100) and (grade_input >= 90):
        return "A+"
    if (grade_input <= 89) and (grade_input >= 85):
        return "A"
    if (grade_input <= 84) and (grade_input >= 80):
        return "A-"
    if (grade_input <= 79) and (grade_input >= 77):
        return "B+"
    if (grade_input <= 76) and (grade_input >= 73):
        return "B"
    if (grade_input <= 72) and (grade_input >= 70):
        return "B-"
    if (grade_input <= 69) and (grade_input >= 0):
        return "FZ"