# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

# Vragenlijst
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Lijst om alle gasten op te slaan
feestgangers = []

while True:
    print("\nVul de vragenlijst in:")
    
    antwoorden = {}
    
    # Vragen genummerd weergeven
    for i in range(len(vragen)):
        print(f"{i+1}. {vragen[i]}")
        antwoord = input()
        
        if i == 0:
            antwoorden["voornaam"] = antwoord
        elif i == 1:
            antwoorden["achternaam"] = antwoord
        elif i == 2:
            antwoorden["drank"] = antwoord
        elif i == 3:
            antwoorden["eten"] = antwoord

    feestgangers.append(antwoorden)

    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")

    doorgaan = input("Wil je nog een gast toevoegen? (ja/nee): ")
    if doorgaan.lower() != "ja":
        break


# Opslaan in tekstbestand
with open("feestgangers.txt", "w") as bestand:
    for gast in feestgangers:
        bestand.write("----\n")
        bestand.write(f"voornaam: {gast['voornaam']}\n")
        bestand.write(f"achternaam: {gast['achternaam']}\n")
        bestand.write(f"drank: {gast['drank']}\n")
        bestand.write(f"eten: {gast['eten']}\n\n")
        bestand.write("----\n\n")

print("Gegevens zijn opgeslagen in feestgangers.txt")