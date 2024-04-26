# slovniky
<!-- 
Rozšíření ke hře piškvorky.

#Využij soubory a formát JSON pro ukládání informací v programech, které už máš hotové.
Vyber si jednu hru, kterou už máte naprogramovanou: Piškvorky nebo Šibenici .
Po každém tahu hru hráče ulož: stav hry převeď na JSON a uložte do souboru stav.json. --> -->

<!-- Při spuštění programu načti uložený stav ze souboru. Tedy:

Na začátku hry:
Pokud existuje soubor stav.json:
přečti ho a nastav podle něj stav hry.
Jinak hru začni normálně. -->

<!-- Když hra (nebo, u Šibenice, hádání jednoho slova) skončí, soubor stav.json odstraň, aby příští hra začala zase od začátku.

Na odstranění souboru můžeš použít funkci os.remove. POZOR: Funkce nepoužívá „odpadkový koš“ – daný soubor jednou provždy smaže:

import os
os.remove("stav.json") -->

