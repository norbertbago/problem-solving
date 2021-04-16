# Úloha: Nájdite slová, ktoré obsahujú opakované výskyty ba medzi dvoma písmenami c

import re

string = """
cbabac
jde baba jde
dddcbabababacccc
babababa
dcdcdcbababababacdc
bubaci
bacil bacil babacila
cbabacbabac
xxcbababababababac
cbababatadyjecalemocdaleko
"""

result = re.findall(r'.*c(ba)*c.*',string, re.MULTILINE)

print(result)
