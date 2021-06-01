def add_dots(string):
    new_string = ""
    for i in range(0, len(string)-1):
        new_string = new_string + string[i] + "."
    
    new_string = new_string + string[len(string)-1]
    return new_string
    
def remove_dots(string):
    new_string = ""
    for letter in string:
        if letter != ".":
            new_string += letter
    return new_string
        
print(add_dots("test"))
print(remove_dots("t.e.s.t"))