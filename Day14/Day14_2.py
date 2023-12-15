import numpy as np

def getIndexToMove(matrix, row, col):
    topElements = matrix[0:row,col][::-1]
    if len(topElements) == 0:
        return 0
    else:
        for ind,c in enumerate(topElements):
            if c == '.':
                continue
            if c in 'O#':
                return row-ind
                break
        return 0


content = [line.replace("\n", "") for line in open("day14.txt", encoding="utf8").readlines()]
matrix_data = [list(line) for line in content]
matrix = np.array(matrix_data)

for loop in range(1000):
    for tiltCnt in range(4):
        for i in range(1,matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if matrix[i,j] == 'O':
                    new_i = getIndexToMove(matrix, i, j)
                    if i != new_i:
                        tmp = matrix[new_i,j].copy()
                        matrix[new_i,j] = matrix[i,j].copy()
                        matrix[i,j] = tmp.copy()
        matrix = np.rot90(matrix, k=-1)

total = 0
top = matrix.shape[0]
for i in range(top):
    row = matrix[i,:]
    cnt = np.count_nonzero(row == 'O')
    total += (top-i)*cnt

print(total)