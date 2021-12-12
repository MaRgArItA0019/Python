# Решение через list:

season_list = ["зима", "весна", "лето", "осень"]
month = int(input("Введите номер месяца года от 1 до 12: "))
if month == 1 or month == 2 or month == 12:
    print("Данный номер месяца относится ко времени года: ", season_list[0])
elif month == 3 or month == 4 or month == 5:
    print("Данный номер месяца относится ко времени года: ", season_list[1])
elif month == 6 or month == 7 or month == 8:
    print("Данный номер месяца относится ко времени года: ", season_list[2])
elif month == 9 or month == 10 or month == 11:
    print("Данный номер месяца относится ко времени года: ", season_list[3])
else:
    print("Месяца под таким номером не существует. Попробуйте ввести еще раз номер месяца от 1 до 12.")

# Решение через dict:

season_dict = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
month = int(input("Введите номер месяца года от 1 до 12: "))
if month == 1 or month == 2 or month == 12:
    print("Данный номер месяца относится ко времени года: ", season_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print("Данный номер месяца относится ко времени года: ", season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print("Данный номер месяца относится ко времени года: ", season_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print("Данный номер месяца относится ко времени года: ", season_dict.get(4))
else:
    print("Месяца под таким номером не существует. Попробуйте ввести еще раз номер месяца от 1 до 12.")