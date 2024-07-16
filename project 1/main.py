name=input("What is your name?\n")

print("")# prints a blank space 

print(f"Hello, {name} let`s play rock paper scissor\n")

u=input("Choose one ( Rock, Paper or scissor) \n")

print("")# prints a blank space 

import random
computer=random.choice([1,2,3])
user_input=u.lower()
cdict={"rock":1, "paper":2, "scissor":3}
rdict={1:"rock",2:"paper",3:"scissor"}
user=cdict[user_input]

print("")# prints a blank space 

print(f"You choose {u.lower()} and the computer choose {rdict[computer]}")
a=computer
b=user
def output(a , b):
    if(a==b):
        print("Its a draw!")
    else:
        if(a==1 and b==3):
            return "Computer won!"
        elif(a==1 and b==2):
            return "You won!"
        elif(a==2 and b==1):
            return "Computer won!"
        elif(a==2 and b== 3):
            return "You won!"
        elif(a==3 and b==2):
            return "Computer won!"
        elif(a==3 and b==1):
            return "Computer won!"

print(output(a , b))