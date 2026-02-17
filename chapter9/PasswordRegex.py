import re
from humre import *

def strong_password_detection(password: str) -> bool:
    """
    Docstring for strong_password_detection
    Returns True if:
        1. Password has at least 8 characters.
        2. Password has at least one uppercase letter, one lowercase letter and at least one digit.
    :param password: string
    """
    if len(password) < 8:
        return False
    lowercase_regex = re.compile(chars('a-z'))
    uppercase_regex = re.compile(chars('A-Z'))
    digit_regex = re.compile(DIGIT)

    lowercase_match = lowercase_regex.search(password)
    uppercase_match = uppercase_regex.search(password)
    digit_match = digit_regex.search(password)
    
    if lowercase_match and uppercase_match and digit_match:
        return True
    else:
        return False
    
print(strong_password_detection('TTTTTTTTTT4'))