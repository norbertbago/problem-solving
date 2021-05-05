strArr = ["5","4","6","E","1","7","E","E","3","2"]

def OffLineMinimum(strArr):
    currentNumbers = list()
    result = list()
    for idx,ch in enumerate(strArr):
        if ch.isnumeric():
            currentNumbers.append(int(ch))
        elif ch == "E":
            currentNumbers = sorted(currentNumbers)
            result.append(currentNumbers[0])
            currentNumbers.pop(0)
            
    return result   

print(OffLineMinimum(strArr))