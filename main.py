# Rock, Paper,Scissors with python


user_name = input("What is your name?\n").lower()  # takes username

file_name = (
    f"user_data/{user_name}_score.txt"  # converts the name to use as score file name
)
import os


def file_exists(file):
    return os.path.isfile(file)


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
    print(f"Hello {user_name}, \nWelcome back :)\n")
    print(f"Your previous high score is: {highscore}")
else:
    print(f"Hey {user_name},")
    print("welcome to 'rock, paper, scissor' a fun and exciting game.")
    
score = 0

while True:
    user_input = input("\nChoose one \n( Rock, Paper or scissor) \n").lower()

    if user_input == "rock" or user_input == "paper" or user_input == "scissor":

        import random

        computer_choice = random.choice([1, 2, 3])
        choice = {"rock": 1, "paper": 2, "scissor": 3}
        reverse_choice = {1: "rock", 2: "paper", 3: "scissor"}
        user_choice = choice[user_input]
        print("")  # prints a blank space

        print(
            f"Your choose: {user_input}\nComputer choose: {reverse_choice[computer_choice]}"
        )

        print("")  # prints a blank space

        if user_choice == computer_choice:
            print("Its a draw!")
        elif (
            (user_choice == 1 and computer_choice == 3)
            or (user_choice == 2 and computer_choice == 1)
            or (user_choice == 3 and computer_choice == 2)
        ):
            score += 1
            print("You won!")
            print(f"Your score is: {score}\n")
            print(f"Your previous high score is: {highscore}")
        else:
            score = 0
            print("You lost!")
            print(f"Your Score is: {score}")
            print(f"Your previous high score is: {highscore}")
        if score >= highscore:
            with open(f"user_data/{user_name}_score.txt", "w") as file_write:
                file_write.write(str(score))

        print("")  # prints a blank space

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

    else:
        print("Something went wrong please try again...")
        break
