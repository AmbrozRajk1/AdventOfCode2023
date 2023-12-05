content = [line.replace("\n","") for line in open("day1.txt", encoding="utf8").readlines()]

allValues = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']
num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

totalSum = 0
for line in content:
    key = []
    value = []
    for v in allValues:
        i = line.find(v)
        i2 = line.rfind(v)
        key.append(v)
        value.append(i)
        key.append(v)
        value.append(i2)

    max_value = -1
    min_value = 999999
    max_key = ''
    min_key = ''

    for i in range(len(key)):
        if value[i] >= 0 and value[i] < min_value:
            min_value = value[i]
            min_key = key[i]
        if value[i] >= 0 and value[i] > max_value:
            max_value = value[i]
            max_key = key[i]

    minint = 0
    maxint = 0
    if min_key.isdigit():
        minint = min_key
    else:
        minint = num[min_key]

    if max_key.isdigit():
        maxint = max_key
    else:
        maxint = num[max_key]

    together = str(minint) + str(maxint)
    togetherint = int(together)
    totalSum += togetherint

print(totalSum)
