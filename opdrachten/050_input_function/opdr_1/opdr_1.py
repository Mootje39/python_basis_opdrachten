# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

# Vraag de gebruiker om invoer
a = float(input("Geef de lengte van de eerste zijde\n> "))
b = float(input("Geef de lengte van de tweede zijde\n> "))

# Berekening volgens de stelling van Pythagoras
c = math.sqrt(a**2 + b**2)

# Toon het resultaat
print(f"\nDe lengte van de schuine zijde is: {c}")


