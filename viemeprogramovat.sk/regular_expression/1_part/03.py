# operator hviezdicka * berie vsetko 
import re

strings = """
prase
koza
krokodýl
velbloud
konipas
velryba
slon
orangutan
kočkodan
strakapoud
ondatra
"""

result = re.findall(r'.*o.*.a.*', strings)
print(result)