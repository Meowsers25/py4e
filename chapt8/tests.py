# data structures are a way of organizing data in a computer
# variables are not collections
# a collection allows us to put many values in a variable

# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print('Blastoff!')
#
# friends = ['Luna', 'B', 'Sully']
# for friend in friends:
#     print('Happy New Year', friend)
# print('Done!')
#
# z = ['Luna', 'B', 'Sully']
# for x in z:
#     print('Happy New Year', x)
# print('Done!')

# friends = ['Luna', 'B', 'Sully']
# print(friends[1])

# strings are not mutable
# fruit = 'Banana'
# fruit[0] = 'B'
# print(fruit)

# lists are mutable
# lotto = [2, 14, 15, 10, 25]
# lotto[2] = 35
# print(lotto)
# print(len(lotto))  # length of list

# range function returns 0 up to/not including the num
# print(range(4))
# friends = ['Luna', 'B', 'Sully']
# print(len(friends))
# print(range(len(friends)))

# concatenate lists
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)

# list slicing
# t = [46, 34, 4, 2, 8, 5]
# print(t[1:3])  # up to but not including
# print(t[2:])
# print(t[:4])
# print(t[:])  # whole list

# build a list from scratch
# stuff = list()  # constructor form
# # print(stuff)
# stuff.append('book')
# stuff.append(99)
# print(stuff)
# stuff.append('cookie')
# print(stuff)

# in operator
# some = [2, 12, 35, 42, 76, 89]
# print(12 in some)
# print(15 in some)
# print(20 not in some)

# sort
# names = ['Luna', 'Sully', 'B']
# names.sort()
# print(names)

# built in functions for lists
# nums = [34, 23, 12, 45, 67, 39, 100, 33, 8, 5]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))
# print(sum(nums) / len(nums))

# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     total = total + value
#     count += 1
# average = total / count
# print('Average: ', average)

# this uses more memory because it stores the numbers
# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print('Average: ', average)

# strings and lists
# abc = 'With three words'
# # .split() splits the string into a list at the blanks spaces
# stuff = abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])
# for w in stuff:
#     print(w)

# split treats multiple spaces as one delimeter
# you can specify what delimeter to split at
# line = 'A lot of          spaces'
# etc = line.split()
# print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))
