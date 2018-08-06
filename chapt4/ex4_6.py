# def computepay(time, rate):
#     if time > 40:
#         oth = time - 40
#         otr = oth * (rate * 1.5)
#         total = otr + (40 * rate)
#         print("Pay: ", total)
#     else:
#         print("Pay: ", time * rate)
#
#
# computepay(45, 10)


def computepay(time, rate):
    if time > 40:
        oth = time - 40
        otr = oth * (rate * 1.5)
        total = otr + (40 * rate)
        return total
    else:
        return time * rate


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
xp = computepay(fh, fr)
print("Pay:", xp)
