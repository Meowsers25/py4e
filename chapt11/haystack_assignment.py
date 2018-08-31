import re

hand = open('regex_sum_123425.txt')
test_nums = list()
for line in hand:
    # line.rstrip() # works with no rstrip
    stuff = re.findall('[0-9]+', line)
    # print(stuff)
    for num in stuff:
        num = int(num)
        test_nums.append(num)
print(sum(test_nums))
