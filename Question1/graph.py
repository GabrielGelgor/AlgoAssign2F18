class Graph():
    def __init__(self, n):
        self.n = n
        self.adjMatrix = []
        for i in range (0,n):
            self.adjMatrix.append([0]*n)

    def BFSpartition(self, i, AssignmentList):
        adjList = []
        adjList.append(i)

        AssignmentList[i] = 1

        while (len(adjList) > 0):

            root = adjList.pop(0)

            for vertex in range(0,self.n):
                if (root == vertex): continue

                elif (self.adjMatrix[root][vertex] == 0 and AssignmentList[root] == AssignmentList[vertex]):
                    return False

                elif (self.adjMatrix[root][vertex] == 0 and AssignmentList[root] != AssignmentList[vertex]):
                    if (AssignmentList[vertex] == 0):
                        adjList.append(vertex)
                    AssignmentList[vertex] = 3 - AssignmentList[root]
        return True
