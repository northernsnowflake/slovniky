from random import randrange, choice

#pole = 'x-------------------'
#pozice = 10
#symbol = 'x'

def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici

    `pole` je herní pole, na které se hraje.
    `pozice` je číslo políčka. Čísluje se od nuly.
    `symbol` může být 'x' nebo 'o', podle toho jestli je tah za křížky
    nebo za kolečka.
    """
    #pozice = randrange(0,20)
    #symbol = choice("o""x")
    if pozice not in range(0,20):
        raise ValueError(f"Zadaná pozice {pozice} je mimo herní pole 0-19")
    if pole[pozice] != '-':
        raise ValueError(f"Pozice {pozice} v poli je již obsazena")
    if symbol != 'x' and symbol != 'o':
        raise ValueError(f"Symbol {symbol} není hrací symbol x ani o")
    else:
        nove_pole = pole[:pozice] + symbol + pole[pozice+1:]
        return nove_pole

#print(tah(pole, pozice, symbol))
#print(tah('--------------------', 0, 'x'))
#print(tah('--------------------', 19, 'o'))
#print(tah('x-o-x-o-x-o-x-o-x-o-', 1, 'o'))
