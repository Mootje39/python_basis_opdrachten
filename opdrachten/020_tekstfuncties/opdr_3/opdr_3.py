# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

def kerstboom():
    """Geeft een lijst van strings terug met 1 kerstboom."""
    return [
        "    *    ",
        "   ***   ",
        "  *****  ",
        " ******* ",
        "*********",
        "   ***   ",
        "   ***   ",
        "   ***   ",
    ]

# Maak 5 kerstbomen naast elkaar
bomen = kerstboom()
for regel in bomen:
    print((regel + " ") * 6)
