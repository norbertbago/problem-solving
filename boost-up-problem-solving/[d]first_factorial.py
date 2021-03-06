# Problem Solving Challange 2: Factorial

num = 4

def FirstFactorial(num):
    if num == 1:
        return num * num
    else:
        return num*FirstFactorial(num-1)

def FirstFactorial1(num):

    fac = 1

    for i in range(1, num + 1):
        fac = fac * i

    return fac

print(FirstFactorial(num))
print(FirstFactorial1(num))
