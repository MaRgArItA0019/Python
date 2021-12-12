products = []
while input("Хотите добавить товар в список? Напишите да/нет: ") == 'да':
    number = int(input("Введите номер товара : "))
    features = {}
    while input("Хотите ввести параметры для продукта? Напишите да/нет: ") == 'да':
        feature_key = input("Напишите название товара: ")
        feature_value = input("Напишите цену товара: ")
        feature_quantity = input("Введите количество товара: ")
        feature_unit = input("Введите единицы измерения товара (ед., шт.): ")
        features[feature_key] = feature_value, feature_quantity, feature_unit
    products.append(tuple([number, features]))
print(products)
analitics = {}
for product in products:
    for feature_key, feature_value in product[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
            analitics[feature_key] = [feature_value]
            print("Аналитика всех товаров списка: ")
for key, value in analitics.items():
     print(f'{key}: {value}')
for f in feature_key():
    feature_ = input({f})
    feature[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
    analytics[f].append(feature[f])
    products.append((num, feature))
print(analitics)