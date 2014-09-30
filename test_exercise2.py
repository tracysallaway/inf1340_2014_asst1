#!/usr/bin/env python3

""" Module to test exercise2.py """
import pytest

__author__ = 'Tracy Sallaway, Sarah-Anne Schultheis'
__email__ = "tracy.armstrong@mail.utoronto.ca, sarahschultheis@mail.utoronto.ca"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

from exercise2 import checksum

def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("892685001003") is True
    assert checksum("012345678905") is True
    assert checksum("692771017440") is True
    assert checksum("827624391275") is False
    assert checksum("012345678901") is False


def test_input():
   # """
    #Inputs that are the incorrect format and length
    #"""
    with pytest.raises(TypeError):
       checksum(1.0)
       checksum(786936224306)

    with pytest.raises(ValueError):
       checksum("1")
       checksum("1234567890")

    # other tests

# add functions for any other tests
