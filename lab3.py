import random
print('')
print('Zadanie 1')
print('')

for i in range(1,100):
    if i % 8 == 0:
        print(i)

print('')
print('Zadanie 2')
print('')

x = int(input('Podaj wartość '))
for i in range(x, 0, -1):
    if i % 6 == 0 and i % 9 == 0:
        print(i)

print('')
print('Zadanie 3')
print('')

for i in range(100, 201):
    if i % 2 != 0 and i % 3 != 0:
        print(i)



print('')
print('Zadanie 4')
print('')

for i in range(100, 201):
    if i % 2 == 0 and i % 5 !=0 and i % 6 != 0 and i % 11 != 0:
        print(i)


print('')
print('Zadanie 5')
print('')

x = int(input('Silnię z jakiej liczby chcesz obliczyć? '))
s = 1
if x == 0:
    print(1)
else:
    for i in range(2, x+2):
        print(s)
        s *= i
print('')
print('Zadanie 6')
print('')

x = int(input('Podaj jak dużą chcesz choinkę: '))
print(' ')
for i in range(x):
    print((' '*(-i+x)+'*'*(i+1))+('*'*(i+1)))
y = x/4
for i in range(int(y)):
    if int(y) < 2:
        print(' '*x+(2*'*'))
    else:
        print(' '*x+(int(y)*'*'))
    

print('')
print('Zadanie 7')
print('')

n = int(input("Podaj ile chcesz potęg liczby 2: "))

for i in range(1,n):
    print("2 do potęgi", i, "wynosi: ",2**i)

print('')
print('Zadanie 8')
print('')
x = 1
wynik = 0
for i in range(0, 1000):
    x += 1
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        wynik = x
print(wynik)
    


print('')
print('Zadanie 9')
print('')

liczby = []
losowane = []
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
    print("Trafiłeś trójkę!")
elif counter == 4:
    print("Trafiłeś czwórkę!")
elif counter == 5:
    print("Trafiłeś piątkę!")
elif counter == 6:
    print("Trafiłeś szóstkę!")
else:
    print("Trafiłeś dwójkę, jedynkę lub nie trafiłeś nic. Spróbuj ponownie")

print('')
print('Zadanie 10')
print('')

#!IMPORTANT: Nigdy nie grałem w Multi Multi ani Mini LOTTO, więc te dwa zadania będą na oko, według tego co zrozumiałem z zasad tych gier po przeczytaniu na stronie LOTTO

liczby = []
losowane = []
n = 0
for i in range(0,100):
    if n == 0:
        n = int(input("Podaj ilość liczb, na które chesz postawić w zakresie 1-10: "))
    elif n > 0 and n < 11:
        print("Stawiasz na ", n, " liczb")
        break
    else:
        n = int(input("Podaj ilość liczb, na które chesz postawić w zakresie 1-10: "))

for i in range(1,21):
    losowane.append(random.randrange(1,80))


i = 0
while i < n:
    try:
        inLiczby = int(input("Podaj liczbę, która twoim zdanie będzie wygrana: "))
        if inLiczby > 80 or inLiczby <= 0:
            print("Podaj liczbę z zakresu 1-80")
        else:
            liczby.append(inLiczby)
            i = i + 1
    except ValueError:
        print("Podaj liczbę z zakresu 1-80")

liczby.sort()
losowane.sort()

mnoznik = 0
for i in range(0,100):
    if mnoznik == 0:
        mnoznik = int(input("Podaj mnożnik w zakresie 1-10: "))
    elif mnoznik > 0 and mnoznik < 11:
        print("Stawiasz na ", mnoznik, "-krotny mnożnik")
        break
    else:
        mnoznik = int(input("Podaj mnożnik w zakresie 1-10: "))

plus = False
plus = bool(input("Z plusem? (True lub False): "))

counter = 0
plusCounter = False
for i in range(0,19):
    if liczby[i] == losowane[0] or liczby[i] == losowane[1] or liczby[i] == losowane[2] or liczby[i] == losowane[3] or liczby[i] == losowane[4] or liczby[i] == losowane[5] or liczby[i] == losowane[6] or liczby[i] == losowane[7] or liczby[i] == losowane[8] or liczby[i] == losowane[9] or liczby[i] == losowane[10] or liczby[i] == losowane[11] or liczby[i] == losowane[12] or liczby[i] == losowane[13] or liczby[i] == losowane[14] or liczby[i] == losowane[15] or liczby[i] == losowane[16] or liczby[i] == losowane[17] or liczby[i] == losowane[18] or liczby[i] == losowane[19]:
        counter = counter + 1
if counter == 0:
    print("Nie trafiłeś nic")
elif counter == 1:
    print("Trafiłeś jedynkę!")
elif counter == 2:
    print("Trafiłeś dwójkę!")
elif counter == 3:
    print("Trafiłeś trójkę!")
elif counter == 4:
    print("Trafiłeś czwórkę!")
elif counter == 5:
    print("Trafiłeś piątkę!")
elif counter == 6:
    print("Trafiłeś szóstkę!")
elif counter == 7:
    print("Trafiłeś siódemkę!")
elif counter == 8:
    print("Trafiłeś ósemkę!")
elif counter == 9:
    print("Trafiłeś dziewiątkę!")
elif counter == 10:
    print("Trafiłeś dziesiątkę!")
if plus == True:
    if liczby[i] == losowane[19]:
        print("Trafiłeś Plusa!")
        plusCounter = True
    elif plusCounter == False:
        print("Nie trafiłeś plusa")


        
    

print('')
print('Zadanie 11')
print('')

liczby = []
losowane = []

for i in range(1,6):
    losowane.append(random.randrange(1,42))

n = 0
for i in range(0,100):
    if n == 0:
        n = int(input("Podaj ilość liczb, na które chesz postawić w zakresie 5-12: "))
    elif n > 4 and n < 13:
        print("Stawiasz na ", n, " liczb")
        break
    else:
        n = int(input("Podaj ilość liczb, na które chesz postawić w zakresie 5-12: "))

i = 0
while i < n:
    try:
        inLiczby = int(input("Podaj liczbę, która twoim zdanie będzie wygrana z zakresu 1-42: "))
        if inLiczby > 42 or inLiczby <= 0:
            print("Podaj liczbę z zakresu 1-42")
        else:
            liczby.append(inLiczby)
            i = i + 1
    except ValueError:
        print("Podaj liczbę z zakresu 1-42")

liczby.sort()
losowane.sort() 

counter = 0
for i in range(0,n):
    if liczby[i] == losowane[0] or liczby[i] == losowane[1] or liczby[i] == losowane[2] or liczby[i] == losowane[3] or liczby[i] == losowane[4]:
        counter = counter + 1

if counter == 0:
    print("Nie trafiłeś nic")
elif counter == 1:
    print("Trafiłeś jedynkę!")
elif counter == 2:
    print("Trafiłeś dwójkę!")
elif counter == 3:
    print("Trafiłeś trójkę!")
elif counter == 4:
    print("Trafiłeś czwórkę!")
elif counter >= 5:
    print("Trafiłeś piątkę lub więcej!")


print('')
print('Zadanie 12')
print('')

lista = []
counterO = 0
counterR = 0
for rzut in range(50):
    a = random.randrange(0,2)
    if a == 0:
        lista.append('orzeł')
        counterO += 1
    else:
        lista.append('reszka')
        counterR += 1
print('Liczba orłów: ', counterO,'; Liczba reszek: ', counterR)
print(lista)

