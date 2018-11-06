import struct

def nodify (matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = struct.node(matrix[i][j])

    return matrix
