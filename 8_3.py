class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                num = int(input("Введите число и далее нажмите Enter для добавления его в список: "))
                self.my_list.append(num)
                print(f"Текущий список - {self.my_list}\n")
                yes_or_no = input("Хотите ввести еще число в список? Y/N ")
                if yes_or_no == "Y" or yes_or_no == "y":
                    print(try_except.my_input())
                elif yes_or_no == "N" or yes_or_no == "n":
                    return f"Финальный список: {self.my_list}\nВы вышли из программы, до встречи"
                else:
                    return "Вы ввели непонятное значение и вышли из программы"
                break
            except ValueError:
                print("Недопустимое значение")
                y_or_n = input("Попробовать еще раз? Y/N ")
                if y_or_n == "Y" or y_or_n == "y":
                    return try_except.my_input()
                elif y_or_n == "N" or y_or_n == "n":
                    return "Вы вышли"
                else:
                    return "Вы вышли"


try_except = Error()
print(try_except.my_input())
