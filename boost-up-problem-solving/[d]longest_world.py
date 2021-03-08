# Problem Solving Challange: Longest Word 

sen = """If we do the right things consistently over a long period of time, the
future  we want becomes more and more inevitable because our action compound
upon one another."""

def LongestWord(sen):

    longest_word = ""
    longest_word_count = 0

    for word in sen.split():

        actual_word_count = 0

        for letter in word:
            if letter.isalpha():
                actual_word_count +=1
        if actual_word_count > longest_word_count:
            longest_word_count = actual_word_count
            longest_word = word

    return longest_word


print(LongestWord(sen))
