# operator bodka . berie znak 
import re 

strings = """
pes
Pardubice
prase
prsten
opqrs
dva prsty
nahrávka je pas
plná pusa
kopec
"""

result = re.findall(r'.*p.s.*', strings)
print(result)