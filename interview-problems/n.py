# Write problme, that print this output with n = 3
# 1
# 1 2
# 1 2 3
# 1 2
# 1

# /} bago.solution


columns = 3

for i in range(1-columns, 2*columns):
    print(' '.join(map(str, range(1, columns-(abs(i))+1))))


for i in range(0-n,n):
    print(''.join(str(x)+" " for x in range(1,(columns-(abs(i))+1))))


def printn(n):
    for i in range(1, 2*n):
        if i <=n:
            for j in range(1, i+1):
                print(j, end= ' ')
            print()
        else:
            for l in range (2*n-i, 0, -1):
                print(l, end=' ')
            print()

printn(n)

# Edit solution
def printn1(n):

    for i in range(1, 2*n):
        if i <=n:
            for j in range(1, i+1):
                print(j, end= ' ')
            print()
        else:
            for l in range (1, 2*n-i):
                print(l, end=' ')
            print()


# Best solution
def printn3(n):
  for i in range(1,2*n):
    print(''.join(str(x) for x in range(1,i+1 if i<=n else 2*n-i+1)))
