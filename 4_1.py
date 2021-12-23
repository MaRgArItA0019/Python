from sys import argv


def sal():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Заработная плата сотрудника - {time * rate + bonus}")
    except ValueError:
        print("Вводите только числа")


sal()