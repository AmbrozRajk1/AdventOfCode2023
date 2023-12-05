content = [line.replace("\n","") for line in open("day1.txt", encoding="utf8").readlines()]

totalSum = 0
for line in content:
    firstdigit = ""
    seconddigit = ""
    for e in line:
        if e.isdigit():
            if firstdigit == "":
                firstdigit = e
            else:
                seconddigit = e
    if seconddigit == "":
        seconddigit = firstdigit
    together = firstdigit + seconddigit
    togetherint = int(together)
    totalSum += togetherint

print(totalSum)
