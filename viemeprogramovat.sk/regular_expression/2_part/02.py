# Úloha: Nájdite text, ktorý obsahuje samohlásku a alebo e.

import re 

string = """
ahoj pepo
Anička má velký hlad
Rytíř uviděl
Ale nelekl jsem se
Asi jsem byl kaput
7 krát 7 = 7
On přišel
Napršelo a uschlo
Již zmizl
Asi zaměstnancům zaplatím
"""

result = re.findall(r'.*a|e.*',string, re.MULTILINE)

print(result)