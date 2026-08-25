kapital = 1000
zinssatz = 0.05
jahre = 0

while kapital < 2000:
    kapital *= 1 + zinssatz
    jahre += 1
    print(f"Im Jahr {jahre} ist das Kapital {kapital}")

if jahre < 20:
    print(f"Weniger als 20 Jahre: {jahre}")

