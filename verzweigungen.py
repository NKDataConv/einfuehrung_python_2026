bedingung = 3>2

if bedingung:
    print("ja, ist groesser")
else:
    print("nein, nicht groesser")


bedingung_1 = 3>2
bedingung_2 = 3==2

if bedingung_1 and bedingung_2:
    print("ja, bedingungen erfüllt")
    print(bedingung_1)
    print(bedingung_2)
    a = 1
    b = 3*7
    print(b)
else:
    print("nein, nicht erfüllt")


# Aufgabe 3:
jahr = 1952
bedingung_4 = jahr % 4 == 0
bedingung_100 = jahr % 100 == 0
bedingung_400 = jahr % 400 == 0

if bedingung_400:
    print("Schaltjahr")
elif bedingung_4 and not bedingung_100:
    print("Schaltjahr")
else:
    print("Kein Schaltjahr")