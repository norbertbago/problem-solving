# Operator . 

import re

string  = """kentaur
Pardubice
prase
tkanina
opqrs
Velikonoce
skonal
okenice
kopec"""

result = re.findall(r'.*k.n.*',string)
print(result)