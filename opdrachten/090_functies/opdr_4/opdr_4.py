# Opdracht 1 functies
# Naam student:
# Groep:

# opdr_4.py

def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        # gebruik filter om lege strings te negeren en join om correct te spacen
        naam = " ".join(filter(None, [persoon["voornaam"], persoon["tussenvoegsel"], persoon["achternaam"]]))
        print(naam)


# Voorbeeldlijst
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

# Functie aanroepen
volledige_naam(namen)