#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock, Paper, Scissors

This module contains one function that outputs a value of 0, 1 or 2 based on the comparison of two input values
(player1 and player2). Accepted inputs are "Rock","Paper", and "Scissors". Output values denote a tie, or a win for player 1 or 2.
All other inputs will result in error.

"""

__author__ = 'Paul Fisher'
__email__ = "ptg.fisher@gmail.com"

__copyright__ = "2014 Paul Fisher"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def decide_rps(player1, player2):
    """
    Returns value of 0, 1 or 2 to denote a tie, or a win for either player1 or player2.

    :param:
        player1: Player 1 selection. String, accepted values are "Rock", "Paper", "Scissors".
        player2: Player 2 selection. String, accepted values are "Rock", "Paper", "Scissors".

    :return:
        0: Denotes a tie. Occurs in the event that player1 value and player2 value are the same.
        1: Denotes a win for Player 1. Occurs when player1 key matches the value in dictionary.
        2: Denotes a win for Player 2. Occurs when player1 key does not match value in dictionary, and is not the same.

    :raises:
        TypeError if parameter is not a string
        ValueError if parameter is not in accepted list
    """
    # sets accepted input values
    valid_strings = ["Rock", "Paper", "Scissors"]
    # sets the conditions of a player1 win, based on a dictionary key and value
    wins = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    # detects if input values are strings.
    if type(player1) is str:
        # was not sure how to have these in same line, had to have separate "if/else" statements
        if type(player2) is str:
            # detects if the input string is in list of accepted terms. Again, two separate statements for each player.
            if player1 in valid_strings:
                if player2 in valid_strings:
                    # if the player1 key matches the dictionary, it is a win
                    if wins[player1] == player2:
                        return 1
                    # if the inputs are the same, it is a tie.
                    if player1 == player2:
                        return 0
                    # if player1 does not win, and it is not a tie, player2 must be the winner.
                    else:
                        return 2
# the rest of these values just raise errors if input is wrong. They are duplicated for each "if/else" statement.
                else:
                    print("You can't just say what you want")
                    raise ValueError
            else:
                print("You can't just say what you want")
                raise ValueError

        else:
            print("You need to give me some string")
            raise TypeError
    else:
        print("You need to give me some string")
        raise TypeError