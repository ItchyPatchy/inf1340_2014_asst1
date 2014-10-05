#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    # other tests
    #assert decide_rps("Chicken", "Cow") == 0
    assert decide_rps("Scissors", "Paper") == 1
    #assert decide_rps(4509, 4207) == 0
