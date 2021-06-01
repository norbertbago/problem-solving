def only_ints(x, y):
    if type(x) == int and type(y) == int:
        return True
    else:
        return False
        
print(only_ints(1,4))