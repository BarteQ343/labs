import math

print("\n\nZadanie 1\n\n")

class pojazd:

    def __init__(self, typ, szybkość):
        self.typ = typ
        self.nr_tablica = None
        self.szybkość = szybkość

    def drive(self):
        print("Jedziemy ",self.typ," z prędkością:", self.szybkość)

    def __del__(self):
        print(self.typ, "się rozbił")

class samochód(pojazd):

    def __init__(self, szybkość):
        super().__init__("samochód", szybkość)

    def brake(self):
        print("Hamuj ten", self.typ, "sarna!")

class motocykl(pojazd):

    def __init__(self, szybkość):
        super().__init__("motocykl", szybkość)

    def brake(self):
        print("Hamuję z prędkości", self.szybkość)

mazda = samochód(120)
mazda.drive()
mazda.brake()

yamaha = motocykl(90)
yamaha.drive()
yamaha.brake()


print("\n\nZadanie 2\n\n")

class Zwierzę:

    def __init__(self, gatunek, sen):
        self.gatunek = gatunek
        self.sen = sen

    def sleep(self):
        print(self.gatunek," śpi ",self.sen, "godzin dziennie")


class kot(Zwierzę):

    def __init__(self, sen):
        super().__init__("kot", sen)

    def attack(self):
        print(self.gatunek, "szykuje się do ataku")

    def pets(self):
        print(self.gatunek, "łasi się")

class pies(Zwierzę):

    def __init__(self, sen):
        super().__init__("pies", sen)

    def attack(self):
        print(self.gatunek, "szykuje się do ataku")

    def pets(self):
        print(self.gatunek, "łasi się")

class ptak(Zwierzę):

    def __init__(self, sen, szybkość):
        super().__init__("ptak", sen)
        self.szybkość = szybkość

    def attack(self):
        print(self.gatunek, "szykuje się do ataku")

    def fly(self):
        print(self.gatunek, "leci z prędkością", self.szybkość)

class ryba(Zwierzę):

    def __init__(self, sen, szybkość):
        super().__init__("ryba", sen)
        self.szybkość = szybkość

    def swim(self):
        print(self.gatunek, "płynie z prędkością", self.szybkość)

PuszekOkruszek = kot(10)
PuszekOkruszek.attack()
PuszekOkruszek.sleep()

Szarik = pies(6)
Szarik.pets()
Szarik.sleep()

Tweety = ptak(4, 50)
Tweety.sleep()
Tweety.fly()

Bul = ryba(1, 15)
Bul.sleep()
Bul.swim()


print("\n\nZadanie 3\n\n")


class Figura:
    def oblicz_obwod(self):
        pass

    def oblicz_pole(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_obwod(self):
        return 4 * self.bok

    def oblicz_pole(self):
        return self.bok * self.bok

class Prostokat(Figura):
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b

    def oblicz_obwod(self):
        return 2 * (self.bok_a + self.bok_b)

    def oblicz_pole(self):
        return self.bok_a * self.bok_b

class Trojkat(Figura):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def oblicz_obwod(self):
        return 3 * self.podstawa

    def oblicz_pole(self):
        return 0.5 * self.podstawa * self.wysokosc

class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_obwod(self):
        return 2 * math.pi * self.promien

    def oblicz_pole(self):
        return math.pi * self.promien * self.promien

class Romb(Figura):
    def __init__(self, przekatna_a, przekatna_b):
        self.przekatna_a = przekatna_a
        self.przekatna_b = przekatna_b

    def oblicz_obwod(self):
        return 2 * math.sqrt(self.przekatna_a ** 2 + self.przekatna_b ** 2)

    def oblicz_pole(self):
        return 0.5 * self.przekatna_a * self.przekatna_b

class Trapez(Figura):
    def __init__(self, podstawa_a, podstawa_b, wysokosc):
        self.podstawa_a = podstawa_a
        self.podstawa_b = podstawa_b
        self.wysokosc = wysokosc

    def oblicz_obwod(self):
        return self.podstawa_a + self.podstawa_b + 2 * math.sqrt(((self.podstawa_a - self.podstawa_b) / 2) ** 2 + self.wysokosc ** 2)

    def oblicz_pole(self):
        return 0.5 * (self.podstawa_a + self.podstawa_b) * self.wysokosc



