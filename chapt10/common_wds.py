fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    # print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# print(counts)
lst = list()
for k, v in counts.items():
    newtup = (v, k)
    lst.append(newtup)
    # print(newtup)

lst = sorted(lst, reverse=True)
# print(lst)

for v, k in lst[:10]:
    print(k, v)
