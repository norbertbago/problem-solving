num1 = 8
num2 = 4

def CheckNums(num1,num2):
    if num1 == num2:
        return "true"
    elif num2 > num1:
        return "- 1"
    else:
        return "false"

print(CheckNums(num1,num2))
