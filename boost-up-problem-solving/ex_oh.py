# Problem Solving Challange: ABCheck(str)

str = "xooxxxxooxo"

def ExOh(str):
    number_of_x = str.count("x")
    number_of_y = str.count("o")

    if number_of_x == number_of_y:
        return "true"
    else:
        return "false"

print(ExOh(str))
