def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x == 0:
            return "Деление на ноль невозможно"
        elif x < 0 or y >= 0:
            return "Введите положительное целое число и отрицательную степень"
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f"Результат возведения числа в степень:  {round(result, 4)}"
    except ValueError:
        return "Введите, пожалуйста, числа"


print(my_func(input("Введите число: "), input("Введите степень числа: ")))