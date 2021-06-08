import timeit

n = 11

def function(columns):
    for i in range(1-columns, 2*columns):
        print(' '.join(map(str, range(1, columns-(abs(i))+1))))


def imperative(n):

    for i in range(1, 2*n):
        if i <=n:
            for j in range(1, i+1):
                print(j, end= ' ')
            print()
        else:
            for l in range (2*n-i, 0, -1):
                print(l, end=' ')
            print()

print("Function programming: ", timeit.timeit(str(function(n)), number=1))
print("Imperative programming: ", timeit.timeit(str(imperative(n)), number=1))