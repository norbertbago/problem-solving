print(abs(-1.455))
print(all([True, False]))
print(all([0,5,6]))
print(any([0,5,6]))
print(any([True, False]))
print(ascii("\n"))
print(bin(3))


print(sorted([4,6,3,2,1]))
print(list(zip([1,4,5],["one", "two", "three"])))
print(round(1.4))
print(list(reversed([4,7,2])))
print(bool(1))
print(bool(4))
print(bool(0))
print(ord("c"))
print(chr(99))
print(type(14))
t1 = tuple()
print(t1)
t2 = tuple('Python')
print(t2)
t3 = tuple([1,2,3])
print(t3)

# n = input("AHOJ: ")
# print(n)

a = slice(1,2,3)
print("ahoj"[a])

a = "ahoj"
a = dir(a)
print(a)

a = divmod(5, 3)
print(a)

x = 1
print(eval('x + 1'))


print(format(123, "f"))

a = [1,2,3,4,5,6,7,8,9]
print(a.index(5))

b = a.copy()
print(b)

b.reverse()
print(b)

b.pop()
print(b)

b.remove(5)
print(b)

b.insert(5, 2)
print(b)

a.extend(b)
print(a)

a.sort()
print(a)

a.clear()
print(a)



