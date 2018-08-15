fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'):
        count += 1
        spt = line.find('0')
        ans = line[spt:]
        fans = float(ans)
        total = fans + total
        # print(total)
print('Average spam confidence:', total / count)
