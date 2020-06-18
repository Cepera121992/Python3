# Первое решение:
# def my_func():
#     x = int(input('Введите положительное число: '))
#     y = int(input('Введите отрицательное число: '))
#     my_pow = x ** y
#     return my_pow
#
#
# print(my_func())

# Второе решение:

def my_func():
    x = int(input('Введите положительное число: '))
    y = int(input('Введите отрицательное число: '))
    i = 0
    while (i != y * -1):
        my_pow = (1 / x)
        i = i + 1
        my_pow_2 = my_pow * (1 / i)
    else:
        return my_pow_2


print(my_func())
