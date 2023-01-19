try:
    print("")
    print("Zadanie 1")
    print("")

    i = 0
    while i < 99:
        print("To jest efekt pętli while")
        i += 1

    print("")
    print("Zadanie 2")
    print("")

    i = 254
    while i <= 320:
        if i % 2 != 0 and i % 5 == 0:
            print(i)
        i += 1

    i = -320
    while i <= -254:
        if i % 2 != 0 and i % 5 == 0:
            print(i)
        i += 1

    print("")
    print("Zadanie 3")
    print("")

    i = 0
    while i == 0:
        test = int(input("Podaj liczbę podzielną przez 12: "))
        if test % 12 == 0:
            print("Podałeś liczbę podzielną przez 12, więc kończę działanie pętli")
            i += 1
    
    print("")
    print("Zadanie 4")
    print("")

    i = 0
    nums = []
    while i == 0:
        try:
            nums.append(int(input("Podaj liczbę: ")))
            if nums[-1] == 0:
                i += 1
            print(sum(nums) / len(nums))
        except ValueError:
            if len(nums) != 0:
                print(sum(nums) / len(nums))
            i += 1
           
    
    print("")
    print("Zadanie 5")
    print("")

    i = 0
    nums = []
    while i == 0:
        try:
            nums.append(int(input("Podaj liczbę: ")))
            if sum(nums) >= 100:
                i += 1
                print("Stopping; exceeded 100 by ",sum(nums)-100)
            elif sum(nums) / len(nums) >= 66:
                i += 1
                print("Stopping; exceeded average of 66 by:", sum(nums) / len(nums))
        except ValueError:
            print("Stopping; NaN")
            i += 1
    
    
    
    print("")
    print("Zadanie 6")
    print("")

    a = int(input("Podaj liczbę: "))
    dzielniki = []
    i = 1
    while i <= int(a/2):
        if a % i == 0:
            dzielniki.append(i)
        i += 1
    if sum(dzielniki) == a:
        print("Liczba jest doskonała")
    else:
        print("Liczba nie jest doskonała")

    
    print("")
    print("Zadanie 7")
    print("")

    a = int(input("Podaj liczbę: "))
    dzielniki = []
    i = 1
    while i <= a:
        if a % i == 0:
            dzielniki.append(i)
        i += 1
    if len(dzielniki) == 2:
        print("Liczba jest pierwsza")
    else:
        print("Liczba nie jest pierwsza")
    
    
    print("")
    print("Zadanie 8")
    print("")

    i = 0
    #earnings = 3891 - 333
    savings = 333
    while i < 12:
        savings = savings*1.08 + 333
        i += 1
    print(round(savings, 2))

    
    print("")
    print("Zadanie 9")
    print("")

    i = 0
    nums = []
    while i == 0:
        try:
            nums.append(int(input("Podaj liczbę: ")))
            if len(nums) <= 1:
                nums.append(int(input("Podaj liczbę: ")))
            elif abs(nums[-1] - nums[-2]) < 5:
                i += 1
                print(nums)
        except ValueError:
            if len(nums) != 0:
                print(sum(nums) / len(nums))
            i += 1
    
    
    print("")
    print("Zadanie 10")
    print("")

    i = 0
    nums = []
    while i == 0:
        try:
            nums.append(int(input("Podaj liczbę: ")))
            if len(nums) <= 1:
                nums.append(int(input("Podaj liczbę: ")))
            elif nums[-1] == nums[-2]:
                i += 1
                print(sum(nums))
        except ValueError:
            if len(nums) != 0:
                print(sum(nums))
            i += 1

except KeyboardInterrupt:
    print("\nStopping")
