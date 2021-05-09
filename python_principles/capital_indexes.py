def capital_indexes(string):
    list_string = []
    for i in range(len(string)):
        if string[i].isupper():
            list_string.append(i)
    return list_string

print(capital_indexes("HeLlO"))
            