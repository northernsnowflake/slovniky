# Napiš funkci mocniny, která pro argumentem zadané číslo 
# n vytvoří a vrátí slovník, kde jako klíče budou čísla od jedné do n 
# a jako hodnoty k nim jejich druhé mocniny.

# Například: mocniny(4) vrátí {1: 1, 2: 4, 3: 9, 4: 16}
def mocniny(n):
    slovnik = {}
    for cislo in range(1,n+1):
        slovnik[cislo] = (cislo**2)
    return slovnik

print(mocniny(4))