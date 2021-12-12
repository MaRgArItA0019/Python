string = input("Введите строку из нескольких слов через пробел: ")
string = string.split()
for ind, el in enumerate(string, 1):
    if len(str(string)) > 10:
        print(f"{ind} {el[0:10]}")
    else:
        print(ind, el)