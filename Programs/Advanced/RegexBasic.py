
import re

def validate_email(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

text = "To email Guido, try guido@gmail.com"
print(validate_email(text))

