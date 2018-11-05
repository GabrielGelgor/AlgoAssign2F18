```
nodes <- 2D job/employee matrix.  

min_sum = ([], infinity)  
sum = ([], 0)  

for p=0 upto people.length  
    for j=0 upto jobs.length  
        if ( nodes[p][j].status="open" and (sum.val + nodes[p][j].val) < min_sum.val )  
            sum.list.append(j)  
            sum.val += nodes[p][j].val  
            blockDown(nodes[p][j])                <- Blocks all people below from getting this job.  
            break
            
        else  
            if j=(jobs.length-1)  
                p--  
                sum.val -= nodes[p][sum.list[-1]]  
                unBlock( nodes[p][sum.list[-1]] ) <- Has functionality of making this node permablocked  
                sum.list[-1].remove()  
                break  
                
            continue 
            
    if (people.length-1):  
        min_sum.list.append( sum.list )  
        min_sum.val = sum.val  
```
