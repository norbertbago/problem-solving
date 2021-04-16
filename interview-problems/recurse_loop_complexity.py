import timeit

def rec(n):
    if n == 0:
        return 1
    return n * rec(n - 1)


def not_rec(n):
    res = 1;
    for i in range(n, 1, -1):
        res *= i;
    return res

n = 50


print("Rekurzia: ", timeit.timeit(str(rec(n)), number=1))
print("Ne-rekurzia: ", timeit.timeit(str(not_rec(n)), number=1))