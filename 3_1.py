def func(var_1, var_2):
    try:
        var_1, var_2 = int(var_1), int(var_2)
        my_func = var_1 / var_2
    except ValueError:
        return "Введите число"
    except ZeroDivisionError:
        return "Деление на ноль невозможно"
    return round(my_func, 2)


print(func(input("Введите первое число: "), input("Введите второе число: ")))
