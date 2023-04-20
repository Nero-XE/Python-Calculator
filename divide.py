#coding: utf-8

def divide(num1, num2):
    res = 0
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Не удалось преобразовать одну из переменных, так как она не является числом"
    res = num1 / num2
    if res % 1 == 0:
        res = int(res)
    return res

num1 = input("Введите первое число для деления: ")
num2 = input("Введите второе число для деления: ")

print(f'Ответ: {divide(num1, num2)}')