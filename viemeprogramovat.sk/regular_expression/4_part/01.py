# Úloha: Nájdite texty začínajúce veľkým A.

import re

string = """
ahoj pepo
Anička má velký hlad
Uviděl jsem rytíře
Ale nelekl jsem se
Asi jsem byl kaput
7 krát 7 je 7
On přišel
Napršelo a uschlo
Už odešel
Asi zaměstnancům zaplatím
"""

result = re.findall(r'.*^A.*',string, re.MULTILINE)

print(result)
