x = 15
if x < 10:
    print("smaller")
if x > 20:
    print("bigger")
print("finis")


y = 42
if y > 1:
    print("Greater than 1")
    if y < 100:
        print("Less than 100")
print("Done")

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)
