def my_func():
    f1 = int(input('Введите первое число: '))
    f2 = int(input('Введите второе число: '))
    f3 = int(input('Введите третье число: '))
    my_max = [f1, f2, f3]
    my_max_1 = max(my_max)
    result_my_max_1 = my_max.remove(my_max_1)
    my_max_2 = max(my_max)
    result_my_max_2 = my_max.remove(my_max_2)
    my_sum = my_max_1 + my_max_2
    return my_sum


print(my_func())


