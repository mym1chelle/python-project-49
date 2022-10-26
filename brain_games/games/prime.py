# Game "Is it a prime number?"
import random


def prime_number_or_not():
    description = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'
    question = random.randint(1, 300)
    divider = 2
    while question % divider != 0:
        divider += 1
    if question == divider:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return description, question, correct_answer
