def dfs(paths , start):
    edges = {}
    unvisted = []
    stack = [start]
    dfs_order = []
    
    for s , e in paths:

        if s not in edges.keys(): edges[s] = []
        if e not in edges.keys(): edges[e] = []

        if s not in unvisted: unvisted.append(s)
        if e not in unvisted: unvisted.append(e)
        
        edges[s].append(e)
        edges[e].append(s)

    while unvisted:
        dfs_order.append(stack[-1])
        stack_pop_value = stack[-1]
        unvisted.remove(stack[-1])
        stack.pop()

        for value in edges[stack_pop_value]:
            if value in unvisted: stack.append(value)
    
    for node in dfs_order[:len(dfs_order) - 1]: print("{} -> ".format(node) , end="")
    print(dfs_order[-1])

dfs([["A" , "C"] ,
    ["A" , "B"] , 
    ["B" , "E"] ,
    ["B" , "D"] ,
    ["D" , "C"] ,
    ["E" , "D"] ], "B")