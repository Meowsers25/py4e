# counting
# zork = 0
# print("Before: ", zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork += 1
#     print(zork, thing)
# print("After: ", zork)
#
# # summing
# zork = 0
# print("Before:", zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + thing
#     print(zork, thing)
# print("After:", zork)
#
# # Average
# count = 0
# sum = 0
# print("Before:", count, sum)
# for value in [9, 41, 12, 3, 74, 15]:
#     count += 1
#     sum = sum + value
#     print(count, sum, value)
# print("After:", count, sum, sum / count)
#
# # filtering
# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print('Larger', value)
# print("After")

# search using boolean
# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)

# smallest
smallest = None  # none is None!
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:  # 'is' demands equality in type and value; stronger than ==
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
# use 'is' for None types or booleans also 'is not'
