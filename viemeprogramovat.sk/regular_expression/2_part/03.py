# Nájdite v údajoch všetky slová, ktoré obsahujú aspoň jeden zo znakov a, e, i, o, u.

import re 

string = """
ahoj
helou
aleš
krk
krtko
hlavolámek
hlt
prst
leporelo
srk
šnek
lesk
"""

result = re.findall(r'.*[aeiou].*',string, re.MULTILINE)

print(result)