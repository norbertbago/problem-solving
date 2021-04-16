# Úloha: Vyberte práve otázky.

import re

string = """
Bolo to tak.
Som kráľ!
Som kráľ?
Mám radosť;
Chcem jesť!
Kde sme?
Robinson
Odkiaľ kam?
Malá vzdialenosť?
Veľká vzdialenosť.
Ešte kúsok.
No dobre!
"""

result = re.findall(r'.*\.$|!$',string, re.MULTILINE)

print(result)
