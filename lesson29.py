arr1 = ['even', 55, 'even', 2, 'even', 10, 'even', 4, 'even', 44, 'odd']
arr2 = ['even', 5, 'even', 25, 'even', 10, 'even', 49, 'odd']
arr3 = ['even', 100, 'even', 7, 'even', 6, 'odd']

# def odd_ball(arr):
#     # index = arr.index('odd')
#     # if arr.count(index):
#     #     return 'True'
#     # else:
#     #     return 'False'
#     # --------------------------
#     return arr.index('odd') in arr
#
# print(odd_ball(arr1))
# print(odd_ball(arr2))
# print(odd_ball(arr3))
# --------------------------------------------------------------
# def find_sum(n):
#     res = 0
#     for i in range(0, n + 1):
#        if i % 3 == 0 or i % 5 == 0:
#            res += i
#     return res
    # -----------------------------------------
#     sum_number = sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0)
#     return sum_number
#
# print(find_sum(5))
# ---------------------------------------------------
names = ['Ryan', 'Kieran', 'Mark', 'John', 'David', 'Paul']
def get_names(names):
    new_names = [name for name in names if len(name) == 4]
    return new_names

print(get_names(names))
