# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

# opdr_3.py

def encrypt(tekst):
    resultaat = ""

    for letter in tekst:
        # Controleer of het een kleine letter is
        if 'a' <= letter <= 'z':
            nieuwe_code = ord(letter) + 5
            if nieuwe_code > ord('z'):
                nieuwe_code -= 26
            resultaat += chr(nieuwe_code)

        # Controleer of het een hoofdletter is
        elif 'A' <= letter <= 'Z':
            nieuwe_code = ord(letter) + 5
            if nieuwe_code > ord('Z'):
                nieuwe_code -= 26
            resultaat += chr(nieuwe_code)

        # Andere tekens blijven hetzelfde
        else:
            resultaat += letter

    return resultaat


# Hoofdprogramma
tekst = input("Geef de tekst die wilt encrypten..\n")
versleuteld = encrypt(tekst)

print("\n" + versleuteld)

