import random


try:
    
    print("\nZadanie 1\n")

    n = int(input("Ile liczb? "))
    i = 0
    nums = []
    while i < n:
        try:
            i += 1
            num = float(input("Podaj liczbę: "))
            if len(nums) <= 1 and num >= 0:
                nums.append(num)
            elif num >= 0:
                nums.append(num)
            else:
                continue
        except ValueError:
            if len(nums) != 0:
                print("Przerwano! Niepoprawny znak")
            i = n
    print(sum(nums)/len(nums))
    
    
    print("\nZadanie 2\n")

    n = int(input("Jaki początek zakresu? "))
    x = int(input("Jaki koniec zakresu? "))
    if n > x or (x-n) < 6:
        print(x-n)
        print("Nieprawidłowy zakres, minimum 6 różnicy")
    else:
        zakres = []
        for i in range(n,x):
            print(i)
            zakres.append(i)
            if i == n+5:
                zakres.sort()
                print("Minimum: ",zakres[0],"\nMaksimum: ",zakres[0],"\nMediana: ",((zakres[2]+zakres[3])/2))
                break
    
    
    print("\nZadanie 3\n")

    n = input("Podaj liczbę do odwrócenia: ")
    Nlist = list(n)
    NlistRev = list(n)
    NlistRev.reverse()
    print(''.join(NlistRev))
    if Nlist == NlistRev:
        print("Liczba jest palindromem")
        
    
    print("\nZadanie 4\n")

    n = int(input("Ile liczb? "))
    i = 0
    while i < n:
        a = int(input("Podaj liczbę: "))
        i += 1
        if a >= -6 and a <= 6:
            print("Liczba jest z przedziału [-6,6]")
    
    
    print("\nZadanie 5\n")

    nums = []
    i = 0
    while i <= 100:
        nums.append(i**3)
        i += 1
    print(sum(nums))

    nums = []
    i = 0
    while i:
        nums.append(i)
        i += 1
        if sum(nums) >= 10**6:
            break
    
    print(i,"\n",sum(nums))
    
    
    print("\nZadanie 6\n")

    n = random.randrange(1,100)
    i = 0
    while i == 0 or i != 0:
        a = int(input("Zgadnij liczbę: "))
        if a > n:
            print("Podałeś za dużą wartość")
            i += 1
            if i == 3:
                print("Haha przegrałeś!")
                break
        elif a < n:
            print("Podałeś za małą wartość")
            i += 1
            if i == 3:
                print("Haha przegrałeś!")
                break
        elif a == n:
            print("Gratulacje!")
            break
    
    
    print("\nZadanie 7\n")

    print("  /\___/\\\n((\`@_@'/))\n  {_:Y:.}_//\n--{_}^-'{_}--\nLubię programować miau!")
    
except KeyboardInterrupt:
    print("\nStopping")
