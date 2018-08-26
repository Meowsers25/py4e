fhand = open('mbox-short.txt')
emails = dict()
for line in fhand:
    line = line.rstrip()

    if line != 0 and line.startswith('From'):
        print(line)
