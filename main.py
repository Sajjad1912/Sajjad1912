'''
1 for snake
-1 for water
0 for gun
'''
import random

# computer's choice
computer = random.choice([-1, 0, 1])

# user's choice
you_string = input("Enter your choice (Snake,Water,Gun) : ")

# Mapping of choices
youDict = {"Sanke" : 1 , "Water" : -1 , "Gun" : 0}
reversDist = {1 : "Snake" , -1 : "Water" , 0 : "Gun" }

# Map user and computer choices to numeric values
you = youDict[you_string]
print(f"You chose {you_string} \nComputer chose {reversDist[computer]}")

# Determine the result
if computer == you :
    print("It's a draw.")
else:
    if computer == -1 and you == 1 :
        print("You win and computer lose.")
    elif computer == -1 and you == 0 :
        print("Computer win and you lose.")
    elif computer == 1 and you == -1 :
        print("Computer win and you lose.")
    elif computer == 1 and you == 0 :
        print("You win and computer lose.")
    elif computer == 0 and you == -1 :
        print("You win and computer lose.")
    elif computer == 0 and you == 1 :
        print("Computer win and you lose.")
    else:
        print("It's a tie.")
    
    # Small logic
    #if computer - you == -1 or computer - you == 2:
    #    print("You lose")
    #else:
    #    print("You win")