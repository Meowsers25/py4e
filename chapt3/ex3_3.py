score = input("Enter Score: ")
try:
    num = float(score)
except:
    print("Pick a number, fool!")
    quit()
if num >= 0.9:
    print("A")
elif num >= 0.8:
    print("B")
elif num >= 0.7:
    print("C")
elif num >= 0.6:
    print("D")
else:
    print("F")
