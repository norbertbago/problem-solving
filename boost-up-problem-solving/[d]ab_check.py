# Problem Solving Challange: ABCheck(str)

str  = "lane borrowed"
str1 = "lgne coraoweb"

def ABCheck(str):
    a_count = str.count("a")
    b_count = str.count("b")

    resul_a  = False
    resul_b  = False

    check_a_str = str

    for i in range(0, a_count+1):
        #print(check_a_str)
        if check_a_str[check_a_str.find("a")+4] == "b":
            result_a = True
        else:
            return False

        check_a_str = check_a_str[check_a_str.find("a")+1:]

    check_b_str = str[::-1]

    for i in range(0, b_count+1):
        #print(check_b_str)
        if check_b_str[check_b_str.find("b")+4] == "a":
            result_b = True
        else:
            return False

    return result_a and result_b


print(ABCheck(str))
print(ABCheck(str1))
