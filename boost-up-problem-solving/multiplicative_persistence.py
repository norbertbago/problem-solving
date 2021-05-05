import functools

num = 18

def MultiplicativePersistence(num):
    count = 0
    ls = list(str(num))
    while len(ls) > 1:
        n = functools.reduce(lambda x,y: int(x) * int(y), ls)
        ls = list(str(n))
        num = str(n)
        count += 1
    return count

print(MultiplicativePersistence(num))