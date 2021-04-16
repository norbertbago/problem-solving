# Značka \d = zodpovedá desiatkovej číslici, napr. a\db zodpovedá a2b, ale nie axb.
# Úloha:Vyberte vety, ktoré obsahujú trojciferné alebo viacciferné číslo.

import re 

string = """
Ahoj, číslo 5!
Já mám 20 kôz.
Já mám 3567 slonov!
Na výlete bolo 43 chlapcov.
Vyhral som 300 korún!
Vyhrál jsem 50 korún!
Maratón má 42 kilometrov.
Brno má 380 tisíc obyvateľov.
Najmenšie trojciferné číslo je 100.
Znojmo má 33 tisíc obyvateľov.
Česko má desať miliónov obyvateľov.
"""

result = re.findall(r'.*\d\d\d.*',string, re.MULTILINE)

print(result)