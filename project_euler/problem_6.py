# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

# Imperative programming in Python 

sum_i = 0
sum_of_square = 0

for i in range(1, 101):
    sum_of_square += i**2
    sum_i         += i

result = sum_i**2 - sum_of_square
print(result)     
    

# Functional programming in Python 
result = sum(range(1,101))**2 - sum(list(map(lambda x : x**2, range(1,101))))
print(result)


