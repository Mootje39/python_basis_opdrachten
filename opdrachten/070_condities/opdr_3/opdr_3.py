# opdr_3.py

normale_toegangsprijs = 12.50
kortings_percentages = { "baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30 }
leeftijd = { "baby": (0,2), "kinderen": (3,18), "volwassenen": (19,64), "ouderen": (65,150) }

# Vraag de leeftijd van de bezoeker
leeftijd_bezoeker = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal de groep
groep_bezoeker = ""
for groep, (laag, hoog) in leeftijd.items():
    if laag <= leeftijd_bezoeker <= hoog:
        groep_bezoeker = groep
        break

# Bereken de prijs
korting = kortings_percentages[groep_bezoeker]
prijs = normale_toegangsprijs * (1 - korting / 100)

# Toon de output
print(f"U behoort tot de groep {groep_bezoeker}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {prijs}")
