# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = []

# Stap 1: De oorspronkelijke lijst pizza's
pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Stap 2: Sorteer de lijst op alfabet
pizza_lijst.sort()
print(pizza_lijst)  # ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi']

# Stap 3: Voeg een pizza naar keuze toe
pizza_lijst.append('yo-favorito')
print(pizza_lijst)  # ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi', 'yo-favorito']

# Stap 4: Verwijder de pizza die je het minst lekker vindt (bijvoorbeeld 'olivio')
pizza_lijst.remove('olivio')
print(pizza_lijst)  # ['calzone', 'margharita', 'quattro stagioni', 'verdi', 'yo-favorito']

# Stap 5: Print de eerste 3 pizza's
print(pizza_lijst[:3])  # ['calzone', 'margharita', 'quattro stagioni']

# Stap 6: Print alleen de middelste pizza uit de lijst
print(pizza_lijst[len(pizza_lijst) // 2:len(pizza_lijst) // 2 + 1])  # ['quattro stagioni']

# Stap 7: Print de laatste 3 pizza's
print(pizza_lijst[-3:])  # ['quattro stagioni', 'verdi', 'yo-favorito']
