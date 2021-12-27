file = open("text_1.txt", "w", encoding="utf-8")
line = " "
while line:
    line = input("Напишите что-то в файле, либо не пишите для закрытия файла: ")
    file.write(f"{line}\n") if line != " " else file.close()
