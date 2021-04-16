# Úloha: Nájdite slová, ktoré obsahujú písmená p a s, medzi ktorými je práve jedno písmeno a toto 
# písmeno je iné ako a.

import re 

string  = """
pes
pas
prase
Uppsala
pastelka
postel
sopka
opustit
ps
prsten
absence
dopis
psi
ptakopysk
egyptský
"""

result = re.findall(r'.*p[^a]s.*',string, re.MULTILINE)

print(result)