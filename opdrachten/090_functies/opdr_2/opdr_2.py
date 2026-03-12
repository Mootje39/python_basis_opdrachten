# Opdracht 1 functies
# Naam student:
# Groep:

# opdr_2.py

# Functie: kilometers naar miles
def kilometers_naar_miles(km):
    return km / 1.609344

# Functie: miles naar kilometers
def miles_naar_kilometers(miles):
    return miles * 1.609344


# Voorbeeldgebruik
kilometers = 15000
miles = 2700

# Berekeningen
miles_resultaat = kilometers_naar_miles(kilometers)
km_resultaat = miles_naar_kilometers(miles)

# Output
print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {km_resultaat} kilometers")