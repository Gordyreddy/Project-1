# Rock, Paper,Scissors with python

import random
import os

from game import welcome
from game import user_input
from game import game_logic
from game import play_again


USER_NAME = input("Enter your name.\n")
SCORE = 0 # initial score for a new game
CHOICES = {1: "rock", 2: "paper", 3: "scissor"}


def main():
    high_score = welcome(USER_NAME, os)
    while True:

        user_choice = user_input()
        game_logic(user_choice, SCORE, high_score, CHOICES, USER_NAME, random)
        value = play_again(USER_NAME)
        if value != True:
            break


main()
