class House:

    houses_history = []

    @classmethod
    def new(cls, *args):
        house = cls(*args)
        return house

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        House.houses_history.append(self.name)

    def __str__(self):
        return f"{self.name} с {self.floors} этажами"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, int):
            return House(self.name, self.floors + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.floors += other
            return self
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        return NotImplemented



h1 = House.new('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House.new('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House.new('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

del h2
del h3

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']