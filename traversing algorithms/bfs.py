def bfs(paths , start):
    edges = {}
    unvisted = []
    queue = [start]
    bfs_order = []
    
    for s , e in paths:

        if s not in edges.keys(): edges[s] = []
        if e not in edges.keys(): edges[e] = []

        if s not in unvisted: unvisted.append(s)
        if e not in unvisted: unvisted.append(e)
        
        edges[s].append(e)
        edges[e].append(s)

    while unvisted:
        bfs_order.append(queue[0])

        for value in edges[queue[0]]:
            if value in unvisted and value not in queue: queue.append(value)

        unvisted.remove(queue[0])
        queue.pop(0)
    
    for node in bfs_order[:len(bfs_order) - 1]: print("{} -> ".format(node) , end="")
    print(bfs_order[-1])

bfs([["A" , "B"] ,
    ["A" , "C"] , 
    ["B" , "E"] ,
    ["B" , "D"] ,
    ["E" , "D"] ,
    ["D" , "C"]], "A")