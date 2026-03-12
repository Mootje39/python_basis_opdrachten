# Opdracht 1 functies
# Naam student:
# Groep:

# opdr_3.py
import math  # Nodig voor pi

# Functie: volume van een kubus
def kubus_vol(zijde):
    return zijde ** 3  # volume = zijde^3

# Functie: volume van een bol
def bol_vol(radius):
    return (4/3) * math.pi * (radius ** 3)  # volume = 4/3 * pi * r^3

# Voorbeeldgebruik
kubus = 25
bol = 14

# Berekeningen
kubus_volume = kubus_vol(kubus)
bol_volume = bol_vol(bol)

# Output
print(f"De inhoud van deze kubus is: {kubus_volume}")
print(f"De inhoud van deze bol is: {bol_volume}")