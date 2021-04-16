# Nájdite v údajoch všetky slová s dĺžkou aspoň 4 a maximálne 5.
import re

string = """
Pes
Kočka
Medvěd
Kočička
Rys
Užovka
Kozel
Ondatra
Zajíc
Krokodýl
Tučňák
Losos
"""

result = re.findall(r'^.{4,5}$',string, re.MULTILINE)

print(result)