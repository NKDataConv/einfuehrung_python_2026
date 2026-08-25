spieler_hp = 100
drachen_hp = 80
spieler_angriff = 15
drachen_angriff = 10

def angriff_ausfuehren(hp, schaden):
    return hp-schaden

def ist_besiegt(hp):
    if hp <= 0:
        return True
    else:
        return False

while (not ist_besiegt(drachen_hp) and not ist_besiegt(spieler_hp)):
    drachen_hp = angriff_ausfuehren(drachen_hp, spieler_angriff)

    if not ist_besiegt(drachen_hp):
        spieler_hp = angriff_ausfuehren(spieler_hp, drachen_angriff)

    print(f"Der Drache hat noch {drachen_hp} HP, der Spieler hat noch {spieler_hp} HP")