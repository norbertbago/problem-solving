# Úloha: Vyberte práve otázky.

import re

string = """
Bylo to tak.
Jsem král!
Jsem král?
Mám radost;
Chci jíst!
Kde jsme?
Robinson
Kudy kam?
Malá dálka?
Symbol '?' se nazývá otazník.
Toto není otázka.
Španělé dávají obrácený ? na za začátek věty.
"""

result = re.findall(r'.*\?$.*',string, re.MULTILINE)

print(result)
