# Úloha: Napíšte výraz, ktorým vyberiete zo zoznamu práve slová, ktoré obsahujú písmeno a a za ním
# o dve pozície ďalšie písmeno a.
import re 

strings = """
prezident
otec
matka
ukradl
zahrada
park
katakomba
stavba
parlament
karate
abeceda
fakta
"""

result = re.findall(r'.*a..a.*',strings, re.MULTILINE)
print(result)