
def erste_funktion(a, b):
    ergebnis = a*b
    print(f"a hat den Wert {a}")
    print(f"b hat den Wert {b}")
    return ergebnis

ausgabe_der_funktion = erste_funktion(a=2, b=3)
print(ausgabe_der_funktion)

def begruessung():
    print("Hallo Welt!")

begruessung()

def begruessung(name):
    print(f"Hallo {name}!")

begruessung("Bob")

def begruessung(name):
    return f"Hallo {name}!"

begruessungs_text = begruessung("Bob")
print(begruessungs_text)

def erste_funktion(a: int, b: float):
    c = 10
    ergebnis = a*b+c
    print(f"a hat den Wert {a}")
    print(f"b hat den Wert {b}")
    return ergebnis


print(erste_funktion(a=2, b=1.23))


globaler_name = "Alice"

def begruessung(name: str):
    """Diese Funktion gibt eine Begrueßung aus."""
    print(f"Hallo {name}!")

begruessung(name="Alice")

def begruessung(name: str):
    print(f"Hallo {name}!")

begruessung("Alice")

# Aufgabe 1
def produkt(zahl_1, zahl_2, zahl_3):
    return zahl_1 * zahl_2 * zahl_3

print(produkt(1,2,3))

# Aufgabe 2
def max_min(zahlen_liste: list):
    return {"max": max(zahlen_liste), "min": min(zahlen_liste)}

print(max_min([1,2,3,4,5,6]))

# Aufgabe 3
def berechne_end_vermoegen(vermoegen_anfang: int, zinssatz: float, jahre: int):
    vermoegen_ende = vermoegen_anfang * (1+zinssatz) ** jahre
    return vermoegen_ende

vermoegen_ende = berechne_end_vermoegen(vermoegen_anfang=1000, zinssatz=0.05, jahre=15)
print(vermoegen_ende)