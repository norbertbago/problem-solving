def middle_letter(string):
    lenght = len(string)
    if lenght%2 == 0:
        return ""
    else:
        return string[lenght//2]

print(middle_letter("abc"))
