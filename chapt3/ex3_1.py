sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)
if fh > 40:
    oth = fh - 40
    regh = fh - oth
    otr = fr * 1.5
    print("You've earned", (oth * otr) + (regh * fr))
else:
    print("You've earned", fh * fr)
