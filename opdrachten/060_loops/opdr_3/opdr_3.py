# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = []

# Maak een lege lijst om de resultaten op te slaan
resultaten = []

# Gebruik een for-loop en range van 3 tot 81, met een stap van 3
for i in range(3, 82, 3):
    # Bereken het kwadraat van het getal en deel het door 3
    resultaat = (i ** 2) / 3
    # Voeg het resultaat toe aan de lijst
    resultaten.append(resultaat)

# Print de lijst met resultaten
print(resultaten)
