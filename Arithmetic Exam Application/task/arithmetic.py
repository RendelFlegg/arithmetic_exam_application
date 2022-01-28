import random


def evaluate(x, operator, y):
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    else:
        result = x * y
    return result


def get_correct_answer():
    first_number = random.randint(2, 9)
    second_number = random.randint(2, 9)
    oper = random.choice(['+', '-', '*'])
    print(first_number, oper, second_number)
    return evaluate(first_number, oper, second_number)


def check_result(result, answer):
    global score
    if result == answer:
        print('Right!')
        score += 1
        return True
    else:
        print('Wrong!')
        return False


def task():
    correct_answer = get_correct_answer()
    while True:
        try:
            user_answer = int(input())
            check_result(correct_answer, user_answer)
            break
        except ValueError:
            print('Incorrect format.')


score = 0

for _ in range(5):
    task()
print(f'Your mark is {score}/5')
