class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract(cls, date):
        my_date = []
        for i in date.split():
            if i != "-":
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return f"Все данные введены верно, указанная дата: {(day, month, year)}"
                else:
                    return "Вы неверно указали год"
            else:
                return "Вы неверно указали месяц"
        else:
            return "Вы неверно указали день"

    def __str__(self):
        return f"Указанная дата: {Date.extract(self.date)}"


today = Date("5 - 1 - 2022")
print(today)
print(Date.valid(9, 8, -98))
print(Date.extract("9 - 12 - 2021"))
print(Date.valid(35, 6, 2000))
print(Date.valid(9, 8, 2010))