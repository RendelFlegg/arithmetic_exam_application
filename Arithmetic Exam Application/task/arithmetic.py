import random


def evaluate(x, operator, y):
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    else:
        result = x * y
    return result


def get_correct_answer_lvl1():
    first_number = random.randint(2, 9)
    second_number = random.randint(2, 9)
    oper = random.choice(['+', '-', '*'])
    print(first_number, oper, second_number)
    return evaluate(first_number, oper, second_number)


def get_correct_answer_lvl2():
    first_number = random.randint(11, 29)
    print(first_number)
    return first_number ** 2


def check_result(result, answer):
    global score
    if result == answer:
        print('Right!')
        score += 1
        return True
    else:
        print('Wrong!')
        return False


def task(level):
    if level == '1':
        correct_answer = get_correct_answer_lvl1()
    else:
        correct_answer = get_correct_answer_lvl2()
    while True:
        try:
            user_answer = int(input())
            check_result(correct_answer, user_answer)
            break
        except ValueError:
            print('Incorrect format.')


def choose_level():
    while True:
        print('Which level do you want? Enter a number:')
        for key in level_dictionary:
            print(f'{key} - {level_dictionary[key]}')
        level = input()
        if level in level_dictionary:
            return level
        print('Incorrect format.')


def saving_result():
    print('Would you like to save your result to the file? Enter yes or no.')
    answer = input()
    if answer in ['yes', 'YES', 'y', 'Yes']:
        return True
    return False


level_dictionary = {'1': 'simple operations with numbers 2-9',
                    '2': 'integral squares of 11-29'}

score = 0

user_level = choose_level()

for _ in range(5):
    task(user_level)
exam_result = f'{score}/5'
print(f'Your mark is {exam_result}')

if saving_result():
    user_name = input("What's your name?\n")
    with open('results.txt', 'a') as results_file:
        results_file.write(f'{user_name}: {exam_result} in level {user_level} ({level_dictionary[user_level]}).')
    print('The results are saved in "results.txt".')
