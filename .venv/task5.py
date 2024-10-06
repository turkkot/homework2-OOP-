class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type
    def __str__(self):
        return f'Toy Name: {self.name}, Color: {self.color}, Toy Type: {self.toy_type}'


class AnimalToy(Toy):
    def __init__(self, name, color, toy_type, is_tail):
        super().__init__(name, color, toy_type)
        self.is_tail = is_tail

    def __str__(self):
        return f'Toy Name: {self.name}, Color: {self.color}, Toy Type: {self.toy_type}, Is tail: {self.is_tail}'

class FruitToy(Toy):
    def __init__(self, name, color, toy_type, fruitType):
        super().__init__(name, color, toy_type)
        self.fruitType = fruitType

        def __str__(self):
            return f'Toy Name: {self.name}, Color: {self.color}, Toy Type: {self.toy_type}, Fruit Type: {self.fruitType}'

class ToyFactory:
    def create_toy(self, name, color, toy_type):
        self.purchase_materials()
        self.make_toy()
        self.paint_toy()
        print('Изготовлена новая игрушка')
        return Toy(name, color, toy_type)

    def create_toy(self, name, color, toy_type, is_tail):
        self.purchase_materials()
        self.make_toy()
        self.paint_toy()
        print('Изготовлена новая игрушка')
        return AnimalToy(name, color, toy_type, is_tail)

    def create_toy(self, name, color, toy_type, fruitType):
        self.purchase_materials()
        self.make_toy()
        self.paint_toy()
        print('Изготовлена новая игрушка')
        return FruitToy(name, color, toy_type, fruitType)

    def purchase_materials(self):
        print("Закупка материалов")

    def make_toy(self):
        print("Пошив игрушки")

    def paint_toy(self):
        print("Покраска игрушки")


toyFactory = ToyFactory()
new_animal_toy = toyFactory.create_toy("Милый кролик", "Белый", "Животное", 0)
print(new_animal_toy)
new_fruit_toy = toyFactory.create_toy("Веселое авакадо", "Зеленый", "Фрукт", "Авакадо")
print(new_fruit_toy)
