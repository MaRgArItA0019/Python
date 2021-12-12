my_list_count = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
while i < my_list_count:
    my_list.append(input("Введите значение элемента списка: "))
    i += 1
print("Ваш список: ", my_list)
k = 0
for i in range(int(len(my_list)/2)):
    my_list[k], my_list[k+1] = my_list[k+1], my_list[k]
    k += 2
print("После смены индексов элементов списка: ", my_list)