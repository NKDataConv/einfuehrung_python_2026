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

# Aufgabe 1
my_list = [3, 4, 3, 2, 3, 5, 3, 4]

# Option 1
summe = 0
for element in my_list:
    summe += element
print(f"Die Summe ist {summe}")

# Option 2
summe = sum(my_list)
print(f"Die Summe ist {summe}")

# Aufgabe 2

# Option 1
maximum = my_list[0]
for element in my_list:
    if element > maximum:
        maximum = element
print(f"Das Maximum ist {maximum}")

# Option 2
maximum = max(my_list)
print("Das Maximum ist", maximum)

# Option 3
my_list.sort()
maximum = my_list[-1]
print(f"Das Maximum ist {maximum}")

# Dictionaries
erstes_dict = {"cat": "Katze", "dog": "Hund", "bird": "Vogel"}
uebersetzung_cat = erstes_dict["cat"]
print(uebersetzung_cat)

zweites_dict = {1: 2, 3: 4, 2: 1}

drittes_dict = {"list": my_list, "other_list": my_list[1:3]}
print(drittes_dict)

viertes_dict = {my_list[3]: True, my_list[1]: False}
print(my_list)
print(viertes_dict)

erstes_dict = {"cat": "Katze", "dog": "Hund", "bird": "Vogel", "cat": "Katze2"}
#uebersetzung_rabbit = erstes_dict["rabbit"]
#print(uebersetzung_rabbit)

for k, v in erstes_dict.items():
    print(f"Die Übersetzung von {k} ist {v}")

# Zugriff über Values
for k, v in erstes_dict.items():
    if v == "Hund":
        print(k)

erstes_dict = {"cat": "Katze", "dog": "Hund", "bird": "Vogel"}
laenge = len(erstes_dict)
print(laenge)

dict_keys = erstes_dict.keys()
print(dict_keys)

dict_values = erstes_dict.values()
print(dict_values)

for deutsche_woerter in erstes_dict.values():
    print(deutsche_woerter)

katze = erstes_dict.pop("cat")
print(erstes_dict)
print(katze)

if "cat" in erstes_dict.keys():
    del(erstes_dict["cat"])

print(erstes_dict)

# Aufgabe 1
namen = {"Peter": 20, "Günter": 16, "Max": 30}

# Aufgabe 2
for k in namen.keys():
    namen[k] = namen[k] + 1
print(namen)

# Aufgabe 3
nicht_volljährig = []
for k, v in namen.items():
    if v < 18:
        nicht_volljährig.append(k)
print(nicht_volljährig)