import re

# s = 'This is string text. And this is more string text. '
# pattern = 'string'

# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No match')
#
# match = re.search(pattern, s)
# print(match)
# print(match.span())
# print(match.start())
# print(match.end())

# print(re.match(pattern, s))
# print(re.findall(pattern, s))
# print(re.split(r'\.', s, 1))

# s = '''Это просто строка текста.
# А это ещё одна строка текста.
# А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
# А это строка с разными символами: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string'''

# pattern = r'\w+'
# print(re.findall(pattern, s))

# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[\da-]+'
# pattern = r'a\\b\tc'
# pattern = r'\w+$'
# print(re.findall(pattern, s))

def validate_email(email):
    return bool(re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE))

print(validate_email('gmail@gmail.com'))
print(validate_email('gmail@gmail.com.ua'))
print(validate_email('gmail@bank'))
print(validate_email('gmail@gmail.com.infocom'))

