# Decorate
#     a sequence by building a list of tuples with one or more sort keys preceding the elements from the sequence,
# Sort
#     the list of tuples using the Python built-in sort, and
# Undecorate
#     by extracting the sorted elements of the sequence.

txt = 'but soft what light in yonder window breaks'
words = txt.split()
# print(words)
t = list()
for word in words:
    # builds tuples (())
    t.append((len(word), word))
# print(t)
t.sort(reverse=True)
# print(t)
res = list()
# builds list in decending order
for x, z in t:
    res.append(z)
print(res)
