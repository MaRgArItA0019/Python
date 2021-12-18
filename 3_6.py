def my_func():
    for word in input("Введите строку слов из маленьких латинских букв через пробел: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else "Вводите только маленькие латинские буквы")


my_func()