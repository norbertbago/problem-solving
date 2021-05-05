arr1 = [4,6,23,10,1,3]
arr2 = [3,6,23,10,1,3]

def ArrayAdditionI(arr):
    max_number = max(arr)
    arr.remove(max_number)
    print(sum(arr))
    if sum(arr) == max_number:
        return True
    else:
        return False

print(ArrayAdditionI(arr1))
print(ArrayAdditionI(arr2))