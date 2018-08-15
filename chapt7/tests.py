# handle allows you to get to the file;
# it is not the file itself, and it it not the data in file
# fhand = open('mbox.txt')
# print(fhand)

# stuff = 'hello\nWorld'
# print(stuff)

# stuff = 'X\nY'
# print(stuff)
# # \n is a character
# print(len(stuff))  # 3 character string

# a file is a sequence of lines with \n at the end of each line
# use the for loop to iterate through the sequence
# xfile = open('mbox.txt')  # use quotations!!!!!
# # cheese is the iteration variable, it goes through each line
# for cheese in xfile:
#     print(cheese)  # for each line inn xfile, print line

# counting lines in a file
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count: ', count)

# # reading the 'whole' file
# fhand = open('mbox.txt')
# inp = fhand.read()  # reads whole file into a single string
# print(len(inp))
# print(inp[:20])  # prints first 20 characters

# searching through a file
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     if line.startswith('From:'):
#         line = line.rstrip()  # .rstrip takes away the whitespace
#         count = count + 1
#         print(line)
# print(count)

# skipping with continue
# this does the same as above code
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

# using 'in' to select lines
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)

# prompt for filename
# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count += 1
# print('There were', count, 'subject lines in', fname)

# dealing with bad file names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
