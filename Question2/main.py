import struct, math, fcns

nodes = fcns.nodify([[10,5,13],[3,9,18],[10,2,2]])

min_sum = struct.Sum([], math.inf)
cur_sum = struct.Sum([], 0)
p=0
col_left = len(nodes) 

while col_left > 0:

    for j in range (len(nodes[p])):
        if (nodes[p][j].status == "open" and ((cur_sum.val + nodes[p][j].val) < min_sum.val)):
            fcns.blockDown(nodes, p, j)
            cur_sum.val += nodes[p][j].val
            cur_sum.List.append(j)

            print(cur_sum.val)

            p += 1
            break

        elif (j == len(nodes[p])-1):
            for c in range(len(nodes[p])):
                if nodes[p][c].status == "blocked" and (c not in cur_sum.List):
                    nodes[p][c].status = "open"

            p -= 1

            print("\nj: ", cur_sum.val)

            cur_sum.val -= nodes[p][cur_sum.List[-1]].val
            fcns.unBlock(nodes, p, cur_sum.List[-1])
            del cur_sum.List[-1]

            if (p == 0):
                col_left -= 1

            break

    if (p == (len(nodes)-1)):
        min_sum.val = cur_sum.val
        min_sum.List = cur_sum.List

        print("Subtraction here: ", nodes[p][cur_sum.List[-1]].val)

        cur_sum.val -= nodes[p][cur_sum.List[-1]].val
        fcns.blockDown(nodes, p, cur_sum.List[-1])
        del cur_sum.List[-1]

print(min_sum.List,",",min_sum.val)