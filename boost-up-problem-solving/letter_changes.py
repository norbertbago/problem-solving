# Problem Solving Challange: Letter Changes

word  = "Ahoj"
word1 = "Zajtra"

def LetterChanges(word):

    new_word = ""

    for letter in word:
        if letter == "z":
            new_word += "a"
        elif letter == "Z":
            new_word += "A"
        else:
            new_word += chr(ord(letter)+1)

    return new_word


print(LetterChanges(word))
print(LetterChanges(word1))
