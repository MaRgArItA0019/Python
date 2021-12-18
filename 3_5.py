def sum_1():
    summa = 0
    while True:
        my_list = input("Введите число, для выхода введите q: ").split()
        for num in my_list:
            if num.lower() == "q":
                return f"Вы вышли из программы, сумма введенных до этого чисел равна: {summa}"
            else:
                try:
                    summa += int(num)
                except ValueError:
                    return "Для выхода введите q: "
        print(f"Сумма всех введенных чисел: {summa}")


print(sum_1())