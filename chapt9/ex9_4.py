fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
hand = open(fname)
emails = dict()
for line in hand:
    line = line.rstrip()
    # print(line)
    wds = line.split()
    if len(wds) != 0 and wds[0] == 'From':
        emails[wds[1]] = emails.get(wds[1], 0) + 1
lgnum = None
lgemail = None
for x, z in emails.items():
    if lgnum is None or z > lgnum:
        lgemail = x
        lgnum = z
print(lgemail, lgnum)
# for wd in wds:
#     if
#     print(wd)
