# Program: CTI-110-0004
# P5LAB3 - Quiz Show
# delrosab1153
# Tue 11/7/2023

import random

def quiz_game():
    print("Welcome to the Economics Quiz Game!")
    print("-----------------------------------")
    
    score = 0
    
    question_set = {
      "What is the study of how societies allocate scarce resources?": "economics",
      "Who is often referred to as the father of modern economics (last name only)?": "smith",
      "What is the primary measure of a country's economic output?": "gdp",
      "What is the term for a situation where demand exceeds supply?": "shortage",
      "What economic system emphasizes voluntary exchange, private property, and property rights?": "capitalism",
      "As price increases, quantity increases. This refers to the economic law of what?": "supply",
      "As price increases, quantity decreases. This refers to the economic law of what?": "demand",
      "What economic system encourages stealing from those who produce to redistribute to those who do not produce?": "socialism",
    }
    
    questions = random.sample(question_set.keys(), 5)
    count = 1
    for question in questions:
        answer = input(f'\n({count}) {question} ')
        if answer.lower() == question_set[question]:
            score += 1
            count += 1
            print("\n  Correct!")
        else:
            count += 1
            print("\n  Incorrect.")
    
    print("\nQuiz completed! Your total score is:", score, "out of", len(questions))

quiz_game()