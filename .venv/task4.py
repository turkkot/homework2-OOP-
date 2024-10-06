class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f'Toy Name: {self.name}, Color: {self.color}, Type: {self.toy_type}'

class ToyFactory:
    def create_toy(self, name, color, toy_type):
        self.purchase_materials()
        self.make_toy()
        self.paint_toy()
        print('Изготовлена новая игрушка')
        return Toy(name, color, toy_type)

    def purchase_materials(self):
        print("Закупка материалов")

    def make_toy(self):
        print("Пошив игрушки")

    def paint_toy(self):
        print("Покраска игрушки")

toyFactory = ToyFactory()
new_toy = toyFactory.create_toy("Милый кролик", "Белый", "Животное")
print(new_toy)