# Check if a password is at least 8 characters, has atleast one upper and one lower letter.
import re

def validate_password(password):
    pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$'

    return bool(re.match(pattern, password))

password = input("Enter a password: ")

print(validate_password(password))

result = validate_password(password)