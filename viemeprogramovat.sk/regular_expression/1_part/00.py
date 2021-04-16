# tranning regular expression 
import re

string = """ahoj
nazdar
zdravíčko
dobrý den
buenos dias
ahoj
čest
tě pic
servus
ahoj
čágo bágo
buenos dias"""

result = re.findall(r'ah.*', string)
print(result)