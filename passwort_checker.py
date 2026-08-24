passwort = "geheim123@%&!"
punkte = 0

if len(passwort) >= 8:
    punkte += 2

for zeichen in passwort:
    if zeichen.isdigit():
        punkte += 1

    # optional
    if not zeichen.isalnum():
        punkte += 1


if punkte < 4:
    print("Schwaches Passwort")
elif punkte < 7:
    print("Mittelstark")
else:
    print("Starkes Passwort")