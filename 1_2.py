time = int(input("Введите время в секундах: "))
a = time // 60
c = time - (a * 60)
b = 0
while a >= 60:
    a = a-60
    b += 1
print(f"Время в формате чч:мм:сс   {b} : {a} : {c}")