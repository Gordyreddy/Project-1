# Rock, Paper,Scissors with python


user_name = input("What is your name?\n").lower()  # takes username

file_name = (f"user_data/{user_name}_score.txt")  # converts the name to use as score file name
import os


def file_exists(file):
    return os.path.isfile(file)

# welcome message
if file_exists(file_name):

    def score_data():
        with open(f"user_data/{user_name}_score.txt") as user_file:
            file_data = user_file.read()
            if file_data != "":
                new_score = int(file_data)
            else:
                new_score = 0
        return new_score
    highscore = score_data()
    print(f"\nHey {user_name}, \nWelcome back :)\n")
    print(f"Your previous high score is: {highscore}")
else:
    highscore = 0
    print(f"\nHello {user_name},")
    print("welcome to ROCK PAPER SCISSORS a fun and exciting game.")

# game rules
print(
    "\nWinning rules of the game ROCK PAPER SCISSORS are:\n"
     "Rock vs Paper -> Paper wins \n"
     "Rock vs Scissors -> Rock wins \n"
     "Paper vs Scissors -> Scissors wins \n"
)

score = 0 # initial score

#game loop
while True:

    print("\nList of choices: \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n") #List of options to select

    # Checking if the input is an integer. If its not a int value then the loop runs again
    try:
        user_choice = int(input("Enter Your Choice: "))
    except ValueError:
            print("\nSomething went wrong :(\n")
            print("Use numbers\n" "\n 1 to select - Rock \n 2 to select - Paper \n 3 to select - Scissors \n")
            continue
    
    # Checking if the user selected options from the given numbers. If not the loop runs again
    if user_choice == 1 or user_choice == 2 or user_choice == 3:

        import random

        computer_choice = random.choice([1, 2, 3])
        choice = {1: "rock", 2: "paper", 3: "scissor"}
        print("")  # prints a blank space

        print(f"Your choise is: {choice[user_choice]}\n")
        print("Now it's Computer's Turn...")
        print(f"\nComputer choise is: {choice[computer_choice]}")
        print(f"\n{choice[user_choice]} VS {choice[computer_choice]}\n")

        # Game decision logic
        if user_choice == computer_choice:
            print("<== Its a draw! ==>")
        elif (
            (user_choice == 1 and computer_choice == 3)
            or (user_choice == 2 and computer_choice == 1)
            or (user_choice == 3 and computer_choice == 2)
        ):
            score += 1
            print("<== You won! ==>")
            print(f"Your score is: {score}\n")
            print(f"Your previous high score is: {highscore}")
        else:
            score = 0
            print("<== Computer won! ==>")
            print(f"Your Score is: {score}")
            print(f"Your previous high score is: {highscore}")
        if score >= highscore:
            with open(f"user_data/{user_name}_score.txt", "w") as file_write:
                file_write.write(str(score))

        print("")  # prints a blank space

        # Asks the user if they want to play again.
        replay = input("Do you want to play again?( y/n )\n")

        if replay == "y":
            continue
        elif replay == "n":
            print(f"Thankyou for playing {user_name}")
            break
        elif replay not in ("y", "n"):

            print("\nSomething went wrong")
            print("choose ( y ) for ( yes ) and choose ( n ) for ( no )")
            replay = input("Do you want to play again?( y/n )\n")

            if replay == "y":
                continue
            else:
                print("Something went wrong try please again.")
                break
    
    # If the user selects numbers other than (1,2,3) the code shown a prompt and the loop runs again
    else:
        print("\nSomething went wrong :(\n")
        print("Use numbers\n" "\n 1 to select - Rock \n 2 to select - Paper \n 3 to select - Scissors \n")
