products = []
features = {'Наименование': '', 'Цена': '', 'Количество': '', 'Единицы измерения': ''}
analytics = {'Наименование': [], 'Цена': [], 'Количество': [], 'Единицы измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для того, чтобы продолжить нажмите 'C', чтобы выйти из программы нажмите 'Q',"
                    "чтобы посмотреть аналитику всех товаров списка нажмите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print("Аналитика всех товаров списка: ")
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for f in features.keys():
        feature_ = input(f'Введите "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    products.append((num, features))
print(my_analyt)