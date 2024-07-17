import os
def file_exists(file):
    return os.path.isfile(file)
un=input("What is your name?\n")
name=un.lower()

print("")# prints a blank space 

file = (f"user_data/{name}_score.txt")
exists = file_exists(file)


if(exists == True ):
    def d():
        with open (f"user_data/{name}_score.txt") as f:
            highscorei=f.read()
            if(highscorei!=""):
                highscore=int(highscorei)
            else:
                highscore = 0
        return highscore
    highscore=d()
    print(f"Hello {name} \nWelcome back :)\n")
    print(f"Your previous high score is: {highscore}")
    
    print("")# prints a blank space 

else:
    def d():
        highscore = 0
        return highscore
    print(f"Hey {name}\n")
    print("welcome to rock paper scissor a fun and exciting game.\n")
    print("Author: Arvind Gotike\n")
highscore=d()
score = 0
starting = "y"
while( starting=="y" or c.lower()=="y"):
    u=input("Choose one \n( Rock, Paper or scissor) \n")

    print("")# prints a blank space 

    import random
    computer=random.choice([1,2,3])
    user_input=u.lower()

    if( user_input == "rock" or user_input == "paper" or user_input == "scissor" ):
        cdict={"rock":1, "paper":2, "scissor":3}
        rdict={1:"rock",2:"paper",3:"scissor"}
        user=cdict[user_input]

        print("")# prints a blank space 

        print(f"You choose {u.lower()} and the computer choose {rdict[computer]}\n")
        a=computer
        b=user
        def output(a , b):
            if(a==b):
                print("Its a draw!")
            else:
                if(a==1 and b==3):
                    return "You lost!"
                elif(a==1 and b==2):
                    return "You won!"
                elif(a==2 and b==1):
                    return "You lost!"
                elif(a==2 and b== 3):
                    return "You won!"
                elif(a==3 and b==2):
                    return "You lost!"
                elif(a==3 and b==1):
                    return "You lost!"
        o=output(a, b)
        print(o)

        print("")# prints a blank space 

        if (o == "You won!" ):
            score+=1
            print(f"Your score is: {score}\n")
            print(f"Your previous high score is: {highscore}")
        elif(o == "You lost!"):
            score=0
            print(f"Your Score is: {score}\n")
            print(f"Your previous high score is: {highscore}")
        else:
            print(f"Your Score is: {score}\n")
            print(f"Your previous high score is: {highscore}")
        if(score>=highscore):
            with open(f"user_data/{name}_score.txt", "w") as wr:
                wr.write(str(score))

        print("")# prints a blank space 
            
        c=input("Do you want to play again?( y/n )\n")

        print("")# prints a blank space 
            
        if(c=="y"):
            continue
            
        elif(c=="n"):
            print(f"Thankyou for playing {name}")
            break

        elif( c != "y" or c != "n" ):
            print("Something went wrong")
            print("choose ( y ) for ( yes ) and choose ( n ) for ( no )")

            print("")# prints a blank space 
                
            c=input("Do you want to play again?( y/n )\n")
            
        if(c=="y"):
            continue
            
        else:
            print(f"Thankyou for playing {name}")
    elif( user_input != "rock" or user_input != "paper" or user_input != "scissor" ):
        print("Something went wrong")
        print(f"Thankyou for playing {name}")
        break
else:
    print("Something went wrong")
    print(f"Thankyou for playing {name}")
