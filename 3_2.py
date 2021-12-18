def inform(**kwargs):
    return ' '.join(kwargs.values())


print(inform(name=input("Введите ваше имя: "), surename=input("Введите вашу фамилию: "),
             birthday=input("Введите дату вашего рождения: "), city=input("Введите город проживания: "),
             email=input("Введите вашу почту: "), telephone=input("Введите ваш телефон: ")))
