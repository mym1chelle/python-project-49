# Game even or odd number
import random


def even_or_not():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = random.randint(1, 20)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return description, question, correct_answer
