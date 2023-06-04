import secrets
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Usage example
password = generate_password(length=16, include_special_chars=False)
print(password)
