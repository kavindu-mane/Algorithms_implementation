def traverse(graph , root , weights , visited):

    for key , value in graph[root].items():

        if(weights[key] > (int(value) + weights[root])):
            weights[key] = int(value) + weights[root]

        visited.append(root)

    for key in graph[root].keys():
            if key not in visited:
                traverse(graph , key , weights, visited)

def bellman_ford(paths , root):
    graph = {}

    for s , e , w in paths:
        if s not in graph.keys():
            graph[s] = {}

        if e not in graph[s].keys() or graph[s][w] > w:
            graph[s][e] = w

    weights = {x : float('inf') for x in graph.keys()}
    weights[root] = 0
    loop_count = len(graph.keys()) - 1
    previous = None
    current = None

    for _ in range(loop_count):

        traverse(graph , root , weights , [])
        current , previous =  weights.copy() , current

        if(current == previous):
            print(weights)
            break
    else:
        print("This graph has negative loops.Therefore no any final answer")

               
    
path_count = int(input("Enter edge count : "))
paths = []
n = 0
for _ in range(path_count):
    n += 1
    paths.append(input("Enter edge {} : ".format(n)).split(" "))
root = input("Enter root vertex : ")
bellman_ford(paths , root)


# Sample input - 1
# 10
# A B 3
# A C 5
# C D 4
# D B 2
# B C 3
# E F 10
# F A 12
# F E 2
# E D 3
# B F 7
# B

# Sample input - 1
#5
# A B 3
# A C 5
# C D 4
# D B -10
# B C 3
# A