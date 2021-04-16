# Správne informatické heslo začína číslom, končí slovom UNIX a má aspoň 12 znakov ;-). 
# Nájdite v prehľade hesiel také, ktoré pravidlo spĺňajú. (prosím neberte tento príklad 
# ako návod na tvorbu hesiel)

import re

string = """
1rootUNIX
Mám hladUNIX
99m8m_hladUNIX
123ROOT
Brno
Uv.-1sP
00k0pec_dol;UNIX
5neco_klesl0UNIX
UNIXantarktida15
Brno60300
1984jenej!UNIX
UNIX777354891
"""

result = re.findall(r'^\d.{7,}UNIX$',string, re.MULTILINE)

print(result)