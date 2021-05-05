import pandas as pd 

df = pd.read_csv('tabulky-olympiada.csv')

# Koľko bolo celkom udelených zlatých medailí?
print('Celkovo bolo ' + str(df['Zlato'].sum()) + ' medaili')

# Koľko krajín získalo viac ako jednu, ale menej ako 10 bronzových medailí?
print(df[(df['Bronz'] > 1) & (df['Bronz'] < 10)]['Bronz'].count())

# Česko získalo spolu 10 medailí. Koľko krajín získalo viac ako 10 medailí?
print(df[df.sum(axis=1)>10].count()['Země'])

# Jedna krajina získala o 3 strieborné medaile viac, ako je súčet jej zlatých a bronzových medailí. 
# O ktorú krajinu ide?
