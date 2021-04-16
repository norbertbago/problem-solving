# Vyberte vety, ktoré obsahujú gól, pričom úvodné g môže byť veľké či malé a ó môže byť 
# písané s čiarkou i bez čiarky v ľubovoľnom počte výskytov.


import re 

string = """
Gól!
Tesne vedľa.
A je to goooool.
glum
Roh, hlavička, gól....
Glóbus
Tyčka, brvno, ... a nepadne a nepadne.
góoóoól
Gool je cool.
GLglggll
That is a remarkable goal!
"""

result = re.findall(r'.*(g|G)(o|ó)+l*.*',string, re.MULTILINE)

print(result)