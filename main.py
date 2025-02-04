# Rock, Paper,Scissors with python

from game import welcome
from game import user_input
from game import game_logic
from game import play_again


def main():
    high_score = welcome()
    
    while True:
        user_choice = user_input()
        game_logic(user_choice, high_score)
        value = play_again()
        if value != True:
            break


main()
