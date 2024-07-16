
name=input("What is your name?\n")

print("")# prints a blank space 

print(f"Hello, {name} let`s play rock paper scissor\n")
starting="y"
while( starting=="y" or c.lower()=="y"):
    u=input("Choose one ( Rock, Paper or scissor) \n")

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
        
        print("")# prints a blank space 
        
        c=input("Do you want to play again?( y/n )\n")

        print("")# prints a blank space 
        
        if(c=="y"):
            continue
        
        elif(c=="n"):
            print(f"Thankyou for playing with me {name}")
            break

        elif( c != "y" or c != "n" ):
            print("Something went wrong")
            print("choose ( y ) for ( yes ) and choose ( n ) for ( no )")

            print("")# prints a blank space 
            
            c=input("Do you want to play again?( y/n )\n")
        
        if(c=="y"):
            continue
        
        else:
            print(f"Thankyou for playing with me {name}")
    elif( user_input != "rock" or user_input != "paper" or user_input != "scissor" ):
        print("Something went wrong")
        print(f"Thankyou for playing with me {name}")
        break
else:
    print("Something went wrong")
    print(f"Thankyou for playing with me {name}")