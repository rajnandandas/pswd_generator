# password_logic.py
import random
import string

def generate_password(length=12, symbols=True):
    chars = string.ascii_letters + string.digits
    if symbols:
        chars += "!@#$%^&*()"

    return "".join(random.choice(chars) for _ in range(length))
