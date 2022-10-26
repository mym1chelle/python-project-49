# Game even or odd number
import prompt
import random


def even_or_not():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_question = 0

    while number_question != 3:
        question = random.randint(1, 20)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if (
            (answer == 'yes' and question % 2 == 0)
            or (answer == 'no' and question % 2 != 0)
        ):
            print('Correct!')
            number_question += 1

        elif answer == 'yes' and question % 2 != 0:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            break

        elif answer == 'no' and question % 2 == 0:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            break

        else:
            break

    if number_question == 3:
        print(f'Congratulations, {name}')
