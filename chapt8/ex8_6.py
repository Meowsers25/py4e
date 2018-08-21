nums = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    val = float(inp)
    nums.append(val)
maximum = max(nums)
minimum = min(nums)
print('Maximum:', maximum)
print('Minimum:', minimum)
