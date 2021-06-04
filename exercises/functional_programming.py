from functools import reduce
# map funcction in python 

numbers = [1,2,3,4,5,6]

def return_power(number, power=2):
    return number**power

print(list(map(return_power, numbers)))
print(list(map(lambda number: number**3, numbers)))
print(list(map(lambda x: (x, -x), numbers)))

# filter 

def is_even(n):
    return n%2 == 0

print(list(filter(is_even, numbers)))
print(list(filter(lambda x: x%3 == 0, numbers)))
print(list(filter(lambda x: x%3 == 0 and x%7 == 0, range(0, 100))))

# reduce 

def reduce_sum(a, b):
    return a + b

print(reduce(reduce_sum, numbers))
print(reduce(lambda x,y: x + y, numbers))

# factorial imperative 

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1

print(factorial(5))

# factorial functional programming 
print(list(map(lambda x: reduce(lambda y,z : y*z, range(1, x+1)),numbers)))


