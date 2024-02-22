import numpy as np
import heapq

def is_valid_position(matrix, row, col):
    return 0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]

content = [line.replace("\n", "") for line in open("day17.txt", encoding="utf8").readlines()]
matrix_data = [list(map(int,line)) for line in content]
matrix = np.array(matrix_data)

alreadyVisited = set()
moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

#hl = heatloss
#r = row we are currently at
#c = column we are currently at
#dr = row direction we are currently traveling; 1 moving over rows down, -1 moving over rows up
#dc = column direction we are currently traveling; 1 moving over columns right, -1 moving over columns left
#n = number of steps we are moving in the same direction
hl, r, c, dr, dc, n = 0, 0, 0, 0, 0, 0

pq = [(0,0,0,0,0,0)]

while pq:
    hl, r, c, dr, dc, n = heapq.heappop(pq)

    if r == matrix.shape[0]-1 and c == matrix.shape[1]-1:
        print(hl)
        break

    if is_valid_position(matrix, r, c) == False:
        continue

    if (r,c,dr,dc,n) in alreadyVisited:
        continue

    alreadyVisited.add((r,c,dr,dc,n))

    if n < 3 and (dr,dc) != (0,0):
        nr = r + dr
        nc = c + dc
        if is_valid_position(matrix, nr, nc):
            heapq.heappush(pq, (hl + matrix[nr,nc],nr,nc,dr,dc,n+1))

    for ndr, ndc in moves:
        if (ndr,ndc) != (dr,dc) and (ndr,ndc) != (-dr,-dc):
            nr = r + ndr
            nc = c + ndc
            if is_valid_position(matrix, nr, nc):
                heapq.heappush(pq, (hl + matrix[nr, nc], nr, nc, ndr, ndc, 1))
