"""
More line of code
"""

# Code

import os


files = os.listdir('problem-solving/boost-up-problem-solving')

count = 0

for file in files:
    if file[0:3] == "[d]":
        count +=1

percentage = (count*100)/29

print(str(count) + "/29")
print(str(percentage) + "%")
