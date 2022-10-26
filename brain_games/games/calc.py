# Game 'calculator'
import random


def calculator():
    description = 'What is the result of the expression?'
    first_number = random.randint(1, 30)
    second_number = random.randint(1, 10)
    symbol = random.choice(['+', '-', '*'])
    question = f'{first_number} {symbol} {second_number}'
    correct_answer = str(eval(question))
    return description, question, correct_answer
