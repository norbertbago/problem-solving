str1 = '454793'

def DashInsert(str1):
    number   = ""
    num_list = []

    for letter in str1:
        number += letter
        if int(number) % 2 > 0:
            num_list.append(number)
            number = ""
    return '-'.join(num_list)

print(DashInsert(str1))
    