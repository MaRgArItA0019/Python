rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4_1.txt", "w", encoding="utf-8") as new_file:
    with open("text_4.txt", encoding="utf-8") as old_file:
        new_file.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in old_file])
