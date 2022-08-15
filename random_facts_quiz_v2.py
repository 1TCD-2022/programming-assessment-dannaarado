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

#introduction and menu options
print ("""Hello, this is a random fact quiz, for general knowledge enjoyers.
       Menu options
        1. Generate general knowledge questions
        2. Generate a random fact
        3. Exit""")

while user_repeat:
    #doesn't crash code if ValueError
    try:
        user_menu_choice = int(input("Choose a menu option. Enter 1, 2, or 3: "))
        #Makes blank space in program for readability
        print ("\n")

        #Generate depending on user menu choice
        if user_menu_choice == 1:
            number_of_questions = int(input ("How many questions do you want to answer between 1-7: "))
            print ("\n")

            #range within the number of questions
            if number_of_questions in range (1, 8):

                #check if in range
                for question_count in range(number_of_questions):
                    
                    #randomly generate questions; .capitaliize() and .strip() to prevent crashing
                    randomly_generated_question = random.choice(FACT_QUESTIONS)
                    user_answer = input(randomly_generated_question).strip()

                    #tell user they are correct if they are
                    if user_answer.capitalize() == FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]:
                        print ("Correct \n")

                    #tell user they are incorrent if they are and prints right answer
                    elif user_answer.capitalize() != FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]:
                        print ("Incorrect \n")
                        print ("The correct answer is {} \n".format(FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]))
                        
                #ask if user wants to repeat
                user_repeat_choice = input("""Please enter n if you don't want to play again
    (enter anything else if you want to repeat): """)
                print ("\n")

                #user choose not to repeat "n", .lower() and .strip() to prevent code crashing
                if user_repeat_choice.lower().strip() == "n":
                    user_repeat = False
                    print ("Thank you for playing")
                    
            #invalid input doesn't crash code
            else:
                print ("Please enter a valid number (1-7)", "\n")

        #Menu option 2
        elif user_menu_choice == 2:
            
            #print randomly generated quesiton
            randomly_generated_question = random.choice(FACT_QUESTIONS)
            print ("""{} \n
Answer is: {} \n""".format(randomly_generated_question, FACT_ANSWERS[FACT_QUESTIONS.index(randomly_generated_question)]))

            user_repeat_choice = input("""Please enter n if you don't want to play again
(enter anything else if you want to repeat): """)
            print ("\n")

                #user choose not to repeat "n"
            if user_repeat_choice.lower().strip() == "n":
                user_repeat = False
                print ("Thank you for playing")
                    
        #Exit if Menu option 3
        elif user_menu_choice == 3:
            user_repeat = False
            print ("Thank you for playing")
        
        else:
            print ("Invalid menu option \n")

    except ValueError:
        print("Please enter a valid option")
