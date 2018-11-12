import struct, math, fcns

nodes = fcns.nodify([[10,3,10,7,7],[5,9,7,11,9],[13,18,2,9,10],[15,13,2,7,4],[16,6,2,12,12]])

min_sum = struct.Sum([], math.inf)
cur_sum = struct.Sum([], 0)
p = 0
col_left = len(nodes) 

while col_left > 0:

    for j in range (len(nodes[p])):
        if (nodes[p][j].status == "open" and ((cur_sum.val + nodes[p][j].val) < min_sum.val)):
            fcns.blockDown(nodes, p, j)
            cur_sum.val += nodes[p][j].val
            cur_sum.List.append(j)

            if (p < (len(nodes[p])-1)):
                p += 1
            break

        elif (j == len(nodes[p])-1):
            for c in range(len(nodes[p])):
                if nodes[p][c].status == "blocked" and (c not in cur_sum.List):
                    nodes[p][c].status = "open"

            if (p == 0):
                nodes[p][j].status = "blocked"
                col_left -= 1
                break 

            p -= 1
            cur_sum.val -= nodes[p][cur_sum.List[-1]].val
            fcns.unBlock(nodes, p, cur_sum.List[-1])
            del cur_sum.List[-1]

            if (p == 0):
                col_left -= 1

            break

    if (p == (len(nodes)-1) and (len(cur_sum.List) == len(nodes[0]))):
        min_sum.val = cur_sum.val
        min_sum.List = cur_sum.List[:]
        cur_sum.val -= nodes[p][cur_sum.List[-1]].val
        nodes[p][cur_sum.List[-1]].status = "blocked"
        del cur_sum.List[-1]

print("Employee Order: ", min_sum.List,", Minimum Time: ",min_sum.val," Hours.")