num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    # print(fval)
    except:
        print('Invalid Input')
        continue
    num = num + 1
    tot = tot + fval
# print('ALL DONE')
print(tot, num, tot / num)
