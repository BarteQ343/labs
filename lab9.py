import random


try:
    print("\nZadanie 1\n")

    pula = ["Bayern Monachium","Real Madrid","FC Barcelona","Legia Warszawa","Manchester United","Arsenal","Chelsea","Borussia Dortmund","AC Milan","SSC Napoli","Manchester City","Paris Saint-Germain","Inter Milan","Benefica","RB Leipzig","FC Porto","Newcastle United","Palmeiras","Ajax Amsterdam","Juventus"]

    LigaMistrzow = set()
    LigaEuropy = set()
    UEFASuperCup = set()
    LigaMlodziezowa = set()
    for i in range(0,10):
        LigaMistrzow.add(pula[random.randrange(0,19)])
        LigaEuropy.add(pula[random.randrange(0,19)])
        UEFASuperCup.add(pula[random.randrange(0,19)])
        LigaMlodziezowa.add(pula[random.randrange(0,19)])

    print("\nZadanie 2\n")

    print(LigaMistrzow.intersection(LigaEuropy),"\n",UEFASuperCup.intersection(LigaMlodziezowa),"\n",UEFASuperCup.intersection(LigaEuropy)," | ")
    print(LigaMistrzow.difference(LigaEuropy),"\n",UEFASuperCup.difference(LigaMlodziezowa),"\n",UEFASuperCup.difference(LigaEuropy)," | ")
    print(LigaMistrzow.union(LigaEuropy),"\n",UEFASuperCup.union(LigaMlodziezowa),"\n",UEFASuperCup.union(LigaEuropy)," | ")
    print(LigaMistrzow.issuperset(LigaEuropy),UEFASuperCup.issuperset(LigaMlodziezowa),UEFASuperCup.issuperset(LigaEuropy))
    print(LigaMistrzow.issubset(LigaEuropy),UEFASuperCup.issubset(LigaMlodziezowa),UEFASuperCup.issubset(LigaEuropy))

    print("\nZadanie 3\n")

    print(len(LigaEuropy),len(LigaMistrzow),len(LigaMlodziezowa),len(UEFASuperCup))
    print(LigaEuropy.symmetric_difference(LigaMlodziezowa),LigaMistrzow.symmetric_difference(LigaMlodziezowa),LigaMlodziezowa.symmetric_difference(UEFASuperCup),UEFASuperCup.symmetric_difference(LigaEuropy))
    list(LigaEuropy)
    list(LigaMlodziezowa)
    list(LigaMistrzow)
    list(UEFASuperCup)

except KeyboardInterrupt:
    print("\nStopping")
