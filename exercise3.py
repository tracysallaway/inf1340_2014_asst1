#!/usr/bin/env python3

"""
    Assignment 1, Exercise 3, INF1340 Fall 2014
"""

__author__ = 'Tracy Sallaway, Sarah-Anne Schultheis'
__email__ = "tracy.armstrong@mail.utoronto.ca, sarah.schultheis@mail.utoronto.ca"
__copyright__ = "2014 Tracy Sallaway and Sarah-Anne Schultheis"

# imports one per line


def decide_rps(player1, player2):

    """
    Checks the results of a match of rock, paper, scissors between two players

    :param player1: player1 response as a str - options are Rock, Paper, or Scissors
           player2: player2 response as a str - options are Rock, Paper, or Scissors
    :return:
        int - 1 if player1 wins
        int - 2 if player2 wins
        int - 0 if there is a tie
    :raises:
        ValueError if inputs do not match available options
    """

    rps_results = {}
    rps_results[("Rock", "Paper")] = 2
    rps_results[("Rock", "Scissors")] = 1
    rps_results[("Paper", "Rock")] = 1
    rps_results[("Scissors", "Rock")] = 2
    rps_results[("Paper", "Scissors")] = 2
    rps_results[("Scissors", "Paper")] = 1
    rps_results[("Rock", "Rock")] = 0
    rps_results[("Paper", "Paper")] = 0
    rps_results[("Scissors", "Scissors")] = 0
    results = (player1, player2)
    if results in rps_results:
        return rps_results.get(results)
    else:
        raise ValueError('Please enter one of the valid inputs - Rock, Paper, or Scissors')