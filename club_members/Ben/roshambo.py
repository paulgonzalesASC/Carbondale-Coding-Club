# import random

# # Initializing options as variables
# options=["rock","paper","scissors"]
# rock=options[0]
# paper=options[1]
# scissors=options[2]

# # Return a number between 0 and 2. Including 0 and 2
# random_num=random.randint(0,2)

# # Computer option generated at random.
# computer_option=options[random_num]

# # User option generated via input
# user_option=input("your move ").lower()

# # Conditions to check whos the winner
# if user_option==rock and computer_option==paper:
#     print("computer wins")
# if user_option==scissors and computer_option==rock:
#     print("computer wins")
# if user_option==paper and computer_option==scissors:
#     print("computer wins")
# if user_option==paper and computer_option==rock:
#     print("you win")
# if user_option==rock and computer_option==scissors:
#     print("you win")
# if user_option==scissors and computer_option==paper:
#     print("you win")

# # Condition to check for a tie
# if user_option==computer_option:
#     print("its a tie")

# # Final print statement to show the outcome of the game
# print("you:"+user_option+" computer "+computer_option)

import time 

isGameOn = True
count = 1

while isGameOn:

    if count <= 10:
        time.sleep(1)
        print(f"Less than 11. The count is {count}")
        count +=1
    elif count <= 20:
        time.sleep(1)
        print(f"Less than 21. The count is {count}")
        count += 1 
    else:
        break
