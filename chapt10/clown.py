fname = input('Enter a file: ')
if len(fname) < 1:
    fname = 'clown.txt'
fhand = open(fname)
di = dict()
for words in fhand:
    words.rstrip()
    word = words.split()
    # print(word)
    for wd in word:
        di[wd] = di.get(wd, 0) + 1
# print(di)
li = list()
for k, v in di.items():
    newtup = (v, k)
    li.append(newtup)
li = sorted(li, reverse=True)
# print(li[:5])
for v, k in li[:5]:
    print(k, v)
