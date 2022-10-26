# Game "Finding the greatest common divisor"
import random


def greatest_common_divisor():
    description = 'Find the greatest common divisor of given numbers.'
    first_number = random.randint(1, 30)
    second_number = random.randint(1, 30)
    question = f'{first_number} {second_number}'

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number

    correct_answer = str(first_number + second_number)
    return description, question, correct_answer
