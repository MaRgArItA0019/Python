first_day = int(input("Введите сколько километров пробежал спортсмен в первый день: "))
last_day = int(input("Введите сколько километров должен пробежать спортсмен для достижения результата: "))
day = 1
while first_day < last_day:
    day += 1
    first_day = first_day + (first_day * 10 / 100)
print("Спортсмен пробежит не менее ", last_day, "км к ", day, "дню")