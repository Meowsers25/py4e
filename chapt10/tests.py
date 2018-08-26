# tuples behave like lists
# use parentheses instead of brackets
# x = ('Luna', 'B', 'Sully')
# print(type(x))
# print(x[1])
# for name in x:
#     print(name)

# tuples are immutable
# for efficiency
# higher memory use
# can put tuple on left hand side of assignment
# (x, y) = (4, 'Luna')
# print(y)
# (a, b) = (98, 99)
# print(a)
# d = dict()
# d['csev'] = 2
# d['cwen'] = 3
# for (k, v) in d.items():
#     print(k, v)
# tups = d.items()
# print(tups)
# d = {'a': 1, 'c': 233, 'b': 10}
# print(d.items())
# print(sorted(d.items()))

# d = {'a': 1, 'c': 233, 'b': 10}
# for k, v in sorted(d.items()):
#     print(k, v)

c = {'a': 1, 'c': 233, 'b': 10}
temp = list()
for k, v in c.items():
    temp.append((v, k))
print(temp)
temp = sorted(temp, reverse=True)
print(temp)
