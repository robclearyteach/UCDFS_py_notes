"""
Write a program to teach a first grade child how to learn subtractions. 
The program randomly generates two single-digit integers 
number1 and number2 (with number1 >= number2) and 
displays a question such as 
“What is 9 – 2?” to the student. 

After the student types the answer, the program displays a message 
to indicate whether the answer is correct.
"""
import random

# 1. Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
    number1, number2 = number2, number1 # Simultaneous assignment

# 4. Prompt the student to answer "what is number1 - number2?"
answer = int(input("What is " + str(number1) + " - " + 
    str(number2) + "? "))

# 4. Grade the answer and display the result
if number1 - number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.")
    print(number1, '-', number2, "is", number1 - number2)
