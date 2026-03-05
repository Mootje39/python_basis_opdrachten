# Opdracht 1 while-loops
# Naam student: Mohamed Maghri
# Groep:

# opdr_1.py
# Enquete programma

def stel_vragen():
    print("Welkom bij de enquete!\n")

    antwoord1 = input("1. Wat vind je van de huidige regering? ")
    antwoord2 = input("2. Wat vind je van de Python-lessen tot nu toe? ")
    antwoord3 = input("3. Wat vind jij de mooiste stad van Nederland? ")

    return antwoord1, antwoord2, antwoord3


def sla_resultaten_op(regering, python_lessen, stad):
    with open("enquete_resultaten.txt", "a") as bestand:
        bestand.write("Nieuwe enquete:\n")
        bestand.write(f"Wat vind je van de huidige regering? {regering}\n")
        bestand.write(f"Wat vind je van de Python-lessen tot nu toe? {python_lessen}\n")
        bestand.write(f"Wat vind jij de mooiste stad van Nederland? {stad}\n")
        bestand.write("-" * 40 + "\n")


def main():
    regering, python_lessen, stad = stel_vragen()
    sla_resultaten_op(regering, python_lessen, stad)

    print("\nBedankt voor het invullen van de enquete!")
    print("De resultaten zijn opgeslagen in 'enquete_resultaten.txt'.")


# Start het programma
if __name__ == "__main__":
    main()