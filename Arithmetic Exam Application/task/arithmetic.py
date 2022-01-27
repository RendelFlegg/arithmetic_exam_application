# write your code here
x, operator, y = input().split()
if operator == '+':
    print(int(x) + int(y))
elif operator == '-':
    print(int(x) - int(y))
elif operator == '*':
    print(int(x) * int(y))
elif operator == '/':
    print(int(x) / int(y))
