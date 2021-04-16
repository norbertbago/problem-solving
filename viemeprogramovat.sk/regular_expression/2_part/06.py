# Úloha: Nájdite slová, ktoré obsahujú písmeno s nasledované niekde neskôr k, pričom medzi nimi 
# sa vyskytujú iba písmená o alebo u.

import re 

string  = """
vysoko
prosakuje
soukromník
klasik
sukně
sanitka
vysoukat
Nagasaki
sokol
soukolí
kousek
"""

result = re.findall(r'.*s.*[ou].*k.*',string, re.MULTILINE)

print(result)