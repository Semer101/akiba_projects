def minimum_length(password, length=8):
    if len(password) < length:
        return False
    else:
        return True

def uppercase_letters(password):
    for letter in password:
        if letter.isupper():
            return True
    return False

def lowercase_letters(password):
    for letter in password:
        if letter.islower():
            return True
    return False

def digits(password):
    for digit in password:
        if digit.isdigit():
            return True
    return False

def special_chars(password):
    for character in password:
        if character in "*!@&%$#":
            return True
    return False

def analyze_password(password, length=8):

    results = {
        "Minimum length": minimum_length(password, length),
        "Uppercase letters": uppercase_letters(password),
        "Lowercase letters": lowercase_letters(password),
        "Digits": digits(password),
        "Special characters": special_chars(password)
    }

    missing = []

    for requirement, passed in results.items():
        if not passed:
            missing.append(requirement)

    results["Missing requirements"] = missing
    return results
    

print(analyze_password("Admin123"))
print(analyze_password("Password!123", 10))
print(analyze_password("password"))
print(analyze_password("Abcdefghijklmnop1234567890!@#$%&*", 12))
print(analyze_password("Password!123", 5))