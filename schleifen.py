for zahl in range(1, 10):
    print(zahl)

for j in range(-10, 1):
    a = j*2
    print(a)

i = 0
while i < 10:
    print(f"Läuft {i}")
    i = i - 1
    if i == -100:
        break

print("Ende des Laufs")

keyboard = "w"
while keyboard == "w":
    action = "vorne laufen"
    print(action)
    keyboard = "a"
    #keyboard = input(str())

# Aufgabe 1a:
for i in range(1, 15):
    print(i*2)

for i in range(1, 30):
    if i % 2 == 0:
        print(i)

for i in range(2, 30, 2):
    print(i)

zahl1 = 2
while zahl1<=28:
    print(zahl1)
    zahl1 = zahl1 +2

# Aufgabe 1b:
for i in range(1, 11):
    print(i**2)

# Aufgabe 1c:
for j in range(1, 10):
    print(2**j)

zahl3 = 1
while zahl3<=512:
    print(zahl3)
    zahl3 = zahl3 * 2

# Aufgabe 2:
n = 10
zahl = 1
for i in range(1, n+1):
    zahl = zahl * i
print(zahl)

# Aufgabe 3
zahl_pos_1 = 0
zahl_pos_2 = 1
n = 100

for i in range(1, n):
    neue_zahl = zahl_pos_1 + zahl_pos_2
    print(neue_zahl)

    zahl_pos_1 = zahl_pos_2
    zahl_pos_2 = neue_zahl

