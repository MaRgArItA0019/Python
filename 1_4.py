num = int(input("Введите положительное целое число: "))
remainder = num % 10
while remainder >= 1:
    num = num // 10
    if num % 10 > remainder:
        remainder = num % 10
    if num > 9:
        continue
    else:
        print("Самая большая цифра: ", remainder)
        break