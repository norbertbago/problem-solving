# Nájdite v údajoch všetky správne utvorené české emaily (teda končiace .cz, so zavináčom atp.).

import re

string = """
jan.tleskac@letadlo.cz
vontove.stinadla.cz
kocici.pracka@.cz
@vkleci.sk
rychlonozka@rychle.sipy.cz
mirek.dusin3@gmail.com
cervenacek12@centrum.cz
bidlo@fbi.com
jindra7@centrum.cz
siroko@hluboko.co.uk
maznak@loupeznik.cz
tam@tam.cz
"""

result = re.findall(r'.*@.*.(.cz)$',string, re.MULTILINE)

print(result)