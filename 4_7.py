def my_func(number):
    num = 1
    for i in range(number + 1):
        yield f"{i}! = {num}"
        num *= i + 1


for el in my_func(int(input("Введите число, чтобы вычислить факториал: "))):
    print(el)