class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(map(lambda arg: '   '.join(map(str, arg)), self.matrix)) + "\n"

    def __add__(self, other):
        return Matrix(map(lambda arg_1, arg_2: map(lambda a, b: a + b, arg_1, arg_2), self.matrix, other.matrix))


m_1 = Matrix([[4, 5, 6], [1, 2, 3], [7, 8, 9]])
m_2 = Matrix([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
print("Первая матрица\n")
print(m_1)
print("Вторая матрица\n")
print(m_2)
summa = m_1 + m_2
print("Сумма матриц\n")
print(summa)
