arr  = [1,2,3,5,6]
arr1 = [1,2,3,4,5]
arr2 = [2,6,18,54]

def ArithGeo(arr):
    arith,geo = True, True
    for num in range(1, len(arr) - 1):
        if arr[num + 1] - arr[num] != arr[num] - arr[num-1]:
            arith = False
        if arr[num +1] / arr[num] != arr[num] / arr[num-1]:
            geo = False
    return "Arithmetic" if arith else "Geometric" if geo else -1

print(ArithGeo(arr))
print(ArithGeo(arr1))
print(ArithGeo(arr2))
