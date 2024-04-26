from piskvorky import piskvorky1d
import json
import os


if 'stav.json':
    #print('Existuje')
    soubor = {'':''}
    nic = json.dumps(soubor,ensure_ascii = False, indent = 2)
    with open('stav.json', encoding = 'utf-8', mode = 'w') as soubor:
        print(nic, file = soubor)


    with open('stav.json', encoding = 'utf-8') as soubor:
        nacteny_kod = soubor.read()

    #print(nacteny_kod)
    nactena_data = json.loads(nacteny_kod)

    for klic,hodnota in nactena_data.items():
        kolo = hodnota
    pole = kolo
    if pole == '':
        pole = '--------------------'
    print(pole)
    #print(nactena_data[-1])
    #for v in nacteny_kod.values():
    #    print(v)
    #print(nactena_data)
    #hodnoty = nactena_data.values()
    #print(hodnoty)
    #posledni_hodnota = hodnoty[-1]
    #print(posledni_hodnota)
    #print(nactena_data[-1])

    #pole = nacteny_kod[-1]
    piskvorky1d(pole)
    os.remove("stav.json")
        #for i in nacteny_kod:
        #    print(i, end='')
    #seznam = ''.join(nacteny_kod)
            #for prvek in seznam:
                #    seznam.append(prvek)
    #print(seznam)

    #slovnik = json.loads(seznam)
    #print(slovnik)
        #posledni = kod[-1]
        #print(posledni)
        #nactene_pole = json.loads(nacteny_kod)

else:
    pole = '--------------------'
    piskvorky1d(pole)
    os.remove("stav.json")

#pole = '--------------------'
#piskvorky1d(pole)
