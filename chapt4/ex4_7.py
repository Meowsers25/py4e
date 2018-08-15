def computegrade(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


grade = input("Enter Score: ")
try:
    num = float(grade)
except:
    print("Bad Score")
    quit()
if num >= 1:
    print("Bad Score")
    quit()
ans = computegrade(num)
print(ans)
