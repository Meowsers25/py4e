# debugging examples from text
# fhand = open('mbox-short.txt')
# for line in fhand:
#     words = line.split()
#     print('Debug: ', words)
#     if words[0] != 'From':
#         continue
#     print(words[2])

# guardian code
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print 'Debug:', words
#     if len(words) == 0:
#         continue
#     if words[0] != 'From':
#         continue
#     print(words[2])

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     # print 'Debug:', words
#     # using 'and'
#     if len(words) != 0 and words[0] == 'From':
#         print(words[2])

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    # using 'or'
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[2])
