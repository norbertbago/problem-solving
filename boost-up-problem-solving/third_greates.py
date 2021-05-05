strArr1 = ["hello", "world", "before", "all"]
strArr2 = ["hello", "world", "after", "all"] 

def ThirdGreatest(strArr):
    new_strArr = sorted(strArr, key = len, reverse = True)
    print(new_strArr)
    return new_strArr[2]
    

print(ThirdGreatest(strArr1))
print(ThirdGreatest(strArr2))