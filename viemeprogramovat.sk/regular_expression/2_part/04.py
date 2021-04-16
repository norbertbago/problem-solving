# Úloha: Nájdite slová, ktoré obsahujú jeden z podreťazcov sen, son, sin.

import re

string = """
kvasinka
svetr
Watson
odsun
prosinec
sanitka
Nissan
housenka
absence
zlosyn
"""

result = re.findall(r'.*s[eoi]n.*',string, re.MULTILINE)

print(result)
