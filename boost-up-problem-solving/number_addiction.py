str1 = "88Hello 3World!"
str2 = "55Hello"
str3 = "5Hello 5"

def NumberSearch(str1):
    number   = ""
    list_num = []
    for letter in str1:
        if ord(letter) > 48 and ord(letter) < 58:
            number += letter
        elif number != "":
            list_num.append(int(''.join(number)))
            number = ""
    return sum(list_num)

print(NumberSearch(str1))
