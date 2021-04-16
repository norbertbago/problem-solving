# Úloha: Nájdite slová, ktoré obsahujú písmeno zo začiatku abecedy (a, b, c) bezprostredne nasledované písmenom z konca 
# abecedy (x, y, z).

import re 

string = """
obraz
svetr
Max
abeceda
bylo
sanitka
koza
Bayern Mnichov
zima
encyklopedie
Hadamczik
azbuka
komnata
"""

result = re.findall(r'.*[abc][xyz].*',string, re.MULTILINE)

print(result)