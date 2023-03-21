import random


class Car:

    def __init__(self, brand, carType, color, mileage, worth, mass, horsepower):
        self.brand = brand
        self.carType = carType
        self.color = color
        self.mileage = mileage
        self.worth = worth
        self.mass = mass
        self.horsepower = horsepower

    def driveForward(self, distance):
        self.mileage = self.mileage + distance
        return "Obecny przebieg to {}".format(self.mileage)

    def repaint(self, paint):
        self.color = paint
        return "Przemalowano"

    def crash(self, predkosc):
        if predkosc > 50:
            loss = random.randrange(30,100)
            if loss < 50:
                loss = loss/100
                self.worth = self.worth*loss
                return "Wartość po stłuczce wynosi: {}".format(self.worth)
            else:
                self.worth = 0
                return "Samochód nadaje się tylko do kasacji"
        else:
            loss = random.randrange(0,50)
            if loss < 50:
                loss = loss/100
                self.worth = self.worth*loss
                return "Wartość po stłuczce wynosi: {}".format(self.worth)
            else:
                self.worth = 0
                return "Samochód nadaje się tylko do kasacji"

    def weightReduction(self, effectiveness):
        self.mass = self.mass*(effectiveness/100)
        return "Nowa waga to: {}".format(self.mass)

    def upgrade(self,effectiveness):
        self.horsepower = self.horsepower + self.horsepower*(effectiveness/100)
        return "Nowa moc samochodu to {}".format(self.horsepower)

    def checkStats(self):
        return "Marka: {}, rodzaj: {}, kolor: {}, przebieg: {}, wartość: {}, waga: {}, moc: {}".format(self.brand, self.carType, self.color, self.mileage, self.worth, self.mass, self.horsepower)

Car1 = Car("Ferrari" ,"Kabriolet" ,"czerwony",58473,60000,329,280)
Car2 = Car("Lamborghini","Kabriolet","żółty",232346,65000,270,247)
Car3 = Car("Honda","Hatchback","srebrny",5423561,2500,300,135)
Car4 = Car("Volkswagen","Hatchback","czarny",240315,10000,345,170)
Car5 = Car("Mazda","Coupe","srebrny",804523,11500,250,170)

print(Car5.repaint("niebieski"))

print(Car5.checkStats())

