import numpy as np

def differ_by_one_char(s1, s2):
    diff_count = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

def getCurrentMirror(matrix):
    rowLen = matrix.shape[0]
    colLen = matrix.shape[1]
    rowCandidates = []
    colCandidates = []

    # get candidates
    for i in range(matrix.shape[0] - 1):
        r1 = "".join(matrix[i])
        r2 = "".join(matrix[i + 1])

        if r1 == r2:
            rowCandidates.append((i, i + 1))
    for i in range(matrix.shape[1] - 1):
        c1 = "".join(matrix[:, i])
        c2 = "".join(matrix[:, i + 1])

        if c1 == c2:
            colCandidates.append((i, i + 1))

    # check col candidates if matrix is mirrored
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
                return "c|{}|{}".format(c1, c2)
        else:
            cnt = 0
            isMirrored = True
            for i in range(c1 - 1, -1, -1):
                cnt += 1
                if "".join(matrix[:, i]) != "".join(matrix[:, c2 + cnt]):
                    isMirrored = False
                    break
            if isMirrored:
                return "c|{}|{}".format(c1, c2)

    # check row candidates if matrix is mirrored
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
                return "r|{}|{}".format(r1, r2)
        else:
            cnt = 0
            isMirrored = True
            for i in range(r1 - 1, -1, -1):
                cnt += 1
                if "".join(matrix[i]) != "".join(matrix[r2 + cnt]):
                    isMirrored = False
                    break
            if isMirrored:
                return "r|{}|{}".format(r1, r2)
    return "NotFound"

def getTotal(matrix, currentMirror):
    total = 0
    rowCurrent = set()
    colCurrent = set()

    if currentMirror.startswith('r'):
        rowCurrent=(int(currentMirror.split('|')[1]),int(currentMirror.split('|')[2]))
    if currentMirror.startswith('c'):
        colCurrent=(int(currentMirror.split('|')[1]),int(currentMirror.split('|')[2]))

    rowLen = matrix.shape[0]
    colLen = matrix.shape[1]
    rowCandidates = []
    colCandidates = []

    # get candidates
    for i in range(matrix.shape[0] - 1):
        r1 = "".join(matrix[i])
        r2 = "".join(matrix[i + 1])

        if r1 == r2:
            rowCandidates.append((i, i + 1))
    for i in range(matrix.shape[1] - 1):
        c1 = "".join(matrix[:, i])
        c2 = "".join(matrix[:, i + 1])

        if c1 == c2:
            colCandidates.append((i, i + 1))

    # check col candidates if matrix is mirrored
    for c1, c2 in colCandidates:
        if colLen - 1 - c2 <= c1 - 1:
            cnt = 0
            isMirrored = True
            for i in range(c2 + 1, colLen, 1):
                cnt += 1
                if "".join(matrix[:, i]) != "".join(matrix[:, c1 - cnt]):
                    isMirrored = False
                    break
            if isMirrored and (c1, c2) != colCurrent and (c2, c1) != colCurrent:
                total += c2
        else:
            cnt = 0
            isMirrored = True
            for i in range(c1 - 1, -1, -1):
                cnt += 1
                if "".join(matrix[:, i]) != "".join(matrix[:, c2 + cnt]):
                    isMirrored = False
                    break
            if isMirrored and (c1, c2) != colCurrent and (c2, c1) != colCurrent:
                total += c2

    # check row candidates if matrix is mirrored
    for r1, r2 in rowCandidates:
        if rowLen - 1 - r2 <= r1 - 1:
            cnt = 0
            isMirrored = True
            for i in range(r2 + 1, rowLen, 1):
                cnt += 1
                if "".join(matrix[i]) != "".join(matrix[r1 - cnt]):
                    isMirrored = False
                    break
            if isMirrored and (r1, r2) != rowCurrent and (r2, r1) != rowCurrent:
                total += r2 * 100
        else:
            cnt = 0
            isMirrored = True
            for i in range(r1 - 1, -1, -1):
                cnt += 1
                if "".join(matrix[i]) != "".join(matrix[r2 + cnt]):
                    isMirrored = False
                    break
            if isMirrored and (r1, r2) != rowCurrent and (r2, r1) != rowCurrent:
                total += r2 * 100
    return total

content = open("day13.txt", encoding="utf8").read()
contentList = content.split('\n\n')
sumTotal = 0

for part in contentList:
    matrix_data = [list(line) for line in part.split('\n')]
    matrix = np.array(matrix_data)

    currentMirror = getCurrentMirror(matrix)
    total = 0

    #find smudge
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            if differ_by_one_char("".join(matrix[i]),"".join(matrix[j])) == 1:
                temp_matrix = matrix.copy()
                temp_matrix[i, :] = matrix[j, :].copy()
                total = getTotal(temp_matrix, currentMirror)
                if total == 0:
                    temp_matrix = matrix.copy()
                    temp_matrix[j, :] = matrix[i, :].copy()
                    total = getTotal(temp_matrix, currentMirror)
                    if total != 0:
                        break
                else:
                    break
        else:
            continue
        break

    if total == 0:
        for i in range(matrix.shape[1]):
            for j in range(matrix.shape[1]):
                if differ_by_one_char("".join(matrix[:,i]), "".join(matrix[:,j])) == 1:
                    temp_matrix = matrix.copy()
                    temp_matrix[:, i] = matrix[:, j].copy()
                    total = getTotal(temp_matrix, currentMirror)
                    if total == 0:
                        temp_matrix = matrix.copy()
                        temp_matrix[:, j] = matrix[:, i].copy()
                        total = getTotal(temp_matrix, currentMirror)
                        if total != 0:
                            break
                    else:
                        break
            else:
                continue
            break

    sumTotal += total

print(sumTotal)