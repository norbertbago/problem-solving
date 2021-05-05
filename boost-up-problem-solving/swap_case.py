str1 = "Hello World"
str2 = "Ahoj"

def SwapCase(str1):
    new_str = ""
    for letter in str1:
        if ord(letter) > 64 and ord(letter) < 91:
            new_str += chr(ord(letter)+32)
        elif ord(letter) > 91 and ord(letter) < 122:
            new_str += chr(ord(letter)-32)
        else:
            new_str += letter
            
    return new_str

print(SwapCase(str1))
print(SwapCase(str2))