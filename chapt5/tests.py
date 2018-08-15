# n = 5
# while n > 0:
#     print(n)
#     n -= 1
# print("Blastoff!")
# print(n)
#
# x = 3
# while x > 0:
#     print("Lather")
#     print("Rinse")
#     x -= 1  # you need the iterator lol
# print("Dry Off")

# while True:
#     line = input("> ")
#     if line == 'done':
#         break
#     print(line)
# print("Done!")
#

# while True:
#     line = input("> ")
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print("Done!")

# Definite loops are for loops; they execute an exact number of times

for i in [5, 4, 3, 2, 1]:  # i is called the iteration variable
    print(i)
print("Blastoff!")

pets = ["Luna", "Beatrice", "Sully"]
for pet in pets:
    print("Hello,", pet)
print("Done")
