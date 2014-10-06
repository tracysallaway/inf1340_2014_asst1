#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_decide_rps():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Paper", "Paper") == 0

def test_input():
    """
    inputs that are incorrect values or types
    """
    with pytest.raises(ValueError):
        decide_rps("Stones", "Paper")
        decide_rps("Stones", "Stones")
        decide_rps("Rock", 3)
        decide_rps(4.0, "Hi")
