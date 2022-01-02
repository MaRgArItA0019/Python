class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, row):
        return "\n".join(["₪" * row for _ in range(self.num // row)]) + "\n" + "₪" * (self.num % row)

    def __str__(self):
        return self.num

    def __add__(self, other):
        print("Сумма клеток: ")
        return Cell(self.num + other.num)

    def __sub__(self, other):
        print("Вычитание клеток: ")
        return Cell(self.num - other.num) if self.num - other.num > 0 \
            else "Невозможно вычесть ячейки первой клетки из второй, так как у первой клетки меньше ячеек"

    def __mul__(self, other):
        print("Умножение клеток: ")
        return Cell(self.num * other.num)

    def __floordiv__(self, other):
        print("Деление клеток: ")
        return Cell(self.num // other.num)


cell_1 = 50
cell_2 = 35
print("Сложение клеток: ", cell_1 + cell_2)
print("Вычитание клеток: ", cell_1 - cell_2)
print("Умножение клеток: ", cell_1 * cell_2)
print("Целочисленное деление клеток: ", cell_1 // cell_2)