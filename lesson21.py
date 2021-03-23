# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = set('hello')
# s3 = {i for i in range(1, 11)}
# s4 = set()
# print(s, type(s))
# print(s2)
# print(s3)
# print(s4)

# nums = [1, 5, 9, 8, 8, 1, 6, 5, 8, 1]
# nums2 = list(set(nums))
# print(nums2)

# a = set('abracadabra')
# b = set('alacazam')
# c = a - b
# d = a | b
# e = a & b
# f = a ^ b
# print(a, b, c, d, e, f, sep='\n')

# s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# s2 = s.copy()
# print(s, id(s))
# print(s2, id(s2))

a = frozenset('hello')
print(a)