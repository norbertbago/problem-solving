import re

string = "Ahoj, ako"

result = re.search(r'ako',string)
result1 = re.match(r'Ahoj', string)
result2 = re.findall(r'o', string)
result3 = re.finditer(r'o', string)


# print(result)
# print(result.group())  groups() use with () in regex
# print(result.start())
# print(result.end())
# print(result.span())

print(result1)
print(result2)

for i in result3:
    print(i.group(), i.start(), i.end())


a = 'no no no'
result4 = re.sub(r'(n)(o)','mu', a)
result5 = re.sub(r'(n)(o)','mu', a, count=2)

print(result4)
print(result5)


# re.split(r'[ ;:]')  - split on more character than single split method
# re.compile()

b = '144445 1444566665'
result6 = re.findall(r'1.*5', b)
print(result6)



# napad pre vyskusanie regular expression na vieme programovat 
# re.findall(r'[\d]{3}-[\d]{4}', text)