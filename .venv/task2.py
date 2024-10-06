class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} just started moving')

    def stop(self):
        print(f'{self.name} just stopped')

    def turn(self, direction):
        print(f'{self.name} just turned {direction}')

class TownCar(Car):
    def __init__(self, speed, color, name, car_number):
        super().__init__(speed, color, name)
        self.car_number = car_number

    def getCarNumber(self):
        print(f'{self.name} has {self.car_number} car number')

class SportCar(Car):
    def __init__(self, speed, color, name, engine_power):
        super().__init__(speed, color, name)
        self.engine_power = engine_power

    def getEnginePower(self):
        print(f'{self.name} has {self.engine_power} h.p')

class WorkCar(Car):
    def __init__(self, speed, color, name, capacity):
        super().__init__(speed, color, name)
        self.capacity = capacity
    def getTrunkCapacity(self):
        print(f'{self.name} has {self.capacity} m3 trunk')

class PoliceCar(Car):
    def __init__(self, speed, color, name, crew_number):
        super().__init__(speed, color, name)
        self.crew_number = crew_number
    def getCrewNumber(self):
        print(f'{self.name} has {self.crew_number} crew number')

townCar = TownCar(40, "black", "Car1", "6MBV006")
townCar.go()
townCar.turn("left")
townCar.stop()
townCar.getCarNumber()
sportCar = SportCar(90, "red", "SportCar1", 280)
workCar = WorkCar(30, "white", "WorkCar1", 5)
policeCar = PoliceCar(60, "black", "PoliceCar1", 33)

sportCar.getEnginePower()
workCar.getTrunkCapacity()
policeCar.getCrewNumber()