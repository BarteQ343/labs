import random

print("Zad 1")
tablica = ['Sztos','Dzban','Wyższa','Szkoła','Bankowa','Dolnośląska','Czarny','Samochód','Most','Wanted']

for i in range(0,10):
    if i == 0 or i == 3 or i == 6 or i == 8:
        print(tablica[i])

print("Zad 2")
tablica = []

for i in range(0,10):
    tablica.append(random.randrange(1,100))
    if i == 0 or i == 3 or i == 6 or i == 8:
        print(tablica[i])

print("Zad 3")
tablica = []

for i in range(0,9):
    tablica.append(random.randrange(0,59))

tablica.append(2)
tablica.append(8)
tablica.append(4)
tablica.insert(12,16)
tablica.insert(13,32)
tablica.insert(14,64)
print(tablica)
counter = 0
for i in range(0,14):
    if tablica[i] % 2 != 0 and counter < 4:
        counter += 1
        tablica.pop(i)
counter = 0
for i in range(0,14):
    if tablica[i] % 2 != 0 and counter < 4:
        counter += 1
        tablica.remove()
for i in range(0,14):
    if i == 4:
        tablica.pop(i)
        tablica.insert(i,3)
    elif i == 9:
        tablica.pop(i)
        tablica.insert(i,33)

print(tablica)

print("Zad 4")

liczbaN = int(input("Podaj dowolną liczbę naturalną: "))

tablica = [liczbaN]
i = 1
while i < liczbaN:
    if liczbaN % i == 0:
        tablica.insert(-1,i)
    i += 1

print(tablica)
print("Zad 5")

n = int(input("Podaj n: "))
x = int(input("Podaj x: "))
z = int(input("Podaj z: "))
k = int(input("Podaj k: "))
i = 1
tablica = []

while i < n:
    tablica.append(random.randrange(x,z))
    i += 1

print(tablica[-3])
tablica.pop(-k)

tablica2 = []
i = 1
while i < n:
    tablica2.append(random.randrange(x,z))
    i += 1

i = 0
while i < n:
    tablica.append(tablica2[i-1])
    i += 1

i = 0

tablica.sort()
while i < len(tablica)-1:
    if tablica[i] == tablica[i + 1]:
        tablica.pop(i)
    else:
        i += 1

print(len(tablica))

print("Zad 6")

zakresX = int(input("Podaj min zakresu: "))
zakresY = int(input("Podaj max zakresu: "))
zakresZ = int(input("Podaj długość zakresu: "))

lista = []
for i in range(0,zakresZ):
    lista.append(random.randrange(zakresX,zakresY))
lista.sort()
i = 1
while i < len(lista):
    if lista[i] == lista[i-1]:
        lista.pop(i)
    else: i += 1

print(lista, "\nDługość tej listy to:", len(lista))

print("Zad 7")

liczby = []
losowane = []
Luck = input("Chybił-trafił? ")
if Luck == "Tak" or Luck == "tak" or Luck == "yes" or Luck == "Yes" or Luck == "y" or Luck == "Y" or Luck == "T" or Luck == "t":
    amount = int(input("Ile losów? "))
    j = 0
    earnings = 0
    Swins = 0
    Mwins = 0
    Bwins = 0
    while j < amount:
        i = 0
        while i < 6:
            liczby.append(random.randrange(1,50))
            losowane.append(random.randrange(1,50))
            i += 1
        liczby.sort()
        losowane.sort() 
        counter = 0
        for i in range(0,6):
            if liczby[i] == losowane[0] or liczby[i] == losowane[1] or liczby[i] == losowane[2] or liczby[i] == losowane[3] or liczby[i] == losowane[4] or liczby[i] == losowane[5]:
                counter = counter + 1
        if counter == 3:
            earnings += 10
            Swins += 1
        elif counter == 4:
            earnings += random.randrange(100, 1000, 10)
            Mwins += 1
        elif counter == 5:
            earnings += random.randrange(3500, 10000, 100)
            Mwins += 1
        elif counter == 6:
            earnings += random.randrange(1000000, 10000000, 10000)
            Bwins += 1
        j += 1
    print("Wygrałeś ",earnings,"zł w ",Swins," małych, ",Mwins," średnich i ",Bwins," dużych wygranych")
else:
    i = 0
    while i < 6:
        try:
            inLiczby = int(input("Podaj liczbę, która twoim zdanie będzie wygrana: "))
            if inLiczby > 50 or inLiczby <= 0:
                print("Podaj liczbę z zakresu 1-50")
            else:
                liczby.append(inLiczby)
                losowane.append(random.randrange(1,50))
                i = i + 1
        except ValueError:
            print("Podaj liczbę z zakresu 1-50")
    liczby.sort()
    losowane.sort() 
    counter = 0
    for i in range(0,6):
        if liczby[i] == losowane[0] or liczby[i] == losowane[1] or liczby[i] == losowane[2] or liczby[i] == losowane[3] or liczby[i] == losowane[4] or liczby[i] == losowane[5]:
            counter = counter + 1
    if counter == 3:
        print("Trafiłeś trójkę! Wygrywasz 10 zł")
    elif counter == 4:
        print("Trafiłeś czwórkę! Wygrywasz ", random.randrange(100, 1000, 10))
    elif counter == 5:
        print("Trafiłeś piątkę! Wygrywasz ", random.randrange(3500, 10000, 100))
    elif counter == 6:
        print("Trafiłeś szóstkę! Wygrywasz ", random.randrange(1000000, 10000000, 10000))
    else:
        print("Trafiłeś dwójkę, jedynkę lub nie trafiłeś nic. Spróbuj ponownie")

print("Zad 8")

lista = []
for i in range(0,20):
    lista.append(random.randrange(0,200))

random.shuffle(lista)
print(lista)
order = input("Rozsnąco, czy malejąco? (asc lub dsc) ")
if order == 'asc':
    lista.sort()
    print(lista)
elif order == 'dsc':
    lista.sort(reverse=True)
    print(lista)
else:
    print("Nie wiem czy chcesz malejąco, czy rosnąco")

print("Zad 9")

amount = int(input("Ile liczb? "))
lista = []
for i in range(0,amount):
    lista.append(int(input("Podaj liczbę: ")))

count = 0
counter = 0
for i in range(0,len(lista)):
    if lista[i] > count:
        count = lista[i]
        counter = 1
    elif lista[i] == count:
        counter += 1

print('Największą liczbą było: ',count,' i wystąpiło ',counter,' razy')

print("Zad 10")

n = int(input("Ile liczb? "))
if n == 0:
    print("To chcesz ten ciąg Fibonacciego, czy nie?")
elif n == 1:
    fib = [0]
    print("Pierwsza liczba Fibonacciego to 0")
elif n == 2:
    fib = [0, 1]
    print("Pierwsze 2 liczby Fibonacciego to 0 i 1")
else:
    i = 2
    fib = [0, 1]
    while i <= n:
        fib.append(fib[i-2]+fib[i-1])
        i += 1
    print("Pierwsze ",n," liczb Fibonacciego to ",fib)

print("Zad 11")
import math

n = int(input("Jaki zakres? "))
A = [True] * (n+1)

for i in range(2,int(math.sqrt(n))):
    if A[i]:
        for k in range(i*i,n+1,i):
            A[k] = False
print('Liczby pierwsze z przedziału <,',n,"> : ")
for i in range(2, n+1): 
    if A[i]:
        print(str(i), end=" | ")
