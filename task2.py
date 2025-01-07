# create a game  that will generate the random numbers and ask user to guess it and give feedback on the basis of their number either its too low or too high or two low 

import random 

randomNumber= random.randint(1,10)
total_chance=5
while total_chance>0:
    print(f"you have remaining {total_chance} chances. ")
    UserInput= int(input("Enter the number"))
    
    if UserInput ==randomNumber:
        print("Congrats you have guess it right ")
        break

    elif UserInput<randomNumber:
        print("Its low than the number ")
    elif UserInput>randomNumber:
        print("Its high than the number ")

    total_chance-=1

if total_chance==0 and UserInput!=randomNumber:
        print("\n You couldnot guess the number right")

    