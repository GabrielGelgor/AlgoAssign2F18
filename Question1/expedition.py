import graph

expeditiongraph = graph.Graph(5)
expeditiongraph.adjMatrix = [[0,1,1,0,0],[1,0,1,0,0],[1,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0]]

AssignmentList = []
isPossible = False

for i in range(0,5):
    AssignmentList.append(0)

for i in range(0,5):
    if (AssignmentList[i] == 0):
         isPossible = expeditiongraph.BFSpartition(i, AssignmentList)
         if (isPossible == False):
             break

if (isPossible == False):
    print("There is no possible solution for the given input")
else:
    for i in range(0,5):
        if (AssignmentList[i] == 1):
            print(i)
