from abc import ABC, abstractmethod


class Clothes(ABC):
    instance = []

    def __init__(self, par):
        self.par = par
        Clothes.instance.append(self)

    @abstractmethod
    def consumption(self):
        pass

    def __del__(self):
        if self in Clothes.instance:
            Clothes.instance.remove(self)


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.par / 6.5 + 0.5)


class Costume(Clothes):
    @property
    def consumption(self):
        return round(self.par * 2 + 0.3)


coat_1 = Coat(44)
costume_1 = Costume(150)
costume_2 = Costume(200)

total_consumption = 0
for wear in Clothes.instance:
    total_consumption += wear.consumption
print(f"Общий расход ткани: {total_consumption}")
coat_1.__del__()

total_consumption = 0
for wear in Clothes.instance:
    total_consumption += wear.consumption
print(f"Общий расход ткани: {total_consumption}")

