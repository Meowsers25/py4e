sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
if fh > 40:
    oth = fh - 40
    regh = fh - oth
    otr = fr * 1.5
    print("You've earned", (oth * otr) + (regh * fr))
else:
    print("You've earned", fh * fr)
