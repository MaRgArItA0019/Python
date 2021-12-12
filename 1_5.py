revenue = float(input("Введите значение прибыли фирмы: "))
costs = float(input("Введите значение издержек фирмы: "))
if revenue > costs:
    print("Фирма работает в плюс. Поздравляю!")
    profitability = f"{(revenue - costs) * 100 / revenue:.4f}"
    print("Прибыль фирмы: ", profitability, "%")
    office = int(input("Введите численность сотрудников фирмы: "))
    profitability = float(profitability)
    revenue_office = f"{profitability / office:.4f}"
    print("Прибыль фирмы в расчете на одного сотрудника: ", revenue_office, "%")
else:
    print("Фирма работает в минус. Это печально.")