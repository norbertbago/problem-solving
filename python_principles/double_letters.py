def double_letters(string):
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

print(double_letters("hello"))
print(double_letters("nono"))
print(double_letters("on and off"))