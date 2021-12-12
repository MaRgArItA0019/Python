products = int(input("Введите количество товара: "))
n = 1
my_dict = []
my_list = []
my_analyt = {}
while n <= products:
    my_dict = dict({'Название': input("Введите название товара: "), 'Цена': input("Введите цену товара: "),
                    'Количество': input('Введите количество товара: '),
                    'Единицы измерения': input("Введите единицу измерения товара: ")})
    my_list.append((n, my_dict))
    n += 1
    my_analyt = dict(
        {'Название': my_dict.get('Название'), 'Цена': my_dict.get('Цена'), 'Количество': my_dict.get('Количество'),
         'Единицы измерения': my_dict.get('Единицы измерения')})
print(my_list)
