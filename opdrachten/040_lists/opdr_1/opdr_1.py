# Opdracht 1 lists
# Naam student:
# Groep:

mylist = ...
dict_1 = ...
dict_2 = ...
dict_3 = ...
dict_4 = ...

# Lijst aanmaken
personen = []

# 4 dictionaries met gegevens van personen
persoon1 = {"id": 0, "voornaam": "Emma", "achternaam": "Jansen"}
persoon2 = {"id": 1, "voornaam": "Liam", "achternaam": "Bakker"}
persoon3 = {"id": 2, "voornaam": "Sophie", "achternaam": "De Vries"}
persoon4 = {"id": 3, "voornaam": "Noah", "achternaam": "Peters"}

# Toevoegen van de dictionaries aan de lijst met een list-methode
personen.extend([persoon1, persoon2, persoon3, persoon4])

# Print de volledige naam van de 2e persoon
print(personen[0]["voornaam"], personen[0]["achternaam"])

