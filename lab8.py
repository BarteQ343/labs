import time

menu = {
    'hamburger mały': 5.0,
    'cheeseburger mały': 6.0,
    'hamburger średni': 7.0,
    'cheeseburger średni': 8.0,
    'hamburger duży': 10.0,
    'cheeseburger duży': 11.0,
    'frytki małe': 2.5,
    'frytki średnie': 4.5,
    'frytki duże': 6.5,
    'coca-cola': 4.25
        }
for i in menu:
    print(i)
for i in menu.values():
    print(i)
for i in menu.items():
    print(i)
print("\n\n\n\n")

countup = 0.01
countdown = 100.50
for i in menu.values():
    if i >= countup:
        countup = i
    if i <= countdown:
        countdown = i

toRm = 0
for key, value in dict(menu).items():
        if value == countdown or value == countup:
            del menu[key]

menu['pizza'] = 19.99
for i in menu.items():
    print(i)

kontakty = {
    'Steve Jobs': 111222333,
    'Bill Gates': 123123123,
    'Kanye West': 222111333,
    'Dwayne Johnson': 333111222,
    'Donald Trump': 333222111,
    'Joe Biden': 321321321,
    'Krzysztof Krawczyk': 213213213,
    'Mark Zuckerberg': 444555666,
    'Arnold Schwarzenegger': 456456456,
    'Amber Heard': 654654654,
}

kontakty['Johnny Depp'] = kontakty['Amber Heard']
del kontakty['Amber Heard']
kontakty['Steve Wozniak'] = kontakty['Steve Jobs']
del kontakty['Steve Jobs']

for i in dict(kontakty):
    if i != 'Johnny Depp' and i != 'Steve Wozniak':
        del kontakty[i]

for i in kontakty.items():
    print(i)

kontakty.clear()

kontakty['Mark Zuckerberg'] = 333111222
kontakty['Krzysztof Krawczyk'] = 444555666

print(sorted(kontakty.items(), reverse=True))

loginy = {
    'karmel':'Karmel2',
    'admin':'admin',
    'moderator':'moderator',
    'bastekmisiek02':'MasloHaslo123',
    'Bobr20_02':'HasloMaslo321',
    'adamw':'WAdam5'
}

i = input("Podaj login: ")
j = input("Podaj hasło: ")
try:
    if i == 'admin' and j == loginy[i]:
        print("Witamy w panelu admina")
    elif j != loginy[i]:
        print("Wprowadzono błędne hasło")
    else:
        print('Witamy na stronie internetowej, która na pewnie nie jest panelem admina')
except KeyError:
    print("Nieznana nazwa użytkownika")
    
email = {
    0: 'sample@sample.com'
}

mail = input('Podaj adres email: ')
count = 0
for i in email:
    
