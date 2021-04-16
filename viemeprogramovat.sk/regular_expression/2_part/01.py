# # Úloha: Vyberte mestá, ktoré v názve obsahujú písmeno r nasledované jedným z písmen a alebo e.

import re

string = """
Pardubice
Praha
Brno
Ostrava
Olomouc
Zlín
Liberec
Opava
Bratislava
Košice
Poprad
"""

result = re.findall(r'.*r[ae].*',string, re.MULTILINE)

print(result)
