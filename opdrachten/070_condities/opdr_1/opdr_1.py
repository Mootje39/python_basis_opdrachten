# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

my_list = []

# for loop
for i in range(3):
    lengte = float(input("Geef een lengte van een zijde: "))
    my_list.append(lengte)

# if statement
# Sorteer de lijst zodat de grootste waarde (hypotenusa) achteraan staat
my_list.sort()

if my_list[0]**2 + my_list[1]**2 == my_list[2]**2:
    print("Dit is een rechthoekige driehoek.")
else:
    print("Dit is geen rechthoekige driehoek.")
