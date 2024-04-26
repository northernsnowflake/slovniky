import util
from random import randrange

def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače

    `pole` je herní pole, na které se hraje.
    `symbol` může být 'x' nebo 'o', podle toho jestli hráč hraje za křížky
    nebo za kolečka.
    """
    #správně a odevzdáno
    # if '-' not in pole:
    #     raise ValueError("Všechny pozice v poli jsou obsazené")
    # i = randrange(0,20)
    # while pole[i] != '-':
    #     i = randrange(0,20)
    # return util.tah(pole,i,symbol)

    #while True:
    if '-' not in pole:
        raise ValueError("Všechny pozice v poli jsou obsazené")
    i = randrange(0,20)
    #print(i)
    #print("-")
    while pole[i] != '-':
        if symbol == 'x' and 'xx' in pole: # pro x dvě vedle sebe (umísťuje 3.)
            i = pole.index('xx') - 1
            print(i)
            if pole[i] != '-':
                i = i + 3
        if symbol == 'o' and 'oo' in pole: # pro o dvě vedle sebe (umísťuje 3.)
            i = pole.index('oo') - 1
            if pole[i] != '-':
                i = i + 3
        if symbol == "x" and pole[i] == "x": # pro x vedle sebe (umísťuje 2.)
            #print(i)
            i = i + 1 # vpravo od původního
            if pole[i] != '-':
                i = i - 2 # vlevo od původního
                #print(i)
        if symbol == "o" and pole[i] == "o": # pro o vedle sebe (umísťuje 2.)
            #print(i)
            i = i + 1
            if pole[i] != '-':
                i = i - 2
                #print(i)
        else:
            i = randrange(0,20)
            #print(i)
    #print(pole)
    return util.tah(pole,i,symbol)
            #i = randrange(0,20)

    #Prochází všechny testy - tj. správně, ale ještě dodělám
    # while True:
    #     i = randrange(0,20)
    #     if '-' not in pole:
    #         raise ValueError("Všechny pole jsou obsazené")
    #     while pole[i] != '-':
    #         i = randrange(0,20)
    #     if pole[i] != 'o' or 'x':
    #         return util.tah(pole,i,symbol)
    #         #break
    #     else:
    #         raise ValueError(f"Pozice {i} v poli je obsazena")
    #         #i = randrange(0,20)


    # Možná správně
    # while True:
    #     pozice = randrange(0,20)
    #     if pole[pozice] != '-':
    #         while pole[pozice] != '-':
    #             pozice = randrange(0,20)
    #             break
    #     if pole[pozice] != 'o' or 'x':
    #         vyber_tahu_pocitace = util.tah(pole, pozice, symbol)
    #         return vyber_tahu_pocitace
    #     else:
    #         pozice = randrange(0,20)

#print(tah_pocitace('-ox-xo-xo--xxo------', 'x'))
#print(tah_pocitace('oooooooooooooooooooo', 'x'))
