fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        count += 1
        print(line)
print(count)
