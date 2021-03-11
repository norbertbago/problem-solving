# Problem Solving Challange: Vowel Count

str = "All cows eat grass"

def VowelCount(str):
    vowel = "aeiou"
    count = 0

    for letter in str:
        if letter in vowel:
            count += 1

    return count

print(VowelCount(str))
