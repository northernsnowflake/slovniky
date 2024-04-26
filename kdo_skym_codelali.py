import json
import random

def ziskej_odpovedi():
    slovnik = {}
    kdo = str(input('Kdo?:'))
    skym = str(input('S kým?:'))
    codelali = str(input('Co delali?:'))
    kde = str(input('Kde?:'))
    kdy = str(input('Kdy?:'))
    proc = str(input('Proč?:'))
    seznam_klicu = ['kdo', 'skym', 'codelali', 'kde', 'kdy', 'proc']
    seznam_hodnot = [kdo, skym, codelali, kde, kdy, proc]
    for klic,hodnota in list(zip(seznam_klicu,seznam_hodnot)):
        if ',' in hodnota:
            slovnik[klic] = hodnota.split()
        else:
            slovnik[klic] = hodnota
    return slovnik
    #(f'{kdo} {skym} {codelali} {kde} {kdy} {proc}')


def vyber_odpovedi(vsechny_odpovedi):
    hodnoty = vsechny_odpovedi.values()
    for klic, hodnota in vsechny_odpovedi.items():
        if type(hodnota) == list:
            nahoda = random.choice(hodnota)
            vsechny_odpovedi[klic] = nahoda
    vybrane_odpovedi = vsechny_odpovedi
    return vybrane_odpovedi


def vypis_vysledek(vybrane_odpovedi):
    vytrizeny = {}
    #print(vybrane_odpovedi)
    for klic, hodnota in vybrane_odpovedi.items():
        print(f"{hodnota }", end =' ')
    return #(f'{kdo} {skym} {codelali} {kde} {kdy} {proc}')



vsechny_odpovedi = ziskej_odpovedi()
vybrane_odpovedi= vyber_odpovedi(vsechny_odpovedi)
vypis_vysledek(vybrane_odpovedi)
