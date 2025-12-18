"""
Write a program that randomly generates a 2-digit
 lottery number between 0 and 99
and prompts the user to guess the number 
The program determines whether the user 
wins according to the following rules:

If the user input matches the lottery numbers in order, the award is $10,000.
If the user input matches the lottery in any order the award is $3,000.
If one digit in the user input matches any single digit, the award is $1,000.
"""

import random

# Generate a random number

#FOR TESTING: Manually setting a guessable number but replace for random
lottery = 42
print("THE TEST NUMBER IS 42")
# lottery = random.randint(0, 99)


# Prompt the user to enter a guess
guess = int(input("Enter your lottery pick (two digits): "))

# Get digits from lottery
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

# Get digits from guess
guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is", lottery)

# Check the guess
if guess == lottery:
    print("Exact match: you win $10,000")
elif (guessDigit2 == lotteryDigit1 and \
  guessDigit1 == lotteryDigit2):
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1 
        or guessDigit1 == lotteryDigit2 
        or guessDigit2 == lotteryDigit1 
        or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")
