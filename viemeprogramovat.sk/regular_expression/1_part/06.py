# Úloha: Nájdite slová začínajúce na „p“ a obsahujúce „r“.

import re 

strings = """
pudr
ovce
prase
kopec
pyramida
kapr
kopretina
provaz
puberta
zaparkovat
"""

result = re.findall(r'^p.r*.*',strings, re.MULTILINE)
print(result)