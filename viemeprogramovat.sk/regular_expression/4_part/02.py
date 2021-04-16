# Úkol: Nájdite slová, ktoré začínajú na pr.

import re

string = """
pravice
parta
prvek
kopr
prosinec
patka
kopretina
prsten
provoz
paruka
"""

result = re.findall(r'.*^pr.*',string, re.MULTILINE)

print(result)
