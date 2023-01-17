tup = (1, 2, 3, 'cztery', 'pięć', 'sześć')
print(len(tup))
print(id(tup))
tup = tup + (7, 8)
print(id(tup))
list(tup)

import random

krotka = []
for i in range(0, 99):
    rand = random.randrange(0, 10)
    rand = int(rand)
    krotka.append(rand)

krotka = tuple(krotka)
print(krotka)

counter01 = 0
counter2 = 0
parzyste = []
nieparzyste = []
for i in range(0, len(krotka)):
    if krotka[i] == 0 or krotka[i] == 1:
        counter01 = counter01 + 1
    elif krotka[i] == 2:
        counter2 = counter2 + 1
    if krotka[i] % 2 == 0:
        parzyste.append(krotka[i])
    elif krotka[i] % 2 != 0:
        nieparzyste.append(krotka[i])
parzyste = tuple(parzyste)
nieparzyste = tuple(nieparzyste)
print('Elementy parzyste: ', parzyste, '\nNieparzyste elementy: ', nieparzyste)

krotka0 = []
for i in range(0, 99):
    rand = random.randrange(0, 101)
    rand = int(rand)
    if rand % 2 == 0:
        krotka0.append(rand)
    else:
        i = i - 1

krotka1 = []
for i in range(0, 99):
    rand = random.randrange(0, 101)
    rand = int(rand)
    if rand % 2 != 0:
        krotka1.append(rand)
    else:
        i = i - 1

krotka0 = tuple(krotka0)
print(id(krotka0))
krotka1 = tuple(krotka1)
print(id(krotka1))
krotka = krotka0 + krotka1
print(id(krotka), len(krotka))

if krotka.count(0) == 0:
    print("Brak zer")
else:
    print('W krotce jest ', krotka.count(0), " zer(a)")
if krotka.count(100) == 0:
    print("Brak setek")
else:
    print('W krotce jest ', krotka.count(100), " setek")

krotka = ('Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'In', 'nec', 'posuere', 'dolor', 'fringilla', 'auctor', 'purus')

lorem = input('Podaj słowo będące częścią lorem ipsum: ')
if lorem in krotka:
    print(krotka.count(lorem))
else:
    print('Brak wystąpień')

ana1 = input("Input")
ana2 = input("Input")

ana0 = (ana1, ana2)

if len(ana1) != len(ana2):
    print("podane wyrazy nie są anagramami")
elif ana1 == ana2:
    print("Podane słowa są te same")
else:
    ana1 = list(ana1)
    ana2 = list(ana2)
    ana1.sort()
    ana2.sort()
    ana1 = tuple(ana1)
    ana2 = tuple(ana2)
    truCount = 0
    for i in (0, len(ana1)-1):
        if ana1.count(ana1[i]) != ana2.count(ana2[i]):
            printer = "podane wyrazy nie są anagramami"
            break
        else:
            printer = "podane wyrazy to anagramy"
    print(printer)
