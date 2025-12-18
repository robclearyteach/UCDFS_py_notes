"""
Write a program that randomly generates an integer between 0 and 100, inclusive. 
The program prompts the user to enter a number continuously until the number matches 
the randomly generated number. For each user input, the program tells the user whether
the input is too low or too high, so the user can choose the next input intelligently. 
"""
#Without Loop
import random

# Generate a random number to be guessed
number = random.randint(0, 100)

print("Guess a magic number between 0 and 100")

# Prompt the user to guess the number
guess = int(input("Enter your guess: "))

if guess == number:
    print("Yes, the number is " + str(number))
elif guess > number:
    print("Your guess is too high")
else:
    print("Your guess is too low")


#With Loop

# import random

# # Generate a random number to be guessed
# number = random.randint(0, 100)

# print("Guess a magic number between 0 and 100")

# guess = -1
# while guess != number:
#     # Prompt the user to guess the number
#     guess = int(input("Enter your guess: "))

#     if guess == number:
#         print("Yes, the number is", number)
#     elif guess > number:
#         print("Your guess is too high")
#     else:
#         print("Your guess is too low")
