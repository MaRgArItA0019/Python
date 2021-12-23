from itertools import count, cycle

my_count = count(1)
my_cycle = cycle("MONTH")
for _ in range(10):
    print("(Первый список, Второй список = ({}, {})".format(next(my_count), next(my_cycle)))