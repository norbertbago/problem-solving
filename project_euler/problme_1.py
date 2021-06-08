# Find the sum of all the multiples of 3 or 5 below 1000.

list1 = list(range(1000))

def find_sum_multiples(n):
    result = 0
    for i in n:
        if i%3 == 0 or i%5 == 0:
            result +=i
    return result

print(find_sum_multiples(list1))

# functional paradigma 

def five_or_three(number):
    return number%3 == 0 or number%5 == 0

print(sum(list(filter(five_or_three,list1))))
print(sum(list(filter(lambda x:x%3 ==0 or x%5 == 0,list1))))