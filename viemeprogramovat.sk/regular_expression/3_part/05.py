# Úloha: Nájdite reťazce, ktoré obsahujú sekvenciu písmen x, y, z. Písmená sa musia 
# vyskytovať v správnom poradí a mať 4-6 výskytov.

import re 

string = """
cbabac
xyz
xxxxxyyyyyzzzzz
yyyyyxxxxxxzzzzzz
xxxxyyyyyzzzzzz
xxxyyyzzzxxxyyyzzz
xxxxxxyyyzzzzzz
xxxxxxyyyyzzzz
abcxxxxxyyyyzzzzdef
xxxxxxxxxxyyyyyyyyyyyyyyzzzzzzzzzzz
"""

result = re.findall(r'.*x{4,6}y{4,6}z{4,6}.*',string, re.MULTILINE)

print(result)