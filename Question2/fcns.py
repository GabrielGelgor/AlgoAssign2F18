import struct

def nodify (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = struct.node(matrix[i][j])

    return matrix

def blockDown (matrix, p, j):
    for i in range(p+1,len(matrix)):
        matrix[i][j].status="blocked"

def unBlock (matrix, p, j):
    matrix[p][j].status = "blocked"
    for i in range(p+1,len(matrix)):
        if matrix[i][j].status == "blocked":
            matrix[i][j].status = "open"
