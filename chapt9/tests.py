# a list is a collection of values that stay in order
#  a dictionary is a bag of values each with its own label
# the order of items in a dictionary is unpredictable.
# you use the keys to look up the corresponding values
# in operator works on dictionaries;
# it tells you whether something appears as a key in the dictionary


# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)
# print(purse['candy'])
# purse['candy'] += 2
# print(purse['candy'])
#
# # dictionary literal
# iii = {'Chris': 46, 'Katie': 34}
# print(len(iii))

# ccc = dict()
# ccc['csev'] = 1
# ccc['cwev'] = 1
# print(ccc)
# ccc['cwev'] = ccc['cwev'] + 1
# print(ccc)

# counts = dict()
# names = ['Katie', 'Luna', 'B', 'Sully', 'Luna']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)

# counts = dict()
# names = ['Katie', 'Luna', 'B', 'Sully', 'Luna']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


# counting pattern
# counts = dict()
# print('Enter a line of text: ')
# line = input('')
# words = line.split()
# print('Words:', words)
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)

# definite loops and dictionaries
# counts = {'Luna': 4, 'B': 2, 'Sully': 2}
# for i in counts:
#     print(i, counts[i])

# retrieving lists of Keys and Values
# counts = {'Luna': 4, 'B': 2, 'Sully': 2}
# print(list(counts))  # prints keys
# print(counts.keys())  # also prints keys; notice difference
# print(counts.values())  # prints values
# print(counts.items())

# BONUS: two iteration variables
# exclusive to Python....elegant
# counts = {'Luna': 4, 'B': 2, 'Sully': 2}
# for x, z in counts.items():  # need 2 iteration vars and items()
#     print(x, z)


name = input('Enter a file: ')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for x, z in counts.items():
    if bigcount is None or z > bigcount:
        bigword = x
        bigcount = z
print(bigword, bigcount)
