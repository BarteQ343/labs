print("")
print("Zadanie 1")
print("")

a = int(input('Podaj liczbę a '))
b = int(input('Podaj liczbę b '))

print(a+b, ' ', a-b, ' ', b-a, ' ', a*b, ' ', a/b, ' ', b/a)

print("")
print("Zadanie 2")
print("")

print(1 % 69, 69 % 1, 1 % 666, 666 % 1, 10000 % 1, 1 % 10000, 69 % 666, 666 % 69, 69 % 10000, 10000 % 69, 666 % 10000, 10000 % 666, 2147483647 % 1, 2147483647 % 69, 2147483647 % 666, 2147483647 % 100000)

print("")
print("Zadanie 3")
print("")

predkoscSwiatla = 299792458

ileSekund = 365 * 24 * 60 * 60

rokSwietlny = predkoscSwiatla * ileSekund

print(rokSwietlny,' metrów')

print("")
print("Zadanie 4")
print("")

godz = 60 * 60
doba = 24 * godz
rok = 365 * doba
zycie = 20 * godz + 2 * 31 * doba + 30 * doba + 18 * doba

print("")
print("Zadanie 5")
print("")

cale = float(input("Ile cali? "))
print(cale,' cali to ',cale*2.54,' centymetrów')

print("")
print("Zadanie 6")
print("")

dystans = 30
czas = 15/60
predkosc = dystans/czas

print(int(predkosc))

czas = 12/60
predkosc = dystans/czas
print(int(predkosc))
