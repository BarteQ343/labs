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

menu['pizza'] =  19.99
for i in menu.items():
    print(i)


