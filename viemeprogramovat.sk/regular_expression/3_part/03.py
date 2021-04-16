# Úloha: Nájdite slová, ktoré obsahujú opakované výskyty ba medzi dvoma písmenami c

import re

string = """
10101
10001
13001
20001
40000
555005
5050505
10000
23078000
"""

result = re.findall(r'.*0{3}.*',string, re.MULTILINE)

print(result)
