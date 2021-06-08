# Problem Solving Challange: Reverse string

input_str = "helloworld"

def FirstReverse(input_str):
    return input_str[::-1]

def FirstReverse1(input_str):

    rev_list = reversed(list(input_str))

    output_str = ''

    for i in rev_list:
        output_str += i

    return output_str

def FirstReverse2(input_str):

    output_str = ''

    i = len(input_str)
    y = 0

    while(i!=0):
        output_str += input_str[i-1]
        i -= 1

    return output_str


print(FirstReverse(input_str))
print(FirstReverse1(input_str))
print(FirstReverse2(input_str))

# functional paradigma

# first solution
print(''.join(list(input_str[i] for i in range(len(input_str)-1,-1,-1))))

# second solution
print(input_str[-1::-1])
