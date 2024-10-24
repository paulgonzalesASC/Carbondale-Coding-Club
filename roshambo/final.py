import random

isGameOn = True

# Initializing options as variables
options=["rock","paper","scissors"]
rock=options[0]
paper=options[1]
scissors=options[2]

result = ""
computer_score = 0
player_score = 0

while isGameOn:

    # Return a number between 0 and 2. Including 0 and 2
    random_num=random.randint(0,2)

    # Computer option generated at random.
    computer_option=options[random_num]

    # User option generated via input
    user_option=input("your move ").lower()

    # Conditions to check whos the winner
    if user_option==rock and computer_option==paper:
        result = "Computer"
        computer_score += 1
    if user_option==scissors and computer_option==rock:
        result = "Computer"
        computer_score += 1
    if user_option==paper and computer_option==scissors:
        result = "Computer"
        computer_score += 1
    if user_option==paper and computer_option==rock:
        result = "User"
        player_score += 1
    if user_option==rock and computer_option==scissors:
        result = "User"
        player_score += 1
    if user_option==scissors and computer_option==paper:
        result = "User"
        player_score += 1

    # Condition to check for a tie
    if user_option==computer_option:
        result = "Tie"

    # Final print statement to show the outcome of the game
    print("------------------------------------")
    print(f"Your option: {user_option} - Computer Option: {computer_option}")
    print(f"Game Result: {result}")
    print(f"Computer: {computer_score} | Player: {player_score}")
    print("------------------------------------")

    #Ask the user if they want to keep playing
    keep_playing = input("Do you want to play again? y or n.").lower()

    if keep_playing == "n": 
        break
    else: continue