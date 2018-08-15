# zot = 'abc'
# print(zot[5])  # traceback error
#
# fruit = 'banana'
# print(len(fruit))  # len is a buuilt in function

# fruit = 'banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index += 1

#  prefer for loop
# fruit = 'banana'
# for letter in fruit:
#     print(letter)

# loop and count
# word = 'banana'
# count = 0
# for letter in word:  # letter is the iteration variable
#     if letter == 'a':
#         count += 1
# print(count)

# s = 'Monty Python'
# print(s[0:4])  # starts at 0 ang goes up to but NOT including 4
# print(s[6:7])
# print(s[6:20])
# print(s[:2])  # if first # left off, starts at beginning
# print(s[8:])  # if last number left off, goes to end
# print(s[:])   # both #s off, prints whole thing

# 'in' as a logical operator
# fruit = 'banana'
# print('n' in fruit)
# print('m' in fruit)
# print('nan' in fruit)
# if 'a' in fruit:
#     print('Found It!')

# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)
# print(greet)
# print('Hi There'.lower())

# stuff = 'Hello World'
# print(type(stuff))
# print(dir(stuff))

# fruit = 'banana'
# pos = fruit.find('na')
# print(pos)
# aa = fruit.find('z')
# print(aa)

# greet = 'Hello B'
# nn = greet.upper()
# print(nn)
# ww = greet.lower()
# print(ww)

# search and replace; replace replaces all instances
# greet = 'Hello B'
# rep = greet.replace('B', 'Luna')
# print(rep)
# new = greet.replace('o', 'X')
# print(new)

# remove whitespace
# greet = '    Hello World          '
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# prefixes
# greet = 'Please have a nice day'
# print(greet.startswith('Please'))
# print(greet.startswith('p'))

data = 'From katie.knochles@rfl.org Sun Aug 12 10:23:16 2018'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)  # finds the ' ' after the atpos position
print(sppos)
host = data[atpos+1: sppos]  # starts at atpos +1 and finishes but doesnt include the space
print(host)
