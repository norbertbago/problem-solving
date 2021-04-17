


import re 


string="""
Maxim-Turbulenc
Velká-Británie
Česká-republika
Dějiny-umění
Karel-IV
Velký-Pátek
Vítězný-oblouk
Myší-díra
"""

result = re.sub('(.*)-(.*)', '$2 $1', string)

print(result)
