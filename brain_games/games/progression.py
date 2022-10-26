# Game "Arithmetic progression"
import random


def arithmetic_progression():
    description = 'What number is missing in the progression?'
    step_progression = random.randint(1, 30)
    length_progression = random.randint(5, 15)
    progression = []
    start = random.randint(1, 30)
    for _ in range(length_progression):
        progression.append(str(start))
        start += step_progression

    hidden_number_index = random.randint(0, length_progression - 1)
    correct_answer = progression[hidden_number_index]
    progression[hidden_number_index] = '..'
    question = ' '.join(progression)
    return description, question, correct_answer
