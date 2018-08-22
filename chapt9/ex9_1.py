storage = dict()
fhand = open('words.txt')
for line in fhand:
    line.rstrip()
    words = line.split()
    for word in words:
        storage[word] = storage.get(word, 0) + 1
for key in storage:
    print(key, storage[key])
# print(storage)
