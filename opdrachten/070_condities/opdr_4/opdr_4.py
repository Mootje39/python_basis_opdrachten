# opdr_5.py

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst van alleen de topping-namen
beschikbare_toppings = [t[0] for t in toppings]

# Vraag de gebruiker om een topping te kiezen
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze in de lijst staat
gevonden = False
for topping, prijs in toppings:
    if topping == keuze:
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        gevonden = True
        break

if not gevonden:
    print("Uw keuze zit niet in ons assortiment")
