erste_liste = [1, 2, 3]
zweite_liste = ["Hallo", "Welt", "!"]
dritte_liste = [True, False]
gemischte_liste = [1.231, 3, True]

laenge_der_liste = len(erste_liste)
print(laenge_der_liste)

zahlen_liste = [5, 9, 3, 12, 0, 1, -100, 30, 8]
print(zahlen_liste[0])
print(zahlen_liste[1])
print(zahlen_liste[2])
print(zahlen_liste[0:5])

laenge = len(zahlen_liste)
print(zahlen_liste[laenge-1])
print(zahlen_liste[-1])
print(zahlen_liste[-2])
print(zahlen_liste[0:-1])
print(zahlen_liste)

zahlen_liste.append(12)
print(zahlen_liste)

i = zahlen_liste.pop(1)
print(i)
print(zahlen_liste)

zahlen_liste[1] = 0
print(zahlen_liste)

del(zahlen_liste[1])
print(zahlen_liste)

zahlen_liste.sort()
print(zahlen_liste)

for i in zahlen_liste:
    print(i)

counter = 0
for i in zahlen_liste:
    if type(i) == int:
        counter += 1

print(f"Es gibt {counter} Integer")

mehrdimensionale_listen = [[1,2,3], True, "Hallo"]
print(mehrdimensionale_listen[2][1])