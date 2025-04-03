# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om een lijst met 5 objecten (bijv. steden, games, voertuigen)
input_waarden = input("Voer minimaal 5 objecten in, gescheiden door een komma:\n> ")

# Zet de input om in een lijst en verwijder eventuele spaties rondom de woorden
objecten_lijst = [item.strip() for item in input_waarden.split(",")]

# Sorteer de lijst in omgekeerde alfabetische volgorde
objecten_lijst.sort(reverse=True)

# Print de gesorteerde lijst
print("\nGesorteerde lijst in omgekeerde volgorde:")
print(objecten_lijst)
