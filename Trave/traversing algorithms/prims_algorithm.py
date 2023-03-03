# Prims Algorithm 
def prims(paths , visited , unvisited , weight ,  root):
    least_edge = float('inf')
    end_vertex = ''
    visited.append(root)
    unvisited.remove(root)
    if(len(unvisited) == 0):
        return weight
        
    for vertex in visited:
        for a , b ,c in paths:
            if a == vertex and (least_edge > int(c)) and b in unvisited:
                end_vertex = b
                least_edge = int(c)
    return prims(paths , visited , unvisited , weight + least_edge ,  end_vertex)

# Find Vertices
def find_vertex(paths):
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
    weight = prims(paths , visited , unvisited , 0 , unvisited[0])
    print("Minimum cost : {}".format(weight))

path_count = int(input("Enter edge count : "))
paths = []
n = 0
for _ in range(path_count):
    n += 1
    paths.append(input("Enter edge {} : ".format(n)).split(" "))
find_vertex(paths)



#Sample Input
#7
#A B 5
#B E 10
#E D 10
#E C 30
#D C 20
#D B 35
#C A 10
