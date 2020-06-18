# Неверное решение. Скажите, пожалуйста, почему при делении на ноль он сначала выводит, что на ноль делить нельзя, а если потом опять вводишь два числа, он в ответе пишет None?
# def division():
#     try:
#         first_number = float(input('Введите любое число: '))
#         second_number = float(input('Введите любое число: '))
#         answer = first_number / second_number
#         return answer
#     except ZeroDivisionError:
#         print('Делить на ноль нельзя!')
#         division()
#
#
# print(division())

def division():
    try:
        first_number = float(input('Введите любое число: '))
        second_number = float(input('Введите любое число: '))
        answer = first_number / second_number
        return answer
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')


print(division())