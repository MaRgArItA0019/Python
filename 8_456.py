class Warehouse:
    def __init__(self):
        self.my_warehouse_full = []
        self.my_warehouse = []

    def reception(self):
        while True:
            try:
                unit = input("Введите наименование: ")
                unit_p = int(input("Введите цену за ед: "))
                unit_q = int(input("Введите количество: "))
                unique = {f"Модель устройства ": unit, "Цена за ед ": unit_p, "Количество ": unit_q}
                self.my_warehouse.append(unique)
                self.my_warehouse_full.append(unique)
                print(self.my_warehouse)
                yes_or_no = input("Хотите ввести еще число в список? Y/N ")
                if yes_or_no == "Y" or yes_or_no == "y":
                    print(try_except.reception())
                elif yes_or_no == "N" or yes_or_no == "n":
                    return f"Финальный список: {self.my_warehouse_full}\nВы вышли из программы, до встречи"
                else:
                    return "Вы ввели непонятное значение и вышли из программы"
                break
            except ValueError:
                print(f"Ошибка ввода данных\nДля выхода - Q, продолжение - E")
                q = input(f"\n---> ")
                if q == "E" or q == "e":
                    return Warehouse.reception(self)
                elif q == 'Q' or q == 'q':
                    return f"Весь склад -\n {self.my_warehouse_full}\nВы вышли из программы"
                else:
                    return "Вы ввели непонятное значение и вышли из программы"


class Machines:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_unit = {"Модель устройства": self.name, "Цена за ед": self.price, "Количество": self.quantity}

    def __str__(self):
        return f"{self.my_unit}"


class Printer(Machines):
    @staticmethod
    def to_print(numb):
        return f"Печатает {numb} лист(ов) в минуту"


class Scanner(Machines):
    @staticmethod
    def to_scan(numb):
        return f"Сканирует {numb} лист(ов) в минуту"


class Copier(Machines):
    @staticmethod
    def to_copier(numb):
        return f"Копирует {numb} лист(ов) в минуту"


try_except = Warehouse()
print(try_except.reception())
print(Machines("HP", 5000, 2))
print(Printer.to_print(10))
