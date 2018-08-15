fname = input('Enter a filename: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    print(line.upper())
