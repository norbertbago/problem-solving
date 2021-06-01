def palindrome(string):
    return string == string[-1::-1]
    
print(palindrome("bob"))