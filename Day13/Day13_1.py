import numpy as np

content = open("day13.txt", encoding="utf8").read()
contentList = content.split('\n\n')
total = 0

for part in contentList:
    matrix_data = [list(line) for line in part.split('\n')]
    matrix = np.array(matrix_data)

    rowLen = matrix.shape[0]
    colLen = matrix.shape[1]
    rowCandidates = []
    colCandidates = []

    #get candidates
    for i in range(matrix.shape[0]-1):
        r1 = "".join(matrix[i])
        r2 = "".join(matrix[i+1])

        if r1 == r2:
            rowCandidates.append((i,i+1))
    for i in range(matrix.shape[1] - 1):
        c1 = "".join(matrix[:,i])
        c2 = "".join(matrix[:,i + 1])

        if c1 == c2:
            colCandidates.append((i, i + 1))

    #check col candidates if matrix is mirrored
    for c1, c2 in colCandidates:
        if colLen - 1 - c2 <= c1 - 1:
            cnt = 0
            isMirrored = True
            for i in range(c2 + 1, colLen, 1):
                cnt += 1
                if "".join(matrix[:, i]) != "".join(matrix[:, c1 - cnt]):
                    isMirrored = False
                    break
            if isMirrored:
                total += c2
        else:
            cnt = 0
            isMirrored = True
            for i in range(c1 - 1, -1, -1):
                cnt += 1
                if "".join(matrix[:, i]) != "".join(matrix[:, c2 + cnt]):
                    isMirrored = False
                    break
            if isMirrored:
                total += c2

    #check row candidates if matrix is mirrored
    for r1, r2 in rowCandidates:
        if rowLen - 1 - r2 <= r1 - 1:
            cnt = 0
            isMirrored = True
            for i in range(r2 + 1, rowLen, 1):
                cnt += 1
                if "".join(matrix[i]) != "".join(matrix[r1 - cnt]):
                    isMirrored = False
                    break
            if isMirrored:
                total += r2 * 100
        else:
            cnt = 0
            isMirrored = True
            for i in range(r1 - 1, -1, -1):
                cnt += 1
                if "".join(matrix[i]) != "".join(matrix[r2 + cnt]):
                    isMirrored = False
                    break
            if isMirrored:
                total += r2 * 100

print(total)