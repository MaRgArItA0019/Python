class Division:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return "Деление на ноль невозможно"


print(Division.divide_by_null(10, 100))
print(Division.divide_by_null(10, 0))
