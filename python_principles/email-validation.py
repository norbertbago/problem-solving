def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    
    # your code here
    for letter in string:
        if letter not in valid:
            return True
    return False

def domain_name(domain):
    domain_name, extension = domain.split(".")
    if len(domain_name) == 0 or len(extension) == 0:
        return False
    else:
        return True

def is_valid(email):
    try:
        prefix, domain = email.split("@")
        result1 = has_invalid_characters(prefix)
        result2 = has_invalid_characters(domain)
        result = result1 or result2
        domain1 = domain_name(domain)
    except:
        prefix = email.split("@")
        result = has_invalid_characters(prefix)
        domain1 = False
    


    at = email.count("@") 
    dot = email.count(".")
    if at == 1 and len(prefix) != 0 and dot == 1 and domain1 and not(result):
        return True
    else:
        return False
    
emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com"
]

for email in emails:
    if is_valid(email):
        print(email + " is valid")
    else:
        print(email + " is invalid")