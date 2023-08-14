import random

# function to generate number
def generate_random():
    while True:
        rand_num = str(random.randint(100,999))
        if rand_num[0] == rand_num[1] or rand_num[0] == rand_num[2] or rand_num[1] == rand_num[2]:
            continue
        else:
            return rand_num

# values
chances = 5
bulls = 0
cows = 0

# taking inputs from the user
player_name = input("Enter your name: ")
print(f"Hi {player_name}! Welcome to the game.\n You have {chances} to guess number.")
confirmation = input("Are you ready? (y/n): ")=='y'

rand_num = generate_random()

# game
if confirmation:
    print("Best of luck!")
    while chances>0:
        inp_num = input("Enter the number")
        if inp_num.isdigit():
            if inp_num == rand_num:
                print("Great! You won the game")
                break
            else:
                for idx in range(3):
                    if inp_num[idx] == rand_num[idx]:
                        bulls+=1
                    elif inp_num[idx] in rand_num:
                        cows+=1
                print(f"Hey {player_name},\n You got Cows: {cows}\n Bulls: {bulls}\n {chances-1} left.")
                bulls = 0
                cows = 0
                chances-=1
        else:
            print("Enter valid integer")
    else:
        print(f"The correct number is {rand_num} \n See you again")
else:
    print("All right. See you soon")