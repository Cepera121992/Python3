def number_sum():
    number = input('Введите любые числа через пробел: ').split()
    for el in range(len(number)):
        my_sum = number[el] + my_sum
    return my_sum


print(number_sum())
