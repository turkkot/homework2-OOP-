class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} just started moving')

    def stop(self):
        print(f'{self.name} just stopped')

    def turn(self, direction):
        print(f'{self.name} just turned {direction}')


class SportCar:
    def __init__(self, speed, color, name, is_police, engine_power):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.engine_power = engine_power

    def go(self):
        print(f'{self.name} just started moving')

    def stop(self):
        print(f'{self.name} just stopped')

    def turn(self, direction):
        print(f'{self.name} just turned {direction}')

class WorkCar:
    def __init__(self, speed, color, name, is_police, capacity):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.capacity = capacity

    def go(self):
        print(f'{self.name} just started moving')

    def stop(self):
        print(f'{self.name} just stopped')

    def turn(self, direction):
        print(f'{self.name} just turned {direction}')


class PoliceCar:
    def __init__(self, speed, color, name, is_police, crew_number):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.crew_number = crew_number

    def go(self):
        print(f'{self.name} just started moving')

    def stop(self):
        print(f'{self.name} just stopped')

    def turn(self, direction):
        print(f'{self.name} just turned {direction}')