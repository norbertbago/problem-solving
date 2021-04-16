# Úloha: V texte nájdite všetky slová, které obsahujú podreťazec kos s jedným alebo viac znakmi o.

import re

string = """
ks
kooos
ojkooos
zkos
los
kostra
kosti
koosatka
kosmetika
keramtika
karimatka
"""

result = re.findall(r'.*ko+s.*',string, re.MULTILINE)

print(result)
