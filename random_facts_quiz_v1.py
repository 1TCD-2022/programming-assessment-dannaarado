"""
Filename: random_facts_quiz_v1.py
Author: Danna Arado
Date: 27/6/2022
Description: This is a program quiz
which generates random fact questions
"""
import random

#These are random fact quiz questions and their respective answers
FACT_QUESTIONS = ["What is the largest human organ?", "What element is the chemical symbol Sn?",
                  "What is the smallest planet in our solar system?", "What kind of food is Penne?",
                  "What is the capital city of Spain?", "What language is spoken in Brazil?",
                  "Where is the smallest bone in the human body located?"]
FACT_ANSWERS = ["Skin", "Tin", "Mercury", "Pasta", "Madrid", "Portuguese", "Ear"]

#To make the code loop
user_repeat = True

#introduction
print ("Hello, this is a random fact quiz, for general knowledge enjoyers.")


while user_repeat:
    #doesn't crash code if ValueError
    try:
            
        number_of_questions = int(input ("How many questions do you want to answer between 1-7: "))
        #range within the number of questions
        if number_of_questions in range (0, 8):

            #check if in range
            for question_count in range(number_of_questions):
                
                #randomly generate questions
                randomly_generated_question = random.choice(FACT_QUESTIONS)
                user_answer = input(randomly_generated_question)

                #tell user they are correct if they are
                if user_answer.title() == FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]:
                    print ("Correct")

                #tell user they are incorrent if they are and prints right answer
                elif user_answer.title() != FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]:
                    print ("Incorrect")
                    print ("The correct answer is {}".format(FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]))
                    
            #ask if user wants to repeat
            user_repeat_choice = input("""Please enter n if you don't want to play again
(enter anything else if you want to repeat): """)

            #user choose not to repeat "n"
            if user_repeat_choice.lower() == "n":
                user_repeat = False
                print ("Thank you for playing")
                
        #invalid input doesn't crash code
        else:
            print ("Please enter a valid number (1-7)")

    except ValueError:
        print("Please enter a valid option")
