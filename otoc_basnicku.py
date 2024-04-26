
# Napiš program, který vypíše básničku ze souboru basnicka.txt,
# ale každé písmeno nahradí jiným podle následujícího slovníku:

# Znaky, které ve slovníku nejsou, program vypíše nezměněné.
# Nepovinný bonus: Každý řádek navíc vypiš pozpátku (od posledního písmena).
# (Který typ sekvencí umíte obrátit?)

slovnik = {'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u',
 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n',
 'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z', 'A': '∀', 'B': 'B',
 'C': 'Ɔ', 'D': 'D', 'E': 'Ǝ', 'F': 'Ⅎ', 'G': 'פ', 'H': 'H', 'I': 'I',
 'J': 'ſ', 'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ',
 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': '┴', 'U': '∩', 'V': 'Λ', 'W': 'M',
 'X': 'X', 'Y': '⅄', 'Z': 'Z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ',
 '4': 'ㄣ', '5': 'ϛ', '6': '9', '7': 'ㄥ', '8': '8', '9': '6', ',': "'",
 '.': '˙', '?': '¿', '!': '¡', '"': '„', "'": ',', '`': ',', '(': ')',
 ')': '(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<',
 '&': '⅋', '_': '‾'}

up_down = ''

with open('basnicka.txt', encoding = 'utf-8', mode = 'r') as soubor:
    for radek in soubor:
        #radek = radek.rstrip()
        for pismeno in radek:
            if pismeno not in slovnik:
                up_down = up_down + pismeno
                #continue
            else:
                up_down = up_down + slovnik[pismeno]
        #print('    ' + radek)
    #print()

print(up_down)
up_down_list = (list(up_down))
up_down_list.reverse()
#print(up_down_list)
print(''.join(up_down_list))