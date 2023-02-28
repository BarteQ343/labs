import math
'''
print("\nZadanie 1\n")


def obliczenia(a,b):
    print("Wynik dodawania: ", a+b)
    print("Wynik odejmowania: ", a-b)
    if b == 0 and a == 0:
        print("Dzielenie się nie uda (nie można dzielić przez 0)")
    elif b == 0 and a != 0:
        print("Wynik dzielenia: ", b/a)
    elif a == 0 and b != 0:
        print("Wynik dzielenia: ", a/b)
    else:
        print("Wyniki dzielenia to odpowiednio: ", a/b, " i ", b/a)
    print("Wynik mnożenia: ", a*b)
    if b > 0 and a > 0:
        print("Wyniki pierwiastkowania: ", math.sqrt(a), " i ", math.sqrt((b)))
    elif b <= 0 and a > 0:
        print("Wynik pierwiastkowania dla liczb powyżej 0: ", math.sqrt(a))
    elif b > 0 and a <= 0:
        print("Wynik pierwiastkowania dla liczb powyżej 0: ", math.sqrt(b))
    else:
        print("Nie można zpierwiastkować żadnej liczby")
    return "\n"

a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))
print(obliczenia(a,b))'''
'''
print("\nZadanie 2\n")

def kula(r):
    PoleKuli = 4*math.pi*r**2
    ObjKuli = (4/3)*math.pi*r**3
    return print("Pole kuli wynosi: ",PoleKuli, ". Objętość kuli wynosi: ",ObjKuli)

def stozek(r,l,H):
    PoleSto = (math.pi*r**2) + (math.pi*r*l)
    ObjSto = (1/3)*math.pi*(r**2)*H
    return print("Pole stożka wynosi: ", PoleSto, ". Objętość stożka wynosi: ", ObjSto)

def szescian(a):
    PoleSzesc = 6*a**2
    ObjSzesc = a**3
    return print("Pole sześcianu wynosi: ", PoleSzesc, ". Objętość sześcianu wynosi: ", ObjSzesc)

bryla = input("Jaką bryłę chcesz przeliczyć: ")

if bryla.lower() != 'kula' and bryla.lower() != 'stożek' and bryla.lower() != 'sześcian':
    print("Bryła nie jest obsługiwana")
elif bryla.lower() == 'kula':
    r = float(input("Podaj średnicę (r): "))
    kula(r)
elif bryla.lower() == 'stożek':
    r = float(input("Podaj średnicę podstawy (r): "))
    l = float(input("Podaj długość boku (l): "))
    H = float(input("Podaj wyskość stożka (H): "))
    stozek(r,l,H)
elif bryla.lower() == 'sześcian':
    a = float(input("Podaj długość boku: "))
    szescian(a)
'''
'''
print("\nZadanie 3\n")

def centymetry(ft):
    cm = ft * 30.48
    return float(cm)
def milimetry(ft):
    mm = ft * 304.8
    return float(mm)
def kilometry(ft):
    km = ft * 0.0003048
    return round(float(km),4)

jednostka = input("Jakiej jednostki potrzebujesz: ")

if jednostka.lower() != 'cm' and jednostka.lower() != 'mm' and jednostka.lower() != 'km' and jednostka.lower() == 'centymetry' and jednostka.lower() == 'milimetry' and jednostka.lower() == 'kilometry':
    print("Jednostka nie jest obsługiwana")
elif jednostka.lower() == 'cm' or jednostka.lower() == 'centymetry':
    ft = float(input("Ile stóp: "))
    print(ft, "stóp jest równe",centymetry(ft), "centymetrów")
elif jednostka.lower() == 'mm' or jednostka.lower() == 'milimetry':
    ft = float(input("Ile stóp: "))
    print(ft, "stóp jest równe",milimetry(ft), "milimetrów")
elif jednostka.lower() == 'km' or jednostka.lower() == 'kilometry':
    ft = float(input("Ile stóp: "))
    print(ft, "stóp jest równe",kilometry(ft), "kilometrów")
'''
'''
print("\nZadanie 4\n")

def safe():
    metry = int(input("Na jakiej wysokości lecimy? [w metrach]:"))
    kilometry = metry/1000
    if int(kilometry) < 5:
        return print(int(kilometry), "km to za nisko!")
    else:
        return print("Na tej wyskości jesteś już bezpieczny")

safe()
'''
'''
print("\nZadanie 5\n")

def BMI(masa, wzrost):
    bmi = masa/(wzrost*wzrost)
    if bmi < 18.5:
        return print("Masz niedowagę")
    elif bmi >= 18.5 and bmi < 25:
        return print("Twoja waga jest prawidłowa")
    elif bmi >= 25:
        return print("Masz nadwagę!!!")

masa = float(input("Podaj swoją masę (w kilogramach)"))
wzrost = float(input("Podaj swój wzrost (w metrach)"))

BMI(masa,wzrost)
'''
'''
print("\nZadanie 6\n")

liczba = int(input("Podaj liczbę w systemie dzisiętnym: "))
binary = bin(liczba)
binary = binary.lstrip('0b')
hexadecimal = hex(liczba)
hexadecimal = hexadecimal.lstrip('0x')
print("Podana liczba to",binary,"w systemie dwójkowym i",hexadecimal,"w systemie szesnastkowym")
'''

print("\nZadanie 7\n")

def toRoman(a):
    dictionary = {
        1:  'I',
        2:  'II',
        3:  'III',
        4:  'IV',
        5:  'V',
        9:  'IX',
        10:  'X',
        20:  'XX',
        30:  'XXX',
        40:  'XL',
        50:  'L',
        90:  'XC',
        100:  'C',
        400:  'CD',
        500:  'D',
        900:  'CM',
        1000:  'M'
    }
    a = [*a]
    


a = input("Podaj liczbę do zamiany: ")
toRoman(a)
