# Problem Solving Challange: Simple Adding

num  = 1000
num1 = 5

def SimpleAdding(num):

    start = 1
    end  = num
    sum_num = 0

    for i in range(start, end+1):

        sum_num += i

    return sum_num


print(SimpleAdding(num))
print(SimpleAdding(num1))
