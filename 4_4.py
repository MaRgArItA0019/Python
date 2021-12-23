from random import randint

my_list = [randint(10, 40) for _ in range(10)]
el_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Список исходных чисел\n{my_list}\nNСписок неповторяющихся чисел\n{el_list}")