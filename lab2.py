'''a = int(input('Podaj liczbę a '))
b = int(input('Podaj liczbę b '))
if b > a:
    print("b jest większe od a")
elif a > b:
    print('a jest większe od b')
elif a == b:
    print('a jest równe b')'''

#Zadanie 1

from math import sqrt


print("")
print("")
print("Zadanie 1")
print("")
print("")
a = int(input('Podaj liczbę a '))
b = int(input('Podaj liczbę b '))

if a % b == 0:
    print('Liczba a jest podzielna przez b')
elif a % b != 0:
    print('Liczba a nie jest podzielna przez b')

#Zadanie 2
print("")
print("")
print("Zadanie 2")
print("")
print("")
#a jest pobierane z zadania 1

if a <= 10:
    print('Zmienna jest mniejsza lub równa 10')
elif a > 10 and a <= 25:
    print('Zmienna jest większa od 10, ale nie większa od 25')
else:
    print('Zmienna jest większa od 25')

#Zadanie 3
print("")
print("")
print("Zadanie 3")
print("")
print("")
a = 40
b = 50
c = 30

if a > b:
    if a > c:
        print('Liczba a jest największa')
    else:
        print('Liczba c jest największa')
elif b > a:
    if c > b:
        print('Liczba c jest największa')
    else:
        print('Liczba b jest największa')


#Zadanie 4
print("")
print("")
print("Zadanie 4")
print("")
print("")
a = 0

if a < 0:
    if a % 2 > 0:
        print('Liczba jest ujemna i podzielna przez 2 z resztą')
    elif a % 2 == 0:
        print('Liczba jest ujemna i podzielna przez 2 bez reszty')
elif a > 0:
    if a % 2 > 0:
        print('Liczba jest dodatnia i podzielna przez 2 z resztą')
    elif a % 2 == 0:
        print('Liczba jest dodatnia i podzielna przez 2 bez reszty')
else:
    print('Liczba wynosi 0 lub nie jest to liczba')

#Zadanie 5
print("")
print("")
print("Zadanie 5")
print("")
print("")

a = float(input('Podaj ile mg/l alkoholu jest w wydychanym powietrzu: '))

if a <= 0.1 and a > 0:
    print('Kierowca jest trzeźwy, ale po spożyciu')
elif a == 0:
    print('Kierowca jest trzeźwy')
elif a > 0.5:
    print('Kierowca popełnia przestępstwo')

#Zadanie 6
print("")
print("")
print("Zadanie 6")
print("")
print("")

a = int(input('Podaj pierwszą liczbę '))
b = int(input('Podaj drugą liczbę '))
c = int(input('Podaj trzecią liczbę '))
d = int(input('Podaj czwartą liczbę '))

if a > b:
    if c > a:
        if d > c:
            print('Liczba d: ', d, ' jest największa')
        else:
            print('Liczba c: ', c, ' jest największa')
    elif d > a:
        print('Liczba d: ', d, ' jest największa')
    else:
        print('Liczba a: ', a, ' jest największa')
elif b > a:
    if c > b:
        if d > c:
            print('Liczba d: ', d, ' jest największa')
        else:
            print('Liczba c: ', c, ' jest największa')
    elif d > b:
        print('Liczba d: ', d, ' jest największa')
    else:
        print('Liczba b: ', b, ' jest największa')
elif a == b and b == c and d == c:
    print('Wszystkie liczby są równe i wynoszą: ', a)
elif a == b:
    if a > d and a > c:
        print('Liczby a i b są równe i największe, i wynoszą: ', a)
    elif d > a or c > a:
        if d > c:
            print('Liczba d: ', d, ' jest największa')
        else:
            print('Liczba c: ', c, ' jest największa')
elif a == c:
    if a > d and a > b:
        print('Liczby a i b są równe i największe, i wynoszą: ', a)
    elif d > a or b > a:
        if d > b:
            print('Liczba d: ', d, ' jest największa')
        else:
            print('Liczba b: ', b, ' jest największa')
elif a == d:
    if a > b and a > c:
        print('Liczby a i d są równe i największe, i wynoszą: ', a)
    elif b > a or c > a:
        if b > c:
            print('Liczba b: ', b, ' jest największa')
        else:
            print('Liczba c: ', c, ' jest największa')
elif d == b:
    if d > a and d > c:
        print('Liczby d i b są równe i największe, i wynoszą: ', d)
    elif a > d or c > d:
        if a > c:
            print('Liczba a: ', a, ' jest największa')
        else:
            print('Liczba c: ', c, ' jest największa')
elif c == b:
    if c > d and c > a:
        print('Liczby c i b są równe i największe, i wynoszą: ', b)
    elif d > c or a > c:
        if d > a:
            print('Liczba d: ', d, ' jest największa')
        else:
            print('Liczba a: ', a, ' jest największa')
elif c == d:
    if c > b and c > a:
        print('Liczby c i d są równe i największe, i wynoszą: ', c)
    elif b > c or a > c:
        if a > b:
            print('Liczba a: ', a, ' jest największa')
        else:
            print('Liczba b: ', b, ' jest największa')
elif a == b and b == c:
    if d > a:
        print('Liczba d: ', d, ' jest największa')
    else:
        print('Liczby a, b i c są równe i wynoszą: ', a)
elif a == b and b == d:
    if c > a:
        print('Liczba c: ', c, ' jest największa')
    else:
        print('Liczby a, b i d są równe i wynoszą: ', a)
elif a == c and a == d:
    if b > a:
        print('Liczba b: ', b, ' jest największa')
    else:
        print('Liczby a, d i c są równe i wynoszą: ', a)
elif b == c and b == d:
    if a > b:
        print('Liczba a: ', a, ' jest największa')
    else:
        print('Liczby d, b i c są równe i wynoszą: ', d)

#Zadanie 7
print("")
print("")
print("Zadanie 7")
print("")
print("")

a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj c "))
x = int(input("Podaj x "))

y = (a * (x ** 2)) + (b * x) + c

print('Współrzędne (x,y) wynoszą: (', x ,',', y ,')')

delta = b ** 2 + 4 * a * c

if delta < 0:
    print('Funkcja kwadratowa nie ma miejsc zerowych')
elif delta == 0:
    x = -(b / (2 * a))
    print('Funkcja kwadratowa ma jedno miejsce zerowe, które wynosi ', x)
elif delta > 0:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print('Funkcja kwadratowa ma dwie miejsca zerowe i wynoszą one ', x1, ',', x2)

#Zadanie 8
print("")
print("")
print("Zadanie 8")
print("")
print("")

a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj c "))

if a+b < c and a+c < b and c+b < a:
    print("Podane boki nie utworzą trójkąta")
else:
    if (a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or (c**2 + b**2) == a**2:
        print("Trójkąt jest prostokątny")
    else:
        print("Trójkąt nie jest prostokątny")
