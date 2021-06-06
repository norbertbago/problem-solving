from functools import reduce

# Structured/Procedular Programming
# Object-Oriented Programming 
# Functional Programming 
# Logic Programming 

# Using Function as value

def cal(f, x, y):
    return f(x, y)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

print(cal(add, 5, 1))
print(cal(sub, 5, 1))

# With lambda 

print(cal(lambda x,y: x+y, 6, 1))
print(cal(lambda x,y: x-y, 6, 1))


a = [6, 1]
print(reduce(lambda x,y: x + y, a))
print(reduce(lambda x,y: x - y, a))


# Make it functional 
b = [1,2,3,5]
c = ["ahoj", "hi"]

def inc(x):
    return x + 1

print(list(map(inc, b)))
print(list(map(lambda x: x + 1, b)))
print(list(map(len, c)))

# Map implementaiton - own soluton

def my_map(fac, elements):
    return [fac(element) for element in elements]

print(my_map(inc, b))

# filter 
print(list(filter(lambda x: len(x) > 2, c)))

# reduce 
print(reduce(lambda a, b: a + b, b))

