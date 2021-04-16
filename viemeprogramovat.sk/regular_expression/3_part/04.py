# Úloha: Nájdite reťazce, ktoré obsahujú šesť písmen a za sebou.

import re 

string = """
aaaaaa
abcdabcd
bbaaaaaaccc
bbbbbbbbb
xxxaaaaaaxxaaaaaaxxx
ababababababababab
aaaaa
aaaaaaba
bbbbbbaaaabb
"""

result = re.findall(r'.*a{6}.*',string, re.MULTILINE)

print(result)
