# multiplication-quiz.py
# Description: Generates a timed quiz with multiplication questions, limiting the user to three tries per question
# and eight seconds to respond. Tracks the number of correct answers out of a set number of questions.

import pyinputplus as pyip
import time
import random

# Initialize the count of correct answers and set the total number of questions
correct_answers = 0
number_of_questions = 10

# Loop through each question, generating random numbers and calculating the correct answer
for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    correct_answer = num1 * num2

    tries = 0  # Track the number of tries for each question

    while tries < 3:  # Allow up to 3 attempts per question
        try:
            # Prompt the user for their answer, with an 8-second time limit
            user_input = pyip.inputNum(prompt=f'Question #{question_number + 1}: {num1} x {num2} = ?\n', timeout=8)
            if user_input == correct_answer:
                print('Correct!')
                correct_answers += 1  # Increment the count of correct answers
                break  # Move on to the next question
            else:
                print('Incorrect! Try again.')
                tries += 1  # Increment the attempt counter

        except pyip.TimeoutException:
            print('Out of time! Moving on to the next question...')
            break  # Move on to the next question after a timeout

        except pyip.ValidationException:
            print('Invalid input! Please enter a number.')
            tries += 1  # Increment the attempt counter for invalid inputs

    time.sleep(1)  # Brief pause before moving on to the next question

# Print the final score
print(f"You answered {correct_answers} out of {number_of_questions} questions correctly.")
