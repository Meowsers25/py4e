import re

# hand = open('mbox-short.txt')
# i = 0
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:

#         i += 1
#         print(i)
#         print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('From: ', line):
#         print(line)

# strartswith
# hand = open('mbox-short.txt')
# i = 0
# for line in hand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         i += 1
#         print(i)
#         print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^From: ', line):
#         print(line)

# findall
# x = 'My 2 favorite numbers are 5 and 8'
# y = re.findall('[0-9]+', x)
# print(y)
# y = re.findall('[AEIOU]+', x)
# print(y)

# greedy matching
# x = 'From: Using the : Character'
# y = re.findall('^F.+:', x) # finds the longest match
# print(y)

# nongreedy matching
# x = 'From: Using the : Character'
# y = re.findall('^F.+?:', x) # ? means not greedy (shorter of strings)
# print(y)

# x = 'From: stephen.marquard@uct.ac.za Sat Jann 4 09:12:15 2018'
# y = re.findall('\S+@\S+', x)
# print(y)

# # fine tuning
# x = 'From stephen.marquard@uct.ac.za Sat Jann 4 09:12:15 2018'
# # line starts with From; the parens is the text you want extracted
# y = re.findall('^From (\S+@\S+)', x)
# print(y)

# data = 'From stephen.marquard@uct.ac.za Sat Jann 4 09:12:15 2018'
# atpos = data.find('@')
# print(atpos)
# sppos = data.find(' ', atpos)
# print(sppos)
# host = data[atpos + 1: sppos]
# print(host)

# # double split pattern
# data = 'From stephen.marquard@uct.ac.za Sat Jann 4 09:12:15 2018'
# words = data.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[0])
# # print(words)

# regex way
data = 'From stephen.marquard@uct.ac.za Sat Jann 4 09:12:15 2018'
y = re.findall('@([^ ]*)', data)
print(y)
