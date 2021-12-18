def my_func(arg_1, arg_2, arg_3):
    try:
        my_list = [int(arg_1), int(arg_2), int(arg_3)]
        my_list.remove(min(my_list))
        return sum(my_list)
    except ValueError:
        return "Пожалуйста, введите числа"


print(my_func(input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")))