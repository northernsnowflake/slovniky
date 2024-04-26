import util
import ai
import json
#pole = '--------------------'

def vyhodnot(pole):
    # Vyhrál hráč s křížky
    if "xxx" in pole:
        #print('vyhrál hráč s křížky')
        return "x"
    # Vyhrál hráč s kolečky
    if "ooo" in pole:
        #print('vyhrál hráč s kolečky')
        return "o"
    if "-" not in pole:
        #print('remíza')
        return "!"
    else:
        #print('hra ještě neskončila')
        return '-'

#vyhodnot('xxooxoxxoxooxxoxxoxx')
#vyhodnot('xx--x-x-ox---oxxoxxo')

def tah_hrace(pole, symbol):
    """Zeptá se hráče na tah a vrátí nové herní pole

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    while True:
        pozice = input('Kam chceš hrát? ')
        try:
            pozice = int(pozice)
        except ValueError:
            print('Zadávej čísla')
            continue
        try:
            pole_s_tahem_hrace = util.tah(pole,pozice,symbol)
            return pole_s_tahem_hrace
        except ValueError:
            print('Tam nejde hrát ')


def piskvorky1d(pole):
    #pole = '--------------------'
    n = 0
    neco = []
    while '-' in pole:
        pole = tah_hrace(pole,'o')
        print(pole)
        #data[''].append(pole)
        neco.append(pole)
        enum = enumerate(neco)
        nazev = dict(enum)
        #print("neco: ", neco)
        jsonpole = json.dumps(nazev,ensure_ascii = False, indent = 2)
        #print("jsonpole: ", jsonpole)
        with open('stav.json', encoding = 'utf-8', mode = 'w') as soubor:
            #zapis.append(jsonpole)
            #data = enumerate([jsonpole])
            #stav = dict(data)
            #stav[n] = jsonpole
            #zapis['tah'] = pole
            print(jsonpole, file=soubor)

        #print(stav)
            # následující dva řádky pokud chceme vypsat po řádcích
            #for hodnota in zapis:
            #    print(hodnota, file=soubor)
        hodnoceni = vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break
        pole = ai.tah_pocitace(pole,'x')
        print(pole)
        hodnoceni = vyhodnot(pole)
        if hodnoceni == 'x':
            print("Gratuluji, hráči s křížky!")
            break
        if hodnoceni == 'o':
            print("Gratuluji, hráči s kolečky!")
            break
        if hodnoceni == '!':
            print("Díky za hru")
            break
#
#print(tah_hrace('o-------------------', 'x'))
