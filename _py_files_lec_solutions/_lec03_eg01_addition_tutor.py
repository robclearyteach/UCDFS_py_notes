"""
Write a program to let a first grader practice additions. 

The program randomly generates two single-digit integers 
number1 and number2 and displays a question such as:
 “What is 7 + 9?” 
 to the student. 

After the student types the answer, 
the program displays a message to indicate whether the answer
is true or false
"""
import random 

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = int(input("What is " + str(number1) + " + " 
    + str(number2) + "? "))
    
# Display result    
print(number1, "+", number2, "=", answer, 
    "is", number1 + number2 == answer)
