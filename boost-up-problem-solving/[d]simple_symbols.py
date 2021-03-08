# Problem Solving Challange: Simple Symbols

str  = "++d+===+c++==a"

def SimpleSymbols(str):

    true_or_false = True

    if len(str) < 3:
        return "false"

    for x in range(1,len(str)):
        if str[x].isalpha() and (str[x-1] != "+" or str[x+1] != "+"):
            flag = False

    if true_or_false:
        return "true"
    else:
        return "false"

print(SimpleSymbols(str))
