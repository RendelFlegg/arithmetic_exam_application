import random


def evaluate(x, operator, y):
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    else:
        result = x * y
    return result


def check(result, user_input):
    if result == int(user_input):
        print('Right!')
    else:
        print('Wrong!')


first_number = random.randint(2, 9)
second_number = random.randint(2, 9)
oper = random.choice(['+', '-', '*'])

print(first_number, oper, second_number)
check(evaluate(first_number, oper, second_number), input())
