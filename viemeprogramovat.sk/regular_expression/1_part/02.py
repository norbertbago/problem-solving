# operator hviezdicka a bodka
import re

string = """
gogol
ggle
lego
gogle
doodle
gooooogle
goglagl
google
doogle
goooogle
ggg
go lee go
"""

result = re.findall(r'go*gle',string, re.MULTILINE)

print(result)
