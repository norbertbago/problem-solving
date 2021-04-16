# Úloha: Napíšte výraz, ktorým vyberiete zo zoznamu práve slová, ktoré v sebe 
# obsahujú všetky tri písmená a, b, c. Písmená musia byť v správnom poradí, nemusia 
# však byť tesne za sebou.

import re 

strings = """
abraka
dabra
Pardubice
ulice
krabice
scrabble
publikace
Jablonec
vrabec
arcibiskup
abeceda
stavebnice
"""

result = re.findall(r'.*a.*b.*c.*',strings, re.MULTILINE)
print(result)
