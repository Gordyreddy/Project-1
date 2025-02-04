import random
import os


USER_NAME = input("Enter your name.\n")
SCORE = 0  # initial score for a new game
CHOICES = {1: "rock", 2: "paper", 3: "scissor"}


def welcome():
    file_path = f"user_data/{USER_NAME.lower()}_score.txt"
    if os.path.isfile(file_path):
        with open(file_path, "r") as user_file:
            file_data = user_file.read()
            if file_data != "":
                old_score = int(file_data)
            else:
                old_score = 0
        print(f"\nHey {USER_NAME}, \nWelcome back :)")
        print(f"Your previous high score is: {old_score}")

        return old_score
    else:
        new_score = 0
        print(f"\nHello {USER_NAME},")
        print("Welcome to ROCK PAPER SCISSORS a fun and exciting game.")

        return new_score


def user_input():
    print(
        "\nWinning rules of the game ROCK PAPER SCISSORS are:\n"
        "Rock vs Paper -> Paper wins \n"
        "Rock vs Scissors -> Rock wins \n"
        "Paper vs Scissors -> Scissors wins \n"
    )
    while True:
        print("\nList of choices: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        user_choice = input("Enter Your Choice: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice in (1, 2, 3):
                break
            else:
                print("Use numbers 1, 2, 3 to select.")
        else:
            print("\nPlease enter a number.\n")

    return user_choice


def game_logic(user_choice, high_score):
    computer_choice = random.choice([1, 2, 3])

    print(f"Your choise is: {CHOICES[user_choice]}\n")
    print("Now it's Computer's Turn...")
    print(f"\nComputer choise is: {CHOICES[computer_choice]}")
    print(f"\n{CHOICES[user_choice]} VS {CHOICES[computer_choice]}\n")

    if user_choice == computer_choice:
        print("<== Its a draw! ==>")
    elif (
        (user_choice == 1 and computer_choice == 3)
        or (user_choice == 2 and computer_choice == 1)
        or (user_choice == 3 and computer_choice == 2)
    ):
        SCORE += 1
        print("<== You won! ==>")
        print(f"Your score is: {SCORE}\n")
        print(f"Your previous high score is: {high_score}")
    else:
        SCORE = 0
        print("<== Computer won! ==>")
        print(f"Your Score is: {SCORE}")
        print(f"Your previous high score is: {high_score}")
    if SCORE >= high_score:
        with open(f"user_data/{USER_NAME}_score.txt", "w") as file_data:
            file_data.write(str(SCORE))

def play_again():
    while True:
        play_again = input("Do you want to play again?( y/n )\n")
        if play_again in("y",'n'):
            if play_again == "y":
                value = True
            elif play_again == "n":
                print(f"Thankyou for playing {USER_NAME}")
                break
            return value
        else:
            print("Invalid input.\nchoose ( y ) for ( yes ) and choose ( n ) for ( no )")
