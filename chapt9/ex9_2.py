fname = input('Enter a file: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)
days = dict()
for line in fhand:
    # print(line)
    line = line.rstrip()
    wds = line.split()
    # print(wds)
    if len(wds) != 0 and wds[0] == 'From':
        # print(wds[2])
        # for word in wds:
        days[wds[2]] = days.get(wds[2], 0) + 1
print(days)
