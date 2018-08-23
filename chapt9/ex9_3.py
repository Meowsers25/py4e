fname = input('Enter a file:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)
emails = dict()
for line in fhand:
    # print(line)
    line = line.rstrip()
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        emails[words[1]] = emails.get(words[1], 0) + 1
print(emails)
