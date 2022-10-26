# Common logic for all games
import prompt


def common_games_logic(function):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    description, _, _ = function()
    print(description)
    number_question = 0

    while number_question != 3:
        _, question, correct_answer = function()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            number_question += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    if number_question == 3:
        print(f'Congratulations, {name}')
