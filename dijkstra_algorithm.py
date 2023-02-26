def print_results(weights , shortest_paths , root):
    for vertex in sorted(weights.keys()):
        print("from {} to {} : \n\t Shortes path : {} \n\t Minimum weight : {} \n"
        .format(root , vertex , shortest_paths[vertex] , weights[vertex]))

# Dijkstra Algorithm 
def dijkstra(paths , visited , unvisited  ,  root):
    start = root
    weights = {x : float('inf') for x in unvisited}
    shortest_paths = {x : "" for x in unvisited}
    weights[root] = 0
    shortest_paths[root] = root
    
    while True:
        visited.append(root)
        unvisited.remove(root)
        
        for a , b , c in paths:
            if a == root and weights[b] > (weights[a] + int(c)) and b in unvisited:
                weights[b] = weights[a] + int(c)
                shortest_paths[b] = shortest_paths[a] + " -> " + b
                
        if(len(unvisited) == 1):
            break
        else:
            root = sorted(sorted(weights.items() , key = lambda x:x[0]) , key = lambda x:x[1])[len(visited)][0]
    # print(weights)
    # print(shortest_paths)
    print_results(weights , shortest_paths , start)

# Find Vertices
def find_vertex(paths , root):
    visited = []
    unvisited = []
    mirror_paths = []
    for a , b ,c in paths:
        if a not in unvisited:
            unvisited.append(a)
        if b not in unvisited:
            unvisited.append(b)
        mirror_paths.append([b,a,c])
    paths.extend(mirror_paths)
    dijkstra(paths , visited , unvisited , root)

path_count = int(input("Enter edge count : "))
paths = []
n = 0
for _ in range(path_count):
    n += 1
    paths.append(input("Enter edge {} : ".format(n)).split(" "))
root = input("Enter root vertex : ")
find_vertex(paths , root)



#Sample Input - 1
#7
# A B 5
# B E 10
# E D 10
# E C 30
# D C 20
# D B 35
# C A 10
# A

#Sample Input - 2
#17
# A B 3
# A E 7
# A G 5
# B C 7
# B E 1
# C E 2
# C F 2
# C D 1
# D F 3
# D I 5
# I F 2
# I H 4
# H F 3
# H E 3
# H G 2
# G E 3
# E F 1
# B
