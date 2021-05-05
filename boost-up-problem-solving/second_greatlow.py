arr = [7, 7, 12, 98, 106]

def SecondGreatLow(arr):
    arr.sort()
    second_great = arr[-2]
    second_low   = arr[2]

    return str(second_great) + ' ' + str(second_low)

print(SecondGreatLow(arr))