fhand = open('mbox-short.txt')
emails = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        # print(words[5])
        hours = words[5]
        emails[hours[:2]] = emails.get(hours[:2], 0) + 1
# print(emails)
lst = list()
for k, v in emails.items():
    newtup = (k, v)
    lst.append(newtup)
lst = sorted(lst)
# print(lst)
for k, v in lst:
    print(k, v)
