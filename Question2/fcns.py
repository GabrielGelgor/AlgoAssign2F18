import struct

def nodify (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = struct.node(matrix[i][j])

    return matrix

def blockDown (matrix, p, j):
    for i in range(p+1,len(matrix)):
        matrix[i][j].status="blocked"
#        print(matrix[i][j].val," Has been blocked.")

def unBlock (matrix, p, j):
    matrix[p][j].status = "blocked"
#    print(matrix[p][j].val," Has been banned.")
    for i in range(p+1,len(matrix)):
        if matrix[i][j].status == "blocked":
            matrix[i][j].status = "open"
#            print(matrix[i][j].val," Has been unblocked.")
