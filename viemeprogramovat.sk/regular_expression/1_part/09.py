# Úloha: Napíšte výraz, ktorým vyberiete zo zoznamu práve slová „starosta“
# , „obstaral“, „kytaru“.

import re 

strings  = """
prezident
ministr
starosta
ukradl
obstaral
vynalezl
tank
kometu
kytaru
karate
"""

result = re.findall(r'.*tar.*',strings, re.MULTILINE)
print(result)