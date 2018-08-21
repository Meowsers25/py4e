fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        print(words[1])
print('There were', count, 'lines in the file with From as the first word')


# There were 27 lines in the file with From as the first word
