def format_number(number):
    n = str(number)[-1::-1]
    result = ""
    while(len(n)>=3):
        if len(n)!=3:
            result = result + n[:3] + "," 
        else:
            result = result + n[:3] 
        n = n[3:]
    
    print(len(n))
    if len(n)!=0:
        result = result + n[:] 
    
    
    return result[-1::-1]
    
print(format_number(1000000))
print(format_number(100000))