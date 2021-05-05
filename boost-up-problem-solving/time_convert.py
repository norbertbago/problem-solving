# Problem Solving Challange: Time Convert

num = 63

def TimeConvert(num):
    return str(num) + " minutes is " + str(num/60) + " hours and " + str(num%60) + " minutes."

print(TimeConvert(num))
