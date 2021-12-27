with open("text_2.txt", encoding="utf-8") as f:
    line = f.readlines()
    for index, value in enumerate(line, 1):
        words = len(value.split())
        print(f"В {index} строке {words} слов")
