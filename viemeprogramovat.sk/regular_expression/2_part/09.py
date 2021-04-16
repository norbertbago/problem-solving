# Úloha: v údajoch nájdite vety, ktoré obsahujú číslicu/skupinu číslic oddelenú 
# z oboch strán medzerou od ostatných znakov.

import re 

string = """
ahoj číslo 5!
Já mám 2x větší hlad.
Uviděl 100 rytířů řádu x
Uviděl 100 rytířů řádu y
Esi si 7x lepší
7 krát 7 je 7
2B OR NOT 2B
Až naprší 5 kapek a uschne.
U 5ti studní x
Už těm 100 zaměstnancům zaplatím!
"""

result = re.findall(r'.*\s\d*\s.*',string, re.MULTILINE)

print(result)