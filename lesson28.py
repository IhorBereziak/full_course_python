# def get_sum(a, b):
#     """
#     Повертає суму аргументів a і b.
#
#     :param a: Перший операнд
#     :type a: int
#     :param b: Другий операнд
#     :type b: int
#     :return: Return type int
#     """
#     return a + b
#
# print(get_sum(1, 2))


a = 8  # global

# def f():
#     a = 12 # local
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)

# def f():
#     global a
#     a += 1
#
# print(a)
# f()
# print(a)

l = [1, '2', 5]

# def f(l):
#     return [i * 2 for i in l]
#
# print(f(l))

# def f2(l):
#     def get_mult(x):
#         return int(x) * 2
#     return [get_mult(i) for i in l]
#
# print(f2(l))

# def f3(l):
#     def get_mult(x):
#         if isinstance(x, int):
#             return int(x) * 2
#     return [get_mult(i) for i in l if get_mult(i)]
#
# print(f3(l))

def f4(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))

print(f4(l))