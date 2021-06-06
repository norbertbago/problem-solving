import itertools 
import operator 

print ("Printing the numbers repeatedly : ")  
print(list(itertools.repeat(25,5)))

# ------ 

count = 0

for i in itertools.cycle('AB'):
    if count > 3:
        break
    else:
        print(i, end=" ")
        count +=1

print()

# ---- 

for i in itertools.count(5,5):
    if i == 35:
        break
    else:
        print(i, end=' ')

print()

# ------- vynasoby stlpce

L1 = [1, 2, 3]
L2 = [2, 3, 4]

a, b, c = map(operator.mul, L1, L2)
print("Result:", a, b, c)
