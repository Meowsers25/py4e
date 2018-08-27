fhand = open('mbox-short.txt')
emails = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) != 0 and words[0] == 'From':
        # print(line)
        emails[words[1]] = emails.get(words[1], 0) + 1
# print(emails)
lst = list()
for k, v in emails.items():
    newtup = (v, k)
    lst.append(newtup)
    # print(newtup)
lst = sorted(lst, reverse=True)
# print(lst)
for v, k in lst[:1]:
    print(k, v)
