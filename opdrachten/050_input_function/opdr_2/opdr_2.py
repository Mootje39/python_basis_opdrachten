# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Jij", ... ]

# Stap 1: Maak de gastenlijst en voeg jezelf toe
gasten = ["Paul", "Kees", "Marie", "Hilda"]
gasten.insert(0, "Jij")  # Voeg jezelf als eerste toe
print(gasten)  # ["Jij", "Paul", "Kees", "Marie", "Hilda"]

# Stap 2: Marie gaat niet meer mee, verwijder haar uit de lijst
gasten.remove("Marie")
print(gasten)  # ["Jij", "Paul", "Kees", "Hilda"]

# Stap 3: George wil mee en naast Kees zitten
index_kees = gasten.index("Kees")  # Vind de positie van Kees
gasten.insert(index_kees + 1, "George")  # Voeg George direct na Kees toe
print(gasten)  # ["Jij", "Paul", "Kees", "George", "Hilda"]
