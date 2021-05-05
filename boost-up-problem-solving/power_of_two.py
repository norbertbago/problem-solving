num1 = 16
num2 = 22

def PowersofTwo(num):
    result = str(num**0.5)
    result = result[result.index('.')+1:]
    result = int(result)
    return True if result == 0 else False

print(PowersofTwo(num1))
print(PowersofTwo(num2))