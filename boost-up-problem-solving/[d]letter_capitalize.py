# Problem Solving Challange: Letter Capitalize

sen = """If we do the right things consistently over a long period of time, the
future  we want becomes more and more inevitable because our action compound
upon one another."""

def LetterCapitalize(sen):

    new_sen = ""

    for word in sen.split():
        new_word = word[0].upper() + word[1:]
        new_sen  = new_sen + new_word + ' '

    return new_sen

print(LetterCapitalize(sen))
