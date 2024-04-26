# Na setkání jsme používali česko-anglický překladový slovník jako tenhle:

# {'Jablko': 'Apple', 'Knoflík': 'Button', 'Myš': 'Mouse'}
# Napiš funkci, která z česko-anglického slovníku (zadaného argumentem) 
# vytvoří slovník anglicko-český. Můžeš předpokládat že se každý anglický termín 
# ve slovníku vyskytuje max. jednou.

slovnik = {'Jablko': 'Apple', 'Knoflík': 'Button', 'Myš': 'Mouse'}

def anglicko_cesky(slovnik):
    obraceny = {}
    for klic, hodnota in slovnik.items():
        obraceny[hodnota] = klic
    return obraceny

print(anglicko_cesky(slovnik))
        
    