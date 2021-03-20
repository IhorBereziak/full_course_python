# words = ['мадам', 'топот', 'test', 'madam', 'world']
# worlds_polid = [word for word in words if word == word[::-1]]
# print(worlds_polid)

# my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']
# my_str_polid = []
# for world in my_str:
#    world_r = world.replace(' ', '').lower()
#    if world_r == world_r[::-1]:
#        my_str_polid.append(world_r)
# print(my_str_polid)

l = list(range(0, 10))
l2 = list('hello')

print(l)

s = '-'.join(map(str, l))
s2 = ','.join(l2)
print(s)
print(s2)
