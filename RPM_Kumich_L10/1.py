import re
from typing import List

# 1 задание
def is_valid_email(email):
    if bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)):
        return 'email соответствует шаблону'
    return 'email не соответствует шаблону'


print(is_valid_email('john_doe@example.com'))
print(is_valid_email('user.name-domain.co.uk'))

# 2 задание
def extract_dates(text: str) -> List[str]:
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)


print(extract_dates("Встреча 12-04-2023 и потом 15/05/2024"))

# 3 задание
def mask_numbers(text: str) -> str:
    return re.sub(r'\b\d+\.?\d*\b', '<num>', text)


print(mask_numbers("У него было 5 яблок и 3.14 пирога"))

# 4 задание
def is_strong_password(password: str) -> bool:
    if 8 >= len(password) <= 20:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%^&+=.]', password):
        return False
    return True


print(is_strong_password('pas'))
print(is_strong_password('Password1'))
print(is_strong_password('Password1@'))

# 5 задание
def extract_tags(html: str) -> List[str]:
    return re.findall(r'<\/?([a-zA-Z0-9]+)(?:>|\/)', html)


print(extract_tags("<div><p>Hello</p><br/></div>"))

# 6 задание
def find_repeated_words(text: str) -> List[str]:
    match = re.findall(r'\b(\w+)\s+\1\b', text)
    return list(dict.fromkeys(match))


print(find_repeated_words("This is is a test test test string"))

# 7 задание
def split_words(text: str) -> List[str]:
    return re.findall(r'\b[\w\-]+\b', text)


print(split_words("Hello, world! How are you?"))