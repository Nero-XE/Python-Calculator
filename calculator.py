#coding: utf-8

def calculate(num1, num2, act):
    res = 0
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Не удалось преобразовать одну из переменных, так как она не является числом"
    match act:
        case '+':
            res = num1 + num2
        case '-':
            res = num1 - num2
        case '*':
            res = num1 * num2
        case '/':
            res = num1 / num2
        case '':
            return "Вы не ввели действие"
        case _: 
            return "Вы ввели не действие"
    if res % 1 == 0:
        res = int(res)
    return res

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
act = input("Введите действие: ")

print(f'Ответ: {calculate(num1, num2, act)}')