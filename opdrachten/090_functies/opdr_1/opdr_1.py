# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(bestandsnaam, tekst):
    with open(bestandsnaam, "w") as bestand:
        bestand.write(tekst + "\n")


# voorbeeldgebruik
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"

write_to_file(my_file, my_tekst)
