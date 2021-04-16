# Vyberte správne slová, ktoré obsahujú iba písmená z prvej polovice abecedy (t. j. od a po m).

import re

string = """
jsem
pak
lidem
bych
film
prostoru
vrstvy
jakmile
chceme
rozporu
hladce
prase
hledal
"""

result = re.findall(r'^[a-m]+$',string, re.MULTILINE)

print(result)