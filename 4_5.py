from functools import reduce


def multiplication_list(arg_1, arg_2):
    return arg_1 * arg_2


my_list = [el for el in range(100, 1001, 2)]
print(f"Список четных чисел\n{my_list}\nПроизведение всех чисел списка\n{reduce(multiplication_list, my_list)}")
