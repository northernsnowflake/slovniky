# # 
# Napiš funkci pocet_znaku, která jako argument dostane řetězec a 
# vrátí slovník, ve kterém budou jako klíče jednotlivé znaky ze zadaného
# řetězce a jako hodnoty počty výskytů těchto znaků v řetězci.

#  Například: pocet_znaku("hello world") 
# vrátí {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
from collections import defaultdict 

def pocet_znaku(retezec):
    slovnik_znaku = defaultdict(int)
    for znak in retezec:
        slovnik_znaku[znak] += 1
    return slovnik_znaku

print(pocet_znaku("hello world"))