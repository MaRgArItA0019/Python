import json

with open("text_77.json", "w", encoding="utf-8") as j:
    with open("text_7.txt", encoding="utf-8") as f:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
        average_profit = [profit, {"Средняя прибыль": round(sum([int(i) for i in
                                                                 profit.values() if int(i) > 0]) / len([int(i) for i
                                                                                                        in
                                                                                                        profit.values()
                                                                                                        if
                                                                                                        int(i) > 0]))}]
    json.dump(average_profit, j, ensure_ascii=False, indent=4)
