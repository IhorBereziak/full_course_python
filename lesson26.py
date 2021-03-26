def register(str):
    if ' ' in str:
        return str.upper()
    else:
        return str.lower()

s = 'Hello world'
res = register(s)
print(res)
print(register('Hello,world'))
#
# def get_sum(a, b):
#     return a + b
#
# x = 6
# y = 9
# get_sum(6, 9)
# get_sum(x, y)
# print(get_sum(x, y))
