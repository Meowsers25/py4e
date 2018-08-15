# handle allows you to get to the file;
# it is not the file itself, and it it not the data in file
# fhand = open('mbox.txt')
# print(fhand)

# stuff = 'hello\nWorld'
# print(stuff)

stuff = 'X\nY'
print(stuff)
# \n is a character
print(len(stuff))  # 3 character string

# a file is a sequence of lines with \n at the end of each line
# xfile = open('mbox.txt')  # use quotations!!!!!
# for cheese in xfile:
#     print(cheese)

# file handle as a sequence
# xfile = open('mbox.txt')
# for cheese in xfile:  # cheese is the iteration variable, it goes through each line
#     print(cheese)  # for each line inn xfile, print line

# counting lines in a file
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count: ', count)

# reading the 'whole' file
# fhand = open('mbox.txt')
# inp = fhand.read()  # reads whole file into a single string
# print(len(inp))
# print(inp[:20])  # prints first 20 characters
