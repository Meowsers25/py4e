fname = input('Enter file name: ')
fhand = open(fname)
new_lst = []
for line in fhand:
    ind_wd = line.split()
    for dere in ind_wd:  # iterates over each word
        # print(dere)
        if dere not in new_lst:
            new_lst.append(dere)
            new_lst.sort()
print(new_lst)
