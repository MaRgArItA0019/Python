with open("text_3.txt", "r", encoding="utf-8") as f:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f"Список сотрудников, которые получают зарплату в размере менее 20 тыс. = "
          f"{[i[0] for i in my_dict.items() if i[1] < 20000]}\n"
          f"Средняя величина дохода сотрудников = {round(sum(my_dict.values()) / len(my_dict), 2)}")
