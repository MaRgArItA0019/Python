my_list = [7, 5, 3, 3, 2]
print("Текущий рейтинг: ", my_list)
num = int(input("Введите новое число рейтинга (либо '0' для выхода): "))
while num != 0:
    c = my_list.count(num)
    for el in my_list:
        if c > 0:
            i = my_list.index(num)
            my_list.insert(i + c, num)
            break
        elif num > el:
            j = my_list.index(el)
            my_list.insert(j, num)
            break
        elif my_list[-1] > num:
            my_list.append(num)
    print(my_list)
    num = int(input("Введите следующее число (либо '0' для выхода): "))