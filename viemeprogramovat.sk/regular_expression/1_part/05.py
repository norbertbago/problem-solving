# zaciatok retazca ^  a konec retazca $
import re 

strings = """
krokodýl
ovce
kos
kráva
koza
křeček
okoun
kolibřík
žirafa
"""

# ^ for start word
result1 = re.findall("^ko.*", strings, re.MULTILINE)
# $ for end word 
result2 = re.findall('.*a$', strings, re.MULTILINE)
print(result1)
print(result2)