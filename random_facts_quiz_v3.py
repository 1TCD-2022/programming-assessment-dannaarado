"""
Filename: random_facts_quiz_v1.py
Author: Danna Arado
Date: 27/6/2022
Description: This is a program quiz
which generates random fact questions
"""
import random

# These are random fact quiz questions and their respective answers
FACT_QUESTIONS = [
    "What is the largest human organ?",
    "What element is the chemical symbol Sn?",
    "What is the smallest planet in our solar system?",
    "What kind of food is Penne?",
    "What is the capital city of Spain?",
    "What language is spoken in Brazil?",
    "Where is the smallest bone in the human body located?",
    "What continent would you find the world's largest desert on?",
    "Which mammal lays eggs, is venomous, has a bill and can swim?",
    "What fear is barophobia of?",
    "Name the liquid produced by flowers to attract insects?",
    "What is the national bird of India?"]
FACT_ANSWERS = [
    "Skin", "Tin", "Mercury", "Pasta", "Madrid", "Portuguese", "Ear",
    "Antartica", "Platypus", "Gravity", "Nectar", "Peacock"]

# Scoring
score = 0

# To make the code loop
user_repeat = True

# Introduction and menu options
print ("""Hello, this is a random fact quiz, for general knowledge enjoyers.
       Menu options
        1. Generate general knowledge questions
        2. Generate a random fact
        3. Current score
        4. Exit""")

while user_repeat:
    # Doesn't crash code if ValueError
    try:
        user_menu_choice = int(input("""Choose a menu option.
Enter 1, 2, 3 or 4: """))
        # \n makes blank space in program for readability
        print ("\n")

        # Generates depending on user menu choice
        if user_menu_choice == 1:
            number_of_questions = int(input("""How many questions do you want to
answer between 1-12: """))
            print ("\n")

            # Range within the number of questions
            if number_of_questions in range(1, 13):

                # Check if within range
                for question_count in range(number_of_questions):

                    # Randomly generate questions
                    # .capitaliize() and .strip() to prevent crashing
                    randomly_generated_question = random.choice(FACT_QUESTIONS)
                    user_answer = input(randomly_generated_question).strip()

                    # Tells user they are correct if they are
                    if user_answer.capitalize() == FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]:
                        print ("Correct \n")
                        score += 1
                        print ("Current score: {} \n".format(score))

                    # Tells user they are incorrect if they are
                    # Prints right answer
                    elif user_answer.capitalize() != FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]:
                        print ("Incorrect \n")
                        print ("The correct answer is {} \n".format(
                            FACT_ANSWERS[FACT_QUESTIONS.index(
                                randomly_generated_question)]))
                        print ("Current score: {} \n".format(score))

                # Ask if user wants to repeat
                user_repeat_choice = input("""Please enter n if you don't want to play again
(enter anything else if you want to repeat): """)
                print ("\n")

                # User choose not to repeat "n" stops program
                # .lower() and .strip() to prevent code crashing
                if user_repeat_choice.lower().strip() == "n":
                    user_repeat = False
                    print ("Thank you for playing")

            # Invalid input doesn't crash code
            else:
                print ("Please enter a valid number (1-12)", "\n")

        # Menu option 2
        elif user_menu_choice == 2:

            # Print randomly generated quesiton
            randomly_generated_question = random.choice(FACT_QUESTIONS)
            print ("""{} \n
Answer is: {} \n""".format(randomly_generated_question, FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]))

            user_repeat_choice = input("""Please enter n if you don't want to play again
(enter anything else if you want to repeat): """)
            print ("\n")

            # User choose not to repeat "n"
            if user_repeat_choice.lower().strip() == "n":
                user_repeat = False
                print ("Thank you for playing")

        # Print user's current score if menu option 3 chosen
        elif user_menu_choice == 3:
            print ("You current total score is {} \n".format(score))

        # Exits and ends program if menu option 4 chosen
        elif user_menu_choice == 4:
            user_repeat = False
            print ("Thank you for playing")

        else:
            print ("Invalid menu option \n")

    except ValueError:
        print("Please enter a valid option \n")
