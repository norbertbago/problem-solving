# Úloha: V údajoch nájdete vety, ktoré nezačínajú číslom a končia alfanumerickým znakom 
# (bez bodky alebo výkričníka).
import re

string = """
ahoj číslo 5!
Já mám 2x větší hlad
Uviděl 100 rytířů řádu x
Asi jsi 7x lepší!
Uviděl 100 rytířů řádu y
7 krát 7 je 7
2B OR NOT 2B
Až naprší 5 kapek a uschne.
U 5ti studní x
Už těm 100 zaměstnancům zaplatím!
"""

result = re.findall(r'^\D.*\w$',string, re.MULTILINE)

print(result)
