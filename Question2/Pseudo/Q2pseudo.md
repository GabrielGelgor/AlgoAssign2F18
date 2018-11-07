```
nodes <- 2D job/employee matrix.  

min_sum = ([], infinity)  
sum = ([], 0)  
top_columns_left = jobs.length
person = 0  

while (top_columns_left > 0)
    for job = 0 upto jobs.length  
        if ( nodes[person][job].status = "open" and (nodes[person][job].value + sum.value < min_sum.value) )  
            blockDown(nodes[person][job])                                                                              //Prevents all people below in this column from getting this job.  
            sum.list.append(job)  
            sum.val += nodes[person][job].val  

            if (person < nodes[person].length-1):
                person += 1
            break
            
        elif job=(jobs.length-1)  
            for col in range(len(nodes[person])):
                if nodes[person][col].status == "blocked" and (col not in cur_sum.List):                                //Removes temporary blocks
                    nodes[person][col].status = "open"

            if (person = 0)                                                                                             //In the case that the current line is the first
                nodes[person][job].status = "blocked"
                col_left -= 1
                break

            person -= 1
            sum.val -= nodes[person][sum.list[-1]].val
            unBlock(nodes[person][job])                                                                                 //Makes this job available for all employees (execept most recent holder) once more.
            cur_sum.List[-1].remove() 

            if (person = 0)
                col_left -= 1

            break  
                 
            
    if (people = people.length-1):  
        min_sum.list.append( sum.list )  
        min_sum.val = sum.val
        sum.val -= nodes[person][sum.list[-1]]  
        unBlock( nodes[person][sum.list[-1]] )
        sum.list[-1].remove()  

```
