fhand = open('romeo.txt')
letters = dict()
for line in fhand:
    line.rstrip()
    words = line.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            letters[letter] = letters.get(letter, 0) + 1
            # print(letter)
# print(letters)
lst = list()
for k, v in letters.items():
    newtup = (v, k)
    lst.append(newtup)
# print(lst)
lst = sorted(lst, reverse=True)
# print(lst)
for v, k in lst:
    print(k, v)
