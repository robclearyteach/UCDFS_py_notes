"""
The Math subtraction learning tool program generates just one question
 for each run. You can use a loop to generate questions repeatedly. 
 This example gives a program that generates five questions and reports 
 the number of the correct answers after a student answers all five questions.

"""
import random                                               #to generate random numbers to subtract
import time                                                 #to be able to report time taken

# a variable to count the number of correct answers
correct_answer_count = 0
# a variable to count the number of questions
questions_attempted = 0

NUMBER_OF_QUESTIONS = 5                                         # Constant

startTime = time.time() # Get start time

while questions_attempted < NUMBER_OF_QUESTIONS:
    # 1. Generate two random single-digit integers
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # 2. If number1 < number2, swap number1 with number2


    # 3. Prompt the student to answer "what is number1 - number2?" 
    answer = int(input(f"What is {number1} - {number2}? "))


    # 5. Grade the answer and display the result
        # increment the 'correct_answer_count'
        # increment the 'questions_attempted'

    if number1 - number2 == answer:
        print("You are correct!")
    else:
        print("Your answer is wrong.\n", number1, "-",
            number2, "should be", (number1 - number2))

    questions_attempted += 1

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correct_answer_count, "out of", 
    NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
