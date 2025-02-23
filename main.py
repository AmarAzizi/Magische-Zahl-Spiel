import random
print("Magische Zahl Spiel")
def spiel():
    print("""Wähle den Schwierigkeitsgrad:
    [1] Einfach:
    Du hast 7 Versuche und musst eine Zahl zwischen 0 und 100 erraten.
    [2] Normal:
    Du hast 9 Versuche und musst eine Zahl zwischen 0 und 500 erraten.
    [3] Schwer:
    Du hast 10 Versuche und musst eine Zahl zwischen 0 und 1000 erraten.
    [4] Extrem:
    Du hast 10 Versuche und musst eine Zahl zwischen 0 und 10000 erraten.""")

    while True:
        schwierigkeitsgrad_input = input()
        try:
            schwierigkeitsgrad = int(schwierigkeitsgrad_input)
            if schwierigkeitsgrad == 1:
                print("Schwierigkeitsgrad auf einfach gesetzt.")
                magische_zahl = random.randint(0, 100)
                versuche = 7
                break
            elif schwierigkeitsgrad == 2:
                print("Schwierigkeitsgrad auf normal gesetzt.")
                magische_zahl = random.randint(0, 500)
                versuche = 9
                break
            elif schwierigkeitsgrad == 3:
                print("Schwierigkeitsgrad auf schwer gesetzt.")
                magische_zahl = random.randint(0, 1000)
                versuche = 10
                break
            elif schwierigkeitsgrad == 4:
                print("Schwierigkeitsgrad auf extrem gesetzt.")
                magische_zahl = random.randint(0, 10000)
                versuche = 10
                break
            else:
                print(" ")
                print("Bitte eine Zahl zwischen 1 und 4 eingeben.")
        except ValueError:
            print("\nBitte eine gültige Zahl eingeben.")

    print("\nErrate die Zahl:\n")
 
    while True:
        zahl_input = input()
        try:
            zahl = int(zahl_input)
            if zahl == magische_zahl:
                versuche -= 1
                print("Du hast die Zahl erraten mit noch", versuche, "Versuchen übrig!")
                break
            elif zahl > magische_zahl:
                versuche -= 1
                if versuche == 0:
                    print("Du hast verloren, die geheime Zahl war:", magische_zahl)
                    break
                print("Die Zahl, die du erraten musst, ist KLEINER!")       
                print("Du hast noch", versuche, "Versuche übrig.\n")
            elif zahl < magische_zahl:
                versuche -= 1
                if versuche == 0:
                    print("Du hast verloren, die geheime Zahl war:", magische_zahl)
                    break
                print("Die Zahl, die du erraten musst, ist GRÖSSER!")        
                print("Du hast noch", versuche, "Versuche übrig.\n")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

while True:
    spiel()
    antwort = input("Möchtest du nochmal spielen? (ja/nein): ")
    if antwort.lower() != 'ja':
        break