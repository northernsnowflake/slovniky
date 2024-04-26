# Napiš proceduru, která vypíše obsah slovníku (klíče a k nim náležící hodnoty) na
# jednotlivé řádky.

# Například vypis_slovnik(mocniny(4)) vypíše

# Klíč 1, hodnota 1
# Klíč 2, hodnota 4
# Klíč 3, hodnota 9
# Klíč 4, hodnota 16

def mocniny(n):
    slovnik = {}
    for cislo in range(1,n+1):
        slovnik[cislo] = (cislo**2)
    return slovnik

def vypis_slovnik(slovnik):
    for klic,hodnota in slovnik.items():
        print(f"Klíč {klic}, hodnota {hodnota}")

vypis_slovnik(mocniny(4))