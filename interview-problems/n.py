# Write problme, that print this output with n = 3
# 1
# 1 2
# 1 2 3
# 1 2
# 1

n = 3

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
