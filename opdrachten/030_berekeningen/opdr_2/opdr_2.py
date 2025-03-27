# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Celsius naar Fahrenheit
def celsius_naar_fahrenheit(c):
    return (c * 9/5) + 32

# Fahrenheit naar Celsius
def fahrenheit_naar_celsius(f):
    return (f - 32) * 5/9

# Gegeven waarden
c = -12
f = 102

# Berekeningen
f_converted = celsius_naar_fahrenheit(c)
c_converted = fahrenheit_naar_celsius(f)

# Resultaat weergeven
print(f"> {c} graden Celsius is gelijk aan {f_converted:.1f} graden Fahrenheit")
print(f"> {f} graden Fahrenheit is gelijk aan {c_converted:.1f} graden Celsius")

# Nieuwe set waarden
c = 62.2
f = 96

# Berekeningen
f_converted = celsius_naar_fahrenheit(c)
c_converted = fahrenheit_naar_celsius(f)

# Resultaat weergeven
print(f"> {c} graden Celsius is gelijk aan {f_converted:.1f} graden Fahrenheit")
print(f"> {f} graden Fahrenheit is gelijk aan {c_converted:.1f} graden Celsius")

exit

# Conversieformules
def celsius_naar_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_naar_celsius(f):
    return (f - 32) * 5/9

# Gegeven waarden
c = -12
f = 102

# Berekeningen en uitvoer
print(f"> {c} graden Celsius is gelijk aan {celsius_naar_fahrenheit(c):.1f} graden Fahrenheit")
print(f"> {f} graden Fahrenheit is gelijk aan {fahrenheit_naar_celsius(f):.1f} graden Celsius")

# Nieuwe waarden
c = 62.2
f = 96

print(f"> {c} graden Celsius is gelijk aan {celsius_naar_fahrenheit(c):.1f} graden Fahrenheit")
print(f"> {f} graden Fahrenheit is gelijk aan {fahrenheit_naar_celsius(f):.1f} graden Celsius")
