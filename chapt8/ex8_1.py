nums = [1, 2, 3, 4, 5, 6, 7, 8, 10]
# print(nums[-1])


# def chop(name):
#     for i in name:
#         name.pop(0) and name.pop(-1)
#     print(nums)


def middle(numbers):
    return numbers[1:-1]


new_arr = middle(nums)
print(new_arr)
