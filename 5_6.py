my_dict = {}
with open("text_6.txt", encoding="utf-8") as f:
    for line in f:
        name, values = line.split(":")
        summa = sum(map(int, "".join([i for i in values if i == " " or "0" <= i <= "9"]).split()))
        my_dict[name] = summa
print(my_dict)
